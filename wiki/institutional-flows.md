# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand.

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures).

**Last updated**: 2026-06-13

---

## Why This Matters

Central banks are the structural buyer. But institutions and hedge funds drive short-to-medium term price momentum. Two data series capture this:

1. **GLD ETF Tonnes** — SPDR GLD holds physical gold. Daily changes in holdings reflect institutional buy/sell flow. A rising GLD tonne count = institutions adding gold exposure. A falling count = profit-taking or risk-off rotation out of gold.

2. **CFTC COT Managed Money** — Every Tuesday, COMEX gold futures positions are recorded. The "Managed Money" category (hedge funds, CTAs, asset managers) shows their net long/short stance. Published every Friday. Key: this is a contrarian indicator at extremes — when MM net-long is historically high, the easy money is made and a correction is likely. When MM is near net-short, upside risk is elevated.

## Signal Rule (Factor 6 in Daily Trading Signal)

| Condition | Score |
|---|---|
| GLD inflows AND MM net-long increasing | +1 Bullish |
| GLD outflows AND MM net-short increasing | -1 Bearish |
| Signals contradict each other | 0 Neutral |
| Only one source available — use that signal | ±1 or 0 |
| No recent data (>7 days old) or GLD_MISSING | 0 Neutral |

## GLD ETF Holdings (Daily)

Data file: `prices/gld.csv`

| Column | Description |
|---|---|
| Date | Trading date |
| GLD_Tonnes | Total gold held by SPDR GLD ETF in tonnes |
| GLD_Tonnes_Change | Day-over-day change in tonnes (+ve = inflows, -ve = outflows) |

*Populated by the daily routine. First entry: 2026-05-30 onwards.*

## CFTC COT Managed Money (Weekly)

Data file: `prices/cot.csv`

| Column | Description |
|---|---|
| Report_Date | Tuesday "as-of" date for the CFTC report |
| Open_Interest | Total COMEX gold futures open interest (contracts, 1 contract = 100 troy oz) |
| MM_Long | Managed Money gross long positions |
| MM_Short | Managed Money gross short positions |
| MM_Net | Net position (Long − Short) |
| MM_Net_Change | Change in MM_Net from prior week |

*Populated by the Saturday COT routine. First entry: first Saturday after 2026-05-30.*

## Context: What Are "Extreme" Readings?

Historically for COMEX gold:
- **Very bullish extremes** (contrarian caution): MM_Net > 250,000 contracts net long
- **Very bearish extremes** (contrarian opportunity): MM_Net < 50,000 contracts or net short
- **Normal range**: 100,000–200,000 contracts net long

These thresholds shift over time as open interest grows. Always compare MM_Net as a % of Open_Interest for a cleaner read.

## Latest COT Data

> **Report_Date (as-of Tuesday):** 2026-06-02  
> **Published by CFTC:** 2026-06-05  
> **Source:** CFTC Disaggregated Futures Only report, COMEX Gold 100 troy oz (code 088691) — sourced via IndexBox.io CFTC COT summary (June 5, 2026 release)

| Field | Value |
|---|---|
| Report_Date | 2026-06-02 |
| Open_Interest | 326,052 contracts |
| MM_Long | 129,367 contracts |
| MM_Short | 17,188 contracts |
| MM_Net | +112,179 contracts |
| MM_Net_Change | +18,639 vs. prior entry (2026-05-19) |
| MM_Net % of OI | 34.4% |
| **Sentiment** | **Neutral zone (50,000–150,000)** |

### Sentiment Interpretation (as of June 2)

MM_Net of +112,179 falls in the **Neutral zone (50,000–150,000 contracts)**. Managed Money has increased net-long exposure meaningfully — shorts dropped sharply from 29,354 to 17,188 (−12,166), while longs rose modestly from 122,894 to 129,367 (+6,473). The positioning move is being driven primarily by short-covering rather than fresh long accumulation.

**Week-over-week change of +18,639 contracts** (from May 19 baseline of +93,540) is just below the ±20,000 significant shift threshold. Not a flag, but approaching notable territory.

**Open Interest contraction is notable:** OI fell from 379,325 (May 19) to 326,052 (June 2), a drop of ~53,000 contracts (−14%). This alongside a rising MM_Net suggests short-covering-driven position reduction rather than fresh speculative enthusiasm.

---

## June 9, 2026 COT Update — Data Retrieval Failure

> **Report_Date (as-of Tuesday):** 2026-06-09  
> **Published by CFTC:** 2026-06-12 (Friday)  
> **Retrieval attempted:** 2026-06-13 (Saturday routine)  
> **Status:** ⚠️ Data not retrieved — all sources blocked by network egress policy

### Sources Attempted

All of the following returned 403 Forbidden or DNS resolution failure due to environment network restrictions:

- **CFTC direct** (`www.cftc.gov`, `data.cftc.gov`, `publicreporting.cftc.gov`) — domain not in network allowlist
- **GoldSeek** `goldseek.com/article/cot-gold-silver-usdx-report-june-12-2026` — 403
- **Barchart, MetalCharts, MacroMicro, YCharts, Investing.com, Kitco, StoneX, Titan FX, InsiderWeek, TradingView** — all 403
- **InvestMacro** — no June 2026 articles indexed yet at time of search
- **Web search snippets** — returned qualitative commentary only; no specific disaggregated managed money contract counts for June 9

The June 12, 2026 COT release exists and contains the June 9 data, but it could not be accessed from this environment. The `cot.csv` file has **not** been updated for this week.

### Market Context for June 9 Positioning (Gold: $4,338.50)

Gold price on June 9 (COT as-of date): **$4,338.50/oz** — down $160.50 (−3.57%) from the June 2 close of $4,499.00.

Key drivers between June 2 and June 9 that would have influenced managed money positioning:
- **June 5**: Strong US NFP (+251K) = gold headwind, DXY lift
- **June 8**: Gold closed at $4,329.33, continuing NFP-driven selloff
- **June 9**: Slight bounce to $4,338.50 (+$9.17) — moderate bearish week overall

**What to expect in the June 9 data (qualitative):**
- Multiple sources (web search snippets) suggest gold speculative net positions fell to a "six-week low" for the week ending June 9, though this could not be confirmed with specific contract counts
- MM_Long likely decreased from 129,367 given the 3.6% price drop and NFP headwinds
- MM_Short potentially rose from the 17-month low of 17,188 (June 2) as traders added defensive hedges
- OI likely continued to fall (was at 19-month low as of June 2)
- Estimated MM_Net direction: **lower** than 112,179 (June 2)
- If "six-week low" characterization is accurate, MM_Net may have approached the May 19 level of ~93,540

> **Action required:** Retry data fetch next Saturday. Check `www.cftc.gov` domain allowlist in network egress settings, or ensure one of the following data aggregators is reachable: GoldSeek, Barchart, MetalCharts, InvestMacro (June 2026 articles).

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
