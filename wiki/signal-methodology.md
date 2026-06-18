# Trading Signal Methodology

**Summary**: Documents the six-factor scoring system used to generate daily gold trading signals. Each factor scores -1 (Bearish), 0 (Neutral), or +1 (Bullish). Range -6 to +6.

**Sources**: Routine design (`trig_01Q7FfuV2Y2Fqk4f8dtokd2J`), updated 2026-06-18.

**Last updated**: 2026-06-18

---

## Overview

The daily signal is produced automatically by the routine each weekday at 12:00 PM IST. It scores six independent factors and maps the sum to a signal label. Results are appended to `signals/signals.csv`.

**Signal range:** -6 to +6  
**Output file:** `signals/signals.csv` (columns: Date, Signal, Score, Reasoning)

## Signal Thresholds

| Net score | Signal |
|---|---|
| +5 to +6 | Strong Buy |
| +3 to +4 | Buy |
| -2 to +2 | Wait |
| -3 to -4 | Sell |
| -5 to -6 | Strong Sell |

---

## The Six Factors

### Factor 1 — Price vs Targets

Measures how far current spot price is from analyst consensus targets.

| Condition | Score |
|---|---|
| Spot >15% below Goldman $5,400 target | +1 Bullish |
| Spot 5–15% below target | 0 Neutral |
| Spot at or above target | -1 Bearish |

**Data source:** Current XAU/USD from `prices/prices.csv` + Goldman/consensus targets from [[goldman-sachs-gold-forecast]].

---

### Factor 2 — Geopolitical Risk

Evaluates whether geopolitical events are *actually transmitting* to gold, not just making headlines.

| Condition | Score |
|---|---|
| Event triggers safe-haven flows INTO gold with USD flat or weakening | +1 Bullish |
| Ambiguous — no clear gold direction | 0 Neutral |
| De-escalation; OR escalation driving USD strength; OR risk already priced in | -1 Bearish |

**Key rule:** De-escalation is not automatically bearish. If a peace deal reduces oil prices → lowers inflation → weakens USD → gold can rally *because* of de-escalation (the macro channel). Evaluate the transmission, not the headline.

**Data source:** Daily web research in Step 3. See [[gold-geopolitical-risk-premium]], [[iran-conflict-2026]], [[us-china-trade-war]].

---

### Factor 3 — Fed / Macro

Evaluates Federal Reserve posture and broader macro environment.

| Condition | Score |
|---|---|
| Dovish signal (rate cut hint, pause extension, inflation easing) | +1 Bullish |
| No change / unchanged guidance | 0 Neutral |
| Hawkish surprise (rate hike signal, sticky inflation, dot plot shift up) | -1 Bearish |

**Data source:** Daily web research. See [[fed-macro-factors]].

---

### Factor 4 — Central Bank Demand

Only scores Bullish if **fresh data was published in the last 7 days**. Avoids double-counting stale data.

| Condition | Score |
|---|---|
| New CB demand data published in last 7 days (WGC report, Goldman nowcast, country purchase/sale announcement from today's CB sweep) | +1 Bullish |
| No new data in last 7 days | 0 Neutral |

**Note:** This factor never scores -1. Central bank selling (Turkey, Russia) is structural/fiscal, not a market signal — see [[russia-gold-reserves]], [[turkey-gold-reserves]].

**Data source:** Today's global CB sweep (Step 3 Topic 1) + [[central-bank-gold-demand]] + [[global-cb-activity-log]].

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

**Data source:** Web search for "XAU/USD 9 day EMA today" and "gold 50 day EMA [month year]" + last 3 rows of `prices/prices.csv`.

---

### Factor 6 — Dollar Pressure (DXY + USD/INR)

Added 2026-06-18. Uses both the US Dollar Index (DXY) and the USD/INR exchange rate to capture dollar strength from two angles: global (DXY) and India-specific (MCX gold price impact).

**Logic:**

```python
dxy_pct = (today_DXY - prev_DXY) / prev_DXY * 100
inr_pct = (today_USD_INR - prev_USD_INR) / prev_USD_INR * 100

dxy_signal = -1 if dxy_pct >= +1.0 else (+1 if dxy_pct <= -1.0 else 0)
inr_signal = +1 if inr_pct >= +1.0 else (-1 if inr_pct <= -1.0 else 0)

factor6 = clamp(dxy_signal + inr_signal, -1, +1)
```

**Why USD/INR up = +1:** Gold in INR (MCX price) = Gold in USD × USD/INR. When the rupee weakens (USD/INR rises), MCX gold rises automatically even if COMEX price is flat — bullish for Indian gold holders and demand.

**Scoring table:**

| DXY move | USD/INR move | factor6 | Reason |
|---|---|---|---|
| up ≥1% | up ≥1% | **0** | Neutralised: COMEX gold falls (-1) but MCX/INR gold rises (+1) |
| up ≥1% | within 1% | **-1** | Dollar strengthening, bearish gold in USD |
| up ≥1% | down ≥1% | **-1** | Double bearish: both COMEX and MCX gold fall |
| down ≥1% | down ≥1% | **0** | Neutralised: COMEX gold rises (+1) but MCX/INR gold falls (-1) |
| down ≥1% | within 1% | **+1** | Dollar weakening, bullish gold in USD |
| down ≥1% | up ≥1% | **+1** | Double bullish: both COMEX and MCX gold rise |
| within 1% | up ≥1% | **+1** | Rupee weakening → MCX gold price rises |
| within 1% | down ≥1% | **-1** | Rupee strengthening → MCX gold price falls |
| within 1% | within 1% | **0** | No significant move in either |

**Real example (June 18, 2026):** DXY +0.49% (within 1%) + FOMC hawkish dot plot. DXY alone didn't trigger the factor; the -1 came from Factor 3 (hawkish Fed). Had DXY been +1.2%, Factor 6 would have added a second -1 → score shifts down one band.

**Data source:** Last 2 rows of `prices/prices.csv` (DXY and USD_INR columns). If either column is missing/blank, that component scores 0.

---

## Historical Signal Log

Signals are stored in `signals/signals.csv`. The scoring system has evolved:

| Period | Factors | Range |
|---|---|---|
| May 21 – May 29, 2026 | 5 factors (Price, Geo, Fed, CB, Technicals) | -5 to +5 |
| May 30 – Jun 17, 2026 | 5 factors (same) | -5 to +5 |
| **Jun 18, 2026 onward** | **6 factors (+ Dollar Pressure)** | **-6 to +6** |

**Note on threshold change:** From June 18, the Wait band widened slightly (-2 to +2 instead of -1 to +1), making it harder to reach Buy/Sell without a majority of factors aligned.

---

## Related pages

- [[gold-geopolitical-risk-premium]]
- [[fed-macro-factors]]
- [[central-bank-gold-demand]]
- [[goldman-sachs-gold-forecast]]
- [[institutional-flows]]
- [[global-cb-activity-log]]
