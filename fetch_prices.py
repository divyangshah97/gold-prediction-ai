"""
Fetches daily OHLC + volume for Gold, Silver, DXY, WTI Crude via yfinance
and appends a row to prices/prices.csv.

Usage:
  python fetch_prices.py            # append today (or last trading day)
  python fetch_prices.py --backfill # seed last 6 months of history
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
    "Gold_USD":              "GC=F",
    "Silver_USD":            "SI=F",
    "DXY":                   "DX-Y.NYB",
    "WTI_Crude":             "CL=F",
}
# Volume is taken from Gold futures only
VOLUME_TICKER = "GC=F"

FIELDNAMES = ["Date", "Gold_USD", "Silver_USD", "DXY", "WTI_Crude", "Gold_Volume_Contracts"]

# Browser-like headers to avoid 403 blocks from Yahoo Finance in cloud environments
HEADERS = {
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


def make_session():
    """Return a requests.Session with browser-like headers."""
    s = requests.Session()
    s.headers.update(HEADERS)
    return s


def load_existing_dates():
    if not os.path.exists(PRICES_CSV):
        return set()
    with open(PRICES_CSV, newline="", encoding="utf-8") as f:
        return {r["Date"] for r in csv.DictReader(f)}


def fetch_ticker(symbol, start, end, session, retries=MAX_RETRIES):
    """Download a single ticker with retry logic. Returns DataFrame or None."""
    for attempt in range(1, retries + 1):
        try:
            t = yf.Ticker(symbol, session=session)
            df = t.history(start=start, end=end, auto_adjust=True)
            if not df.empty:
                return df
            # Empty can mean market closed — return as-is, not an error
            return df
        except Exception as exc:
            print(f"  [{symbol}] attempt {attempt}/{retries} failed: {exc}")
            if attempt < retries:
                time.sleep(RETRY_DELAY)
    return None


def fetch_range(start: str, end: str) -> list[dict]:
    """Download data for all tickers between start and end (inclusive)."""
    session = make_session()
    data = {}

    for col, symbol in TICKERS.items():
        df = fetch_ticker(symbol, start, end, session)
        if df is None or df.empty:
            print(f"  [{symbol}] no data returned (market may be closed or 403 persists)")
            continue

        # yfinance Ticker.history() returns simple column names: Close, Volume, …
        for ts, row in df.iterrows():
            day = str(ts.date()) if hasattr(ts, "date") else str(ts)[:10]
            if day not in data:
                data[day] = {}
            close_val = row.get("Close")
            if close_val is not None:
                data[day][col] = round(float(close_val), 4)
            if col == "Gold_USD":
                vol = row.get("Volume")
                if vol is not None:
                    data[day]["Gold_Volume_Contracts"] = int(vol)

    rows = []
    for day in sorted(data.keys()):
        row = {"Date": day}
        for col in FIELDNAMES[1:]:
            row[col] = data[day].get(col, "")
        rows.append(row)
    return rows


def append_rows(new_rows: list[dict]):
    existing = load_existing_dates()
    to_write  = [r for r in new_rows if r["Date"] not in existing]
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
        print(f"  {r['Date']}  Gold={r['Gold_USD']}  Silver={r['Silver_USD']}  DXY={r['DXY']}  WTI={r['WTI_Crude']}  Vol={r['Gold_Volume_Contracts']}")


def run_backfill(months: int = 6):
    end   = date.today() + timedelta(days=1)
    start = date.today() - timedelta(days=30 * months)
    print(f"Backfilling {start} to {end} ...")
    rows = fetch_range(str(start), str(end))
    append_rows(rows)


def run_today():
    # Fetch last 5 days to ensure we catch the most recent trading day
    end   = date.today() + timedelta(days=1)
    start = date.today() - timedelta(days=5)
    rows  = fetch_range(str(start), str(end))
    if rows:
        # Only append the latest row (most recent trading day)
        append_rows([rows[-1]])
    else:
        print("No data returned from yfinance.")


if __name__ == "__main__":
    if "--backfill" in sys.argv:
        run_backfill()
    else:
        run_today()
