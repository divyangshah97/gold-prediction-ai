"""
Fetches daily OHLC + volume for Gold, Silver, DXY, WTI Crude via yfinance
and appends a row to prices/prices.csv.

Fallback chain:
  Gold, Silver : yfinance (3 retries + browser UA)  →  metals.dev API
  DXY, WTI     : yfinance only — prints DXY_MISSING / WTI_MISSING if yfinance fails
                 (the calling routine should patch those via web search)
  Volume       : Yahoo Finance JSON API (primary, direct HTTP — bypasses yfinance 403)
                 → yfinance (fallback)
                 → prints VOLUME_MISSING if both fail

Only COMPLETED trading days are appended (previous day's official close, never
the live/in-progress price) — Factor 5 green/red scoring needs true daily closes.

Usage:
  python fetch_prices.py                        # append last completed trading day(s)
  python fetch_prices.py --backfill             # seed last 6 months of history
  python fetch_prices.py --metals-key YOUR_KEY  # override metals.dev key (env: METALS_DEV_KEY)
"""

import csv
import os
import sys
import time
from datetime import date, timedelta

try:
    import requests
except ImportError:
    raise SystemExit("Install requests first:  pip install requests")

try:
    import yfinance as yf
except ImportError:
    raise SystemExit("Install yfinance first:  pip install yfinance")

PRICES_CSV = os.path.join(os.path.dirname(__file__), "prices", "prices.csv")

TICKERS = {
    "Gold_USD":   "GC=F",
    "Silver_USD": "SI=F",
    "DXY":        "DX-Y.NYB",
    "WTI_Crude":  "CL=F",
    "USD_INR":    "USDINR=X",
}

FIELDNAMES = ["Date", "Gold_USD", "Silver_USD", "DXY", "WTI_Crude", "Gold_Volume_Contracts", "USD_INR"]

# Browser-like headers — avoids Yahoo Finance 403 blocks in cloud environments
_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds between retries


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(_BROWSER_HEADERS)
    return s


