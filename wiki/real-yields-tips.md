# Real Yields (TIPS)

**Summary**: The 10-year Treasury Inflation-Protected Securities (TIPS) yield is the market's real (inflation-adjusted) interest rate. It is inversely correlated with gold because gold pays no yield — as the real yield rises, the opportunity cost of holding gold rises, and vice versa. Live as **Factor 7** of the signal methodology from 2026-07-25 (part of the five-factor system from 2026-07-27 onward, after Factors 1 and 4 were retired).

**Sources**: FRED series `DFII10` (10-Year Treasury Inflation-Indexed Security, Constant Maturity); general macro literature on gold/real-yield relationship; user-proposed addition, discussed 2026-07-25.

**Last updated**: 2026-07-27

---

## Latest Reading

| Date | DFII10 | Note |
|---|---|---|
| 2026-07-23 | **2.43%** | First data point in `prices/real_yields.csv` (2026-07-27 run). Sourced via web search fallback (Fed H.15 release) — direct FRED `fredgraph.csv` fetch blocked by proxy policy (403) on 2026-07-27. Insufficient history (need 2+ rows) — Factor 7 scored **Neutral (0)** for the 2026-07-27 signal. |

## Why real yields matter more than nominal yields for gold

Nominal Treasury yields conflate two things: the real return investors demand and expected inflation. Gold is a hedge against the *inflation* component but has no yield of its own, so its true competitor is the **real** return available on safe assets — i.e., nominal yield minus expected inflation.

- **Real yield rising** → holding non-yielding gold costs more relative to TIPS/cash → bearish for gold.
- **Real yield falling (or negative)** → opportunity cost of gold shrinks → bullish for gold.

This is why gold and nominal yields can rise *together* (as they did in 2022–2023) when inflation expectations rise faster than nominal yields — real yields were falling even as nominal yields climbed. Tracking only nominal Fed policy (as [[fed-macro-factors]] does) can miss this divergence.

## Why this factor survived the 2026-07-25 factor review

A short-term-relevance review of all seven signal factors (2-3 month futures horizon) found real yields to be one of the fastest-transmitting drivers — real yields move on every CPI/PPI print and FOMC event, and gold typically reprices against them same-day to within a week. This is more precise than [[signal-methodology]] Factor 3 (Fed/Macro) alone, because Factor 3 scores qualitative Fed *rhetoric*, while Factor 7 scores the actual real-rate *outcome* — the two can diverge when inflation expectations move faster than nominal rate expectations. Factors 1 (Price vs Targets) and 4 (Central Bank Demand) were retired the same day for being poor fits to a quarterly trading horizon; Factor 7 was kept because it clears that bar.

## Relationship to existing wiki factors

[[fed-macro-factors]] tracks the *drivers* of real yields qualitatively (Fed rate path, CPI/PPI prints, fiscal deficit concerns) but does not track the TIPS yield itself as a number. The 10Y real yield is effectively a single summary statistic of the net effect of those drivers on gold's opportunity cost — it can move even when nominal Fed policy is unchanged, if inflation expectations shift.

## Data source

**FRED series `DFII10`** — 10-Year Treasury Inflation-Indexed Security, Constant Maturity Rate. Free, daily (business days), no API key required. Fetched by the routine in Step 1c via `curl "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10"`, with a web-search fallback, stored in `prices/real_yields.csv` (a sidecar file separate from `prices/prices.csv`, mirroring how EMAs are fetched fresh each run rather than persisted).

## Related pages

- [[signal-methodology]] — Factor 7 scoring definition
- [[fed-macro-factors]] — qualitative drivers of real yields (Fed policy, CPI/PPI, fiscal deficit)
- [[gold-geopolitical-risk-premium]]
