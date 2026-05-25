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
from datetime import date, timedelta

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


def load_existing_dates():
    if not os.path.exists(PRICES_CSV):
        return set()
    with open(PRICES_CSV, newline="", encoding="utf-8") as f:
        return {r["Date"] for r in csv.DictReader(f)}


def fetch_range(start: str, end: str) -> list[dict]:
    """Download data for all tickers between start and end (inclusive)."""
    data = {}
    for col, symbol in TICKERS.items():
        df = yf.download(symbol, start=start, end=end, auto_adjust=True, progress=False)
        if df.empty:
            continue
        # yfinance returns multi-level columns: ("Close", ticker) — flatten
        close_series = df[("Close", symbol)].dropna()
        vol_series   = df[("Volume", symbol)].dropna() if col == "Gold_USD" else None
        for ts, close in close_series.items():
            day = str(ts.date()) if hasattr(ts, "date") else str(ts)[:10]
            if day not in data:
                data[day] = {}
            data[day][col] = round(float(close), 4)
            if vol_series is not None and ts in vol_series.index:
                data[day]["Gold_Volume_Contracts"] = int(vol_series[ts])

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