def _migrate_csv():
    """Rewrite prices.csv header if new FIELDNAMES columns are missing (non-destructive)."""
    if not os.path.exists(PRICES_CSV):
        return
    with open(PRICES_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        existing_fields = list(reader.fieldnames or [])
        if set(FIELDNAMES) <= set(existing_fields):
            return
        rows = list(reader)
    new_cols = set(FIELDNAMES) - set(existing_fields)
    with open(PRICES_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({fn: row.get(fn, "") for fn in FIELDNAMES})
    print(f"[migration] Added column(s) {new_cols} to prices.csv (existing rows left blank)")


def load_existing_dates() -> set:
    if not os.path.exists(PRICES_CSV):
        return set()
    with open(PRICES_CSV, newline="", encoding="utf-8") as f:
        return {r["Date"] for r in csv.DictReader(f)}


# ---------------------------------------------------------------------------
# yfinance fetch (with retry)
# ---------------------------------------------------------------------------

def _fetch_yf(symbol: str, start: str, end: str, session: requests.Session):
    """Return yfinance DataFrame or None after MAX_RETRIES failures."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            ticker = yf.Ticker(symbol, session=session)
            df = ticker.history(start=start, end=end, auto_adjust=True)
            return df  # may be empty on market holidays — that's OK
        except Exception as exc:
            print(f"  [yfinance/{symbol}] attempt {attempt}/{MAX_RETRIES} failed: {exc}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
    return None


# ---------------------------------------------------------------------------
# Yahoo Finance JSON API — primary volume source
# ---------------------------------------------------------------------------

def _fetch_yahoo_api_volume(days_back: int = 10) -> dict:
    """
    Fetch COMEX gold futures daily volume via Yahoo Finance JSON API.
    Returns {date_str: volume_int} for the last `days_back` trading days.
    This endpoint works in cloud environments where the yfinance library gets 403-blocked.
    """
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/GC=F?interval=1d&range={days_back}d"
    try:
        resp = requests.get(url, timeout=10, headers=_BROWSER_HEADERS)
        resp.raise_for_status()
        body = resp.json()
        result_list = body.get("chart", {}).get("result") or []
        if not result_list:
            print("  [yahoo-api/volume] empty result")
            return {}
        result = result_list[0]
        timestamps = result.get("timestamp", [])
        quote = result.get("indicators", {}).get("quote", [{}])[0]
        volumes = quote.get("volume", [])
        out = {}
        import datetime
        for ts, vol in zip(timestamps, volumes):
            if vol is None:
                continue
            day = datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
            out[day] = int(vol)
        print(f"  [yahoo-api/volume] fetched {len(out)} day(s): {sorted(out.keys())[-3:]}")
        return out
    except Exception as exc:
        print(f"  [yahoo-api/volume] error: {exc}")
        return {}


# ---------------------------------------------------------------------------
# metals.dev fallback (Gold + Silver only)
# ---------------------------------------------------------------------------

def _fetch_metals_dev(key: str) -> dict:
    """
    Fetch Gold and Silver spot prices from metals.dev.
    Returns dict like {"Gold_USD": 3245.6, "Silver_USD": 32.4} or {}.
    """
    try:
        url = (
            f"https://api.metals.dev/v1/latest"
            f"?api_key={key}&currency=USD&unit=toz"
        )
        resp = requests.get(url, timeout=10, headers=_BROWSER_HEADERS)
        resp.raise_for_status()
        body = resp.json()
        if body.get("status") != "success":
            print(f"  [metals.dev] unexpected response: {body.get('status')}")
            return {}
        metals = body.get("metals", {})
        result = {}
        if "gold" in metals:
            result["Gold_USD"] = round(float(metals["gold"]), 4)
        if "silver" in metals:
            result["Silver_USD"] = round(float(metals["silver"]), 4)
        return result
    except Exception as exc:
        print(f"  [metals.dev] fallback error: {exc}")
        return {}


# ---------------------------------------------------------------------------
# Core fetch logic
# ---------------------------------------------------------------------------

def fetch_range(start: str, end: str, metals_key: str = None) -> list[dict]:
    """
    Download data for all tickers between start and end (inclusive).
    Returns list of row dicts ready to write to CSV.
    Prints DXY_MISSING / WTI_MISSING if those fields cannot be fetched.
    """
    session = _make_session()
    data: dict[str, dict] = {}
    yf_failed = set()  # tracks which columns yfinance could not fetch

    for col, symbol in TICKERS.items():
        df = _fetch_yf(symbol, start, end, session)
        if df is None or df.empty:
            print(f"  [yfinance/{symbol}] no data (market closed or 403 persists)")
            yf_failed.add(col)
            continue

        for ts, row in df.iterrows():
            day = str(ts.date()) if hasattr(ts, "date") else str(ts)[:10]
            data.setdefault(day, {})
            close = row.get("Close")
            if close is not None:
                data[day][col] = round(float(close), 4)
            if col == "Gold_USD":
                vol = row.get("Volume")
                if vol is not None:
                    data[day]["Gold_Volume_Contracts"] = int(vol)

    # --- Yahoo Finance direct API: primary volume source ---
    yahoo_volumes = _fetch_yahoo_api_volume()
    for day, vol in yahoo_volumes.items():
        if day in data:
            if vol > 0:
                data[day]["Gold_Volume_Contracts"] = vol
                print(f"  [yahoo-api/volume] {day} volume = {vol}")
        # Also seed volume for days not yet in data (e.g. when yfinance failed entirely)
        elif vol > 0:
            data.setdefault(day, {})["Gold_Volume_Contracts"] = vol

    # --- metals.dev fallback for Gold / Silver ---
    needs_fallback = yf_failed & {"Gold_USD", "Silver_USD"}
    if needs_fallback and metals_key:
        print(f"  [fallback] yfinance failed for {needs_fallback} — trying metals.dev ...")
        md = _fetch_metals_dev(metals_key)
        if md:
            today_str = str(date.today())
            data.setdefault(today_str, {})
            for field in needs_fallback:
                if field in md:
                    data[today_str][field] = md[field]
                    print(f"  [metals.dev] {field} = {md[field]}")
    elif needs_fallback and not metals_key:
        print(
            f"  [metals.dev] METALS_DEV_KEY not set — cannot fall back for {needs_fallback}"
        )

    # --- signal missing fields for caller to patch via web search ---
    today_str = str(date.today())
    latest_day = max(data.keys()) if data else today_str
    for col in ("DXY", "WTI_Crude", "USD_INR"):
        if col in yf_failed or not data.get(latest_day, {}).get(col):
            print(f"{col}_MISSING")   # sentinel read by the routine prompt
    if not data.get(latest_day, {}).get("Gold_Volume_Contracts"):
        print("VOLUME_MISSING")       # sentinel: both yahoo-api and yfinance failed

    # Build output rows
    rows = []
    for day in sorted(data.keys()):
        row = {"Date": day}
        for col in FIELDNAMES[1:]:
            row[col] = data[day].get(col, "")
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# CSV write helpers
# ---------------------------------------------------------------------------

def append_rows(new_rows: list[dict]):
    _migrate_csv()
    existing = load_existing_dates()
    to_write = [r for r in new_rows if r["Date"] not in existing]
    if not to_write:
        print("Nothing new to append — all dates already in CSV.")
        return

    write_header = not os.path.exists(PRICES_CSV)
    with open(PRICES_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerows(to_write)

    print(f"Appended {len(to_write)} row(s) to {PRICES_CSV}")
    for r in to_write:
        print(
            f"  {r['Date']}  Gold={r['Gold_USD']}  Silver={r['Silver_USD']}"
            f"  DXY={r['DXY']}  WTI={r['WTI_Crude']}  Vol={r['Gold_Volume_Contracts']}"
            f"  USD_INR={r['USD_INR']}"
        )


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------

def _parse_metals_key() -> str | None:
    """Resolve metals.dev API key: --metals-key arg > METALS_DEV_KEY env var."""
    if "--metals-key" in sys.argv:
        idx = sys.argv.index("--metals-key")
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return os.environ.get("METALS_DEV_KEY")


def run_backfill(months: int = 6, metals_key: str = None):
    end   = date.today() + timedelta(days=1)
    start = date.today() - timedelta(days=30 * months)
    print(f"Backfilling {start} → {end} ...")
    rows = fetch_range(str(start), str(end), metals_key)
    append_rows(rows)


def run_today(metals_key: str = None):
    # Append only COMPLETED trading days (Date < today, UTC).
    # yfinance returns an in-progress bar for the current session, so appending
    # rows[-1] unfiltered would freeze a mid-session price (~12 PM IST when the
    # daily routine runs) into the CSV instead of a real daily close — this
    # corrupted Factor 5 green/red scoring before 2026-07-18.
    end   = date.today() + timedelta(days=1)
    start = date.today() - timedelta(days=7)
    rows  = fetch_range(str(start), str(end), metals_key)
    today_str = str(date.today())
    completed = [r for r in rows if r["Date"] < today_str]
    if completed:
        append_rows(completed)  # append_rows skips dates already in the CSV
    else:
        print("No completed trading day returned from yfinance or fallback.")


if __name__ == "__main__":
    _key = _parse_metals_key()
    if "--backfill" in sys.argv:
        run_backfill(metals_key=_key)
    else:
        run_today(metals_key=_key)
