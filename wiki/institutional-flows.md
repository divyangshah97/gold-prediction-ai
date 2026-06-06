# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand.

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures).

**Last updated**: 2026-06-06

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

### Sentiment Interpretation

MM_Net of +112,179 falls in the **Neutral zone (50,000–150,000 contracts)**. Managed Money has increased net-long exposure meaningfully — shorts dropped sharply from 29,354 to 17,188 (−12,166), while longs rose modestly from 122,894 to 129,367 (+6,473). The positioning move is being driven primarily by short-covering rather than fresh long accumulation.

**Week-over-week change of +18,639 contracts** (from May 19 baseline of +93,540) is just below the ±20,000 significant shift threshold. Not a flag, but approaching notable territory — watch next week for continuation.

**Open Interest contraction is notable:** OI fell from 379,325 (May 19) to 326,052 (June 2), a drop of ~53,000 contracts (−14%). This alongside a rising MM_Net suggests short-covering-driven position reduction rather than fresh speculative enthusiasm. Fewer total contracts outstanding with more net-long bias = a tighter, less liquid market.

**Context:** Gold price was ~$4,446–$4,499 as of June 2 (June 2 close ~$4,499, June 5 close ~$4,446 post-NFP). The strong US NFP report (+251K) released June 5 is a gold headwind. MM positioning as of Tuesday June 2 pre-dates the NFP reaction, so the next COT report (as of June 9) may reflect NFP-driven repositioning.

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
