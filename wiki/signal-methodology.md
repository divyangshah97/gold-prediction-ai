# Trading Signal Methodology

**Summary**: Documents the five-factor scoring system used to generate daily gold trading signals. Each factor scores -1 (Bearish), 0 (Neutral), or +1 (Bullish). Range -5 to +5. Factors 1 (Price vs Targets) and 4 (Central Bank Demand) were retired 2026-07-25 as poor fits for a 2-3 month trading horizon; Factor 7 (Real Yields/TIPS) was added the same day.

**Sources**: Routine design (`trig_01Q7FfuV2Y2Fqk4f8dtokd2J`), updated 2026-07-25.

**Last updated**: 2026-07-25

---

## Overview

The daily signal is produced automatically by the routine each weekday at 12:00 PM IST. It scores five independent factors and maps the sum to a signal label. Results are appended to `signals/signals.csv`.

**Signal range:** -5 to +5
**Output file:** `signals/signals.csv` (columns: Date, Signal, Score, Reasoning) — **restarted fresh 2026-07-25**; the prior six-factor (-6/+6) and seven-factor history lives in `signals/signals_archive_2026-05-22_to_2026-07-24.csv` (44 rows, 2026-05-22 through 2026-07-24). Do not append new rows to the archive file.

## Why Factors 1 and 4 were retired (2026-07-25)

Prompted by a review of which factors actually move gold within a 2-3 month futures trading horizon (see `wiki/log.md` 2026-07-25 entries for the full discussion):

- **Factor 1 (Price vs Targets)** anchors off Goldman/JPM/UBS year-end targets ([[goldman-sachs-gold-forecast]]) — a multi-month/annual valuation view. A >15%-below-target reading says nothing about the next 2-3 months; gold can stay "cheap" (or get cheaper) for a long time. Better suited to a long-term thesis than a quarterly trading signal.
- **Factor 4 (Central Bank Demand)** is monthly/quarterly reported data with a lag ([[central-bank-gold-demand]], [[global-cb-activity-log]]) — it moves the multi-year price floor, not next quarter's futures price. It was also structurally asymmetric (could only ever score 0 or +1, never bearish), which biased the composite score.

The remaining five factors (2, 3, 5, 6, 7) were kept because they transmit to gold within days to a few weeks — the relevant window for a 2-3 month futures position. Numbering is preserved from the original six/seven-factor systems (no Factor 1 or Factor 4 in the table below) so historical `signals_archive_*.csv` reasoning text stays interpretable.

**Global CB sweep research (Step 3 Topic 1 in the routine) and Goldman/bank forecast tracking are unaffected** — they still update `wiki/global-cb-activity-log.md`, country pages, and `wiki/goldman-sachs-gold-forecast.md` for wiki completeness. Only their role in the *signal score* was removed.

## Price data basis (changed 2026-07-18)

`prices/prices.csv` records **official previous-day closes**, not live prices. `fetch_prices.py` appends only *completed* trading sessions (yfinance daily closes for GC=F, SI=F, DX-Y.NYB, CL=F, USDINR=X) — never the in-progress bar. When the routine runs at ~12 PM IST on day T, the newest CSV row is day T-1.

**Why:** before 2026-07-18 the routine wrote the *live spot price at run time* (~12 PM IST) into the CSV as "today's" row. Day-over-day deltas were therefore noon-to-noon snapshot changes that missed each day's US session — on 2026-07-17 this scored "last 2 days green" when the real closes for Jul 15/16 were both red, flipping Factor 5. The routine must **never** write a live/intraday price into `prices/prices.csv`; live spot may be quoted in report text only.

**Row history:** rows from **2026-06-25 onward** are official daily closes (rewritten 2026-07-18); rows up to **2026-06-24** are legacy ~12 PM IST snapshots. The one delta spanning the boundary (Jun 24→25) mixes the two bases.

## Signal Thresholds

**Live from 2026-07-27 onward (five-factor, -5 to +5)**:

| Net score | Signal |
|---|---|
| +5 | Strong Buy |
| +3 to +4 | Buy |
| -2 to +2 | Wait |
| -3 to -4 | Sell |
| -5 | Strong Sell |

**Historical (six-factor, -6/+6, Jun 18 – Jul 24) and seven-factor (-7/+7, briefly configured Jul 25) thresholds** are documented in the Historical Signal Log below for reference when reading `signals_archive_2026-05-22_to_2026-07-24.csv`.

---

## The Five Factors

### Factor 2 — Geopolitical Risk

Evaluates whether geopolitical events are *actually transmitting* to gold, not just making headlines.

| Condition | Score |
|---|---|
| Event triggers safe-haven flows INTO gold with USD flat or weakening | +1 Bullish |
| Ambiguous — no clear gold direction | 0 Neutral |
| De-escalation; OR escalation driving USD strength; OR risk already priced in | -1 Bearish |

