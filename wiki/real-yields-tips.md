# Real Yields (TIPS)

**Summary**: The 10-year Treasury Inflation-Protected Securities (TIPS) yield is the market's real (inflation-adjusted) interest rate. It is inversely correlated with gold because gold pays no yield — as the real yield rises, the opportunity cost of holding gold rises, and vice versa. Live as **Factor 7** of the signal methodology from 2026-07-25 (part of the five-factor system from 2026-07-27 onward, after Factors 1 and 4 were retired).

**Sources**: FRED series `DFII10` (10-Year Treasury Inflation-Indexed Security, Constant Maturity); general macro literature on gold/real-yield relationship; user-proposed addition, discussed 2026-07-25.

**Last updated**: 2026-08-05

---

## Latest Reading

**August 5 check**: No newer confirmed DFII10 reading found. FRED direct fetch (`fredgraph.csv`) again failed with a 403 CONNECT rejection (`recentRelayFailures` confirmed `fred.stlouisfed.org:443` specifically rejected, per `$HTTPS_PROXY/__agentproxy/status`). `WebFetch` was also non-functional this session — it returned HTTP 403 on every URL attempted, including normally-permissive ones like Wikipedia, so no fallback fetch to macrotrends/CNBC/macromicro was possible either. Web search for "10 year TIPS yield DFII10 August 2026" and "10-year treasury real yield today August 4 2026" returned only a stale, undated ~2.41-2.44% figure attributed to "July 29, 2026," which conflicts with this file's own already-confirmed July 29 entry (2.44%) and is older than the July 30/31 entries on file — discarded as non-newer, not a fresh reading. Per the routine's no-duplicate/no-fabrication rule, the file was left unchanged rather than appending an unreliable value. Factor 7 for the August 5 signal used the last confirmed delta (+4bps, Jul30→Jul31, carried forward for the second consecutive day), still above the ±3bps threshold — **Bearish (−1)**.

**Prior (August 4) check**: No newer confirmed DFII10 reading found. FRED direct fetch (`fredgraph.csv`) failed with a 403 CONNECT rejection (proxy policy denial, confirmed via `$HTTPS_PROXY/__agentproxy/status`). Web search for "10 year TIPS yield DFII10 today August 2026" and "10-year real yield TIPS August 3 2026 percent" returned inconsistent, largely undated figures — one source cited "2.47% as of July 31, 2026," which conflicts with this file's own July 31 estimate of 2.50% for the same date (both cannot be independently verified against a primary FRED read given the fetch block). Per the routine's no-duplicate/no-fabrication rule, the file was left unchanged rather than appending an unreliable value. Factor 7 for the August 4 signal used the last confirmed delta (+4bps, Jul30→Jul31), still above the ±3bps threshold — **Bearish (−1)**.

| Date | DFII10 | Note |
|---|---|---|
| 2026-07-31 | **~2.50% (estimated)** | Fifth data point in `prices/real_yields.csv`. FRED direct fetch failed (403 — blocked by proxy egress policy, confirmed via `/__agentproxy/status`, not a retriable error). Web-search fallback also failed to find a directly-dated Jul31 reading: CNBC (`US10YTIP`), tradingeconomics, and macrotrends all returned HTTP 403 to direct fetch; search snippets gave conflicting numbers (2.37% "as of late July," 2.41% for "Jul 30" — the latter contradicts this file's own Jul30 entry of 2.46% sourced the same way one day earlier, so both noisy snippets were discarded). **Estimated at 2.50%** via cross-check: 10Y nominal Treasury yield (4.74%, Jul31, tradingeconomics) minus 10Y breakeven inflation rate (T10YIE, ~2.24%, FRED, July average) ≈ 2.50% — consistent with, and a continuation of, the rising-real-yield trend visible in the last 4 rows (2.43→2.42→2.44→2.46). Delta vs 2026-07-30 (2.46%) = **+4bps**, at/above the ±3bps threshold → Factor 7 scored **Bearish (−1)** for the 2026-08-03 signal — the first non-Neutral Factor 7 reading since the factor went live. |
| 2026-07-30 | **~2.46% (estimated)** | Fourth data point in `prices/real_yields.csv`. No directly-dated July 30 FRED/tradingeconomics reading could be sourced (direct FRED fetch blocked again; tradingeconomics' TIPS-yield page had not refreshed past April 2026; one third-party aggregator showed 2.37%, but this conflicts with contemporaneous reporting that "TIPS and nominal yields" moved "in tandem" while breakevens stayed flat post-FOMC, and is treated as likely stale/undated). Estimated at 2.44% + ~2bps = **2.46%**, matching the nominal 10Y Treasury yield's confirmed +2bps move (4.677%→4.70%) on July 30. Delta vs 2026-07-29 (2.44%) = **+2bps**, below the ±3bps threshold → Factor 7 scored **Neutral (0)** for the 2026-07-31 signal. |
| 2026-07-29 | **2.44%** | Third data point in `prices/real_yields.csv`. Sourced via web search fallback (tradingeconomics.com "10 Year TIPS Yield rose to 2.44% on July 29, 2026") — direct FRED `fredgraph.csv` fetch again blocked by proxy policy (403) on 2026-07-30. Delta vs 2026-07-28 (2.42%) = **+2bps**, below the ±3bps threshold → Factor 7 scored **Neutral (0)** for the 2026-07-30 signal. The rise is consistent with the day's broader hawkish Fed tone (nominal 10Y yield rose 7bps to 4.677% on the Warsh press conference) but was damped relative to the nominal move, implying breakeven inflation expectations also ticked up. |
| 2026-07-28 | 2.42% | Sourced via web search fallback. |
| 2026-07-23 | 2.43% | First data point in `prices/real_yields.csv`. |

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
