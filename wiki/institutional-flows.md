# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand.

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures).

**Last updated**: 2026-05-30

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

> **Report_Date (as-of Tuesday):** 2026-05-19
> **Published by CFTC:** 2026-05-22
> **Source:** CFTC Disaggregated Futures Only report, COMEX Gold 100 troy oz (code 088691) — sourced via CFTC data aggregated through web search (getarcresearch.com / CFTC public data)
>
> ⚠️ *Note: The 2026-05-26 report (published 2026-05-29) was not yet indexed by search engines as of 2026-05-30 morning. This entry uses the most recent confirmed disaggregated Managed Money data available.*

| Field | Value |
|---|---|
| Report_Date | 2026-05-19 |
| Open_Interest | 379,325 contracts |
| MM_Long | 122,894 contracts |
| MM_Short | 29,354 contracts |
| MM_Net | +93,540 contracts |
| MM_Net_Change | N/A (first entry) |
| MM_Net % of OI | 24.7% |
| **Sentiment** | **Neutral zone (50,000–150,000)** |

### Sentiment Interpretation

MM_Net of +93,540 falls in the **Neutral zone (50,000–150,000 contracts)**. Managed Money is modestly net long — neither crowded nor near net-short. There is meaningful room to add longs if a catalyst emerges. No contrarian warning applies here.

**Context from prior data:** As of 2026-04-28, MM_Net was +89,752 (source: getarcresearch.com). The modest increase to +93,540 by May 19 reflects a period of low-conviction repositioning amid the Iran MOU negotiation uncertainty and gold prices falling from the $5,200 ATH toward $4,500. Open interest of 379,325 is elevated, suggesting the market is actively engaged even with subdued MM directionality.

No significant positioning shift to flag (MM_Net_Change unavailable for week-over-week comparison; multi-week change from April 28 to May 19 is only +3,788 contracts).

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