**Key rule:** De-escalation is not automatically bearish. If a peace deal reduces oil prices → lowers inflation → weakens USD → gold can rally *because* of de-escalation (the macro channel). Evaluate the transmission, not the headline.

**Horizon note:** Immediate but episodic — moves gold within hours of a shock, but isn't a factor you can plan a position around in advance. Treat as an event-risk overlay on the other four factors, not a standalone trend signal.

**Data source:** Daily web research in Step 3. See [[gold-geopolitical-risk-premium]], [[iran-conflict-2026]], [[us-china-trade-war]].

---

### Factor 3 — Fed / Macro

Evaluates Federal Reserve posture and broader macro environment.

| Condition | Score |
|---|---|
| Dovish signal (rate cut hint, pause extension, inflation easing) | +1 Bullish |
| No change / unchanged guidance | 0 Neutral |
| Hawkish surprise (rate hike signal, sticky inflation, dot plot shift up) | -1 Bearish |

**Horizon note:** Re-scores on the macro calendar cadence (FOMC every ~6 weeks, monthly CPI/PPI/NFP) — each print can shift the multi-week trend. Good fit for a 2-3 month horizon: effectively trading the next 2-4 macro data releases.

**Data source:** Daily web research. See [[fed-macro-factors]].

---

### Factor 5 — Technicals

Uses live EMAs from a mandatory daily web search (never from wiki — those are stale). Reads last 3 rows of `prices/prices.csv` for recent price direction.

**EMA rule table:**

| Price position | MA config | Last 2 days | Score |
|---|---|---|---|
| Above both EMAs | Either | 2 green | +1 Bullish |
| Above both EMAs | Either | Not 2 green | -1 Bearish |
| Above 9d, below 50d | 50d > 9d (downtrend) | Any | -1 Bearish |
| Below 9d, above 50d | 9d > 50d (uptrend) | Any | +1 Bullish |
| Below both EMAs | Either | 2 green | +1 Bullish |
| Below both EMAs | Either | Not 2 green | -1 Bearish |

**"2 green" — explicit definition (fixes prior ambiguity/mis-scoring bug):**

A day is **green** if that day's XAU/USD close is higher than the *previous row's* close in `prices/prices.csv` (i.e. day-over-day change > 0). A day is **red** if the close is lower or unchanged.

"2 green" = the last two rows of `prices/prices.csv` are *both* green by that definition — meaning you need 3 consecutive rows to evaluate the two most recent day-over-day deltas. Do not substitute intraday candle color, weekly direction, or "price is up over the last 2 days" (a single two-day-span comparison) — check each of the two most recent day-over-day deltas independently and both must be positive.

Since the 2026-07-18 close-basis change, the CSV's newest row on signal day T is the *previous* completed day (T-1), so "last 2 days" naturally means the two most recent **completed** sessions (T-1 and T-2) — evaluate the last two rows as-is after `fetch_prices.py` runs; never append or use a live intraday price.

**"Price position"** (vs the two EMAs) is also evaluated with the newest CSV row's close — the last completed session — not a live intraday price.

**Horizon note:** By construction a short-to-medium trend-following signal tuned for exactly this horizon. It's a lagging confirmation of where Factors 3/6/7 have already pushed price, not an independent driver — most useful for entry timing within a position.

**Data source:** Web search for "XAU/USD 9 day EMA today" and "gold 50 day EMA [month year]" + last 3 rows of `prices/prices.csv` (need 3 rows to compute 2 day-over-day deltas).

---

### Factor 6 — Dollar Pressure (DXY + USD/INR)

Added 2026-06-18. Uses both the US Dollar Index (DXY) and the USD/INR exchange rate to capture dollar strength from two angles: global (DXY) and India-specific (MCX gold price impact).

**Logic:**

```python
dxy_pct = (today_DXY - prev_DXY) / prev_DXY * 100
inr_pct = (today_USD_INR - prev_USD_INR) / prev_USD_INR * 100

dxy_signal = -1 if dxy_pct >= +0.5 else (+1 if dxy_pct <= -0.5 else 0)
inr_signal = +1 if inr_pct >= +0.5 else (-1 if inr_pct <= -0.5 else 0)

factor6 = clamp(dxy_signal + inr_signal, -1, +1)
```

**Threshold changed from ±1.0% to ±0.5% on 2026-07-02** (was too wide — daily DXY/USD-INR moves rarely hit 1%, so Factor 6 almost always scored 0/neutral even when the dollar was meaningfully moving).

**Why USD/INR up = +1:** Gold in INR (MCX price) = Gold in USD × USD/INR. When the rupee weakens (USD/INR rises), MCX gold rises automatically even if COMEX price is flat — bullish for Indian gold holders and demand.

**Scoring table:**

| DXY move | USD/INR move | factor6 | Reason |
|---|---|---|---|
| up ≥0.5% | up ≥0.5% | **0** | Neutralised: COMEX gold falls (-1) but MCX/INR gold rises (+1) |
| up ≥0.5% | within 0.5% | **-1** | Dollar strengthening, bearish gold in USD |
| up ≥0.5% | down ≥0.5% | **-1** | Double bearish: both COMEX and MCX gold fall |
| down ≥0.5% | down ≥0.5% | **0** | Neutralised: COMEX gold rises (+1) but MCX/INR gold falls (-1) |
| down ≥0.5% | within 0.5% | **+1** | Dollar weakening, bullish gold in USD |
| down ≥0.5% | up ≥0.5% | **+1** | Double bullish: both COMEX and MCX gold rise |
| within 0.5% | up ≥0.5% | **+1** | Rupee weakening → MCX gold price rises |
| within 0.5% | down ≥0.5% | **-1** | Rupee strengthening → MCX gold price falls |
| within 0.5% | within 0.5% | **0** | No significant move in either |

**Real example (June 18, 2026):** DXY +0.49% (within 1%) + FOMC hawkish dot plot. DXY alone didn't trigger the factor; the -1 came from Factor 3 (hawkish Fed). Had DXY been +1.2%, Factor 6 would have added a second -1 → score shifts down one band.

**Horizon note:** Fastest-transmitting factor — DXY/USD-INR moves are near-mechanically inverse to gold intraday/daily. Highest relevance for near-term entry/exit timing.

**Data source:** Last 2 rows of `prices/prices.csv` (DXY and USD_INR columns). If either column is missing/blank, that component scores 0.

---

### Factor 7 — Real Yields (TIPS)

**Live from 2026-07-25.** Uses the 10-year TIPS yield (FRED `DFII10`) as a direct measure of gold's opportunity cost, distinct from the qualitative Fed-posture read in Factor 3. Fetched in routine Step 1c and stored in `prices/real_yields.csv` (new sidecar file, separate from `prices/prices.csv`).

| Condition | Score |
|---|---|
| 10Y real yield fell ≥3bps day-over-day | +1 Bullish |
| Real yield roughly flat (within ±3bps) | 0 Neutral |
| 10Y real yield rose ≥3bps day-over-day | -1 Bearish |
| Fewer than 2 rows in `real_yields.csv` (insufficient history) | 0 Neutral |

**Threshold note:** 3bps was chosen as a starting calibration (same pattern as Factor 6's ±1.0%→±0.5% tightening on 2026-07-02) — revisit once a few weeks of real signal data accumulate.

**Horizon note:** Second-fastest-transmitting factor after Factor 6 — real yields move on every CPI/PPI print and FOMC event, and gold typically reprices against them same-day to within a week. More precise than Factor 3 alone because it strips out Fed rhetoric that doesn't actually move real rates.

**Data source:** FRED `DFII10` (https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10) or daily web search fallback ("10 year TIPS yield today"). See [[real-yields-tips]].

---

## Historical Signal Log

Current signals are stored in `signals/signals.csv` (restarted 2026-07-25). Prior history (2026-05-22 through 2026-07-24, six/seven-factor systems) is preserved in `signals/signals_archive_2026-05-22_to_2026-07-24.csv` and summarized below:

| Period | Factors | Range | File |
|---|---|---|---|
| May 21 – May 29, 2026 | 5 factors (Price, Geo, Fed, CB, Technicals) | -5 to +5 | archive |
| May 30 – Jun 17, 2026 | 5 factors (same) | -5 to +5 | archive |
| Jun 18 – Jul 24, 2026 | 6 factors (+ Dollar Pressure) | -6 to +6 | archive |
| Jul 25, 2026 (config only, no live runs) | 7 factors (+ Real Yields/TIPS) | -7 to +7 | — |
| **Jul 27, 2026 onward** | **5 factors (Geo, Fed, Technicals, Dollar, Real Yields — Price & CB Demand retired)** | **-5 to +5** | `signals.csv` |

**Note on the 2026-07-25 seven-factor configuration:** Factor 7 was added and briefly live-configured in the routine at -7/+7 before Factors 1 and 4 were retired the same day, before any run actually executed under that config. No signals were generated under the seven-factor system — the archive's last row (Jul 24) is still six-factor, and `signals.csv`'s first row (expected Jul 27) is five-factor.

**Note on threshold change (Jun 18):** the Wait band widened slightly (-2 to +2 instead of -1 to +1) at the six-factor transition; the five-factor Jul 27 restart uses the identical band shape to the original May 2026 five-factor system.

---

## Related pages

- [[gold-geopolitical-risk-premium]]
- [[fed-macro-factors]]
- [[central-bank-gold-demand]]
- [[goldman-sachs-gold-forecast]]
- [[institutional-flows]]
- [[global-cb-activity-log]]
- [[real-yields-tips]]
