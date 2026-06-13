# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand.

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures).

**Last updated**: 2026-06-13 (COT June 9 data retrieved via web search fallback)

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

> **Report_Date (as-of Tuesday):** 2026-06-09  
> **Published by CFTC:** 2026-06-12 (Friday)  
> **Retrieved:** 2026-06-13 (Saturday routine) via web search fallback — direct API (Nasdaq Data Link) and WebFetch blocked by network egress; figures sourced from search aggregators citing CFTC Disaggregated Futures Only report, COMEX Gold 100 troy oz (code 088691)

| Field | Value |
|---|---|
| Report_Date | 2026-06-09 |
| Open_Interest | 332,709 contracts |
| MM_Long | 126,280 contracts |
| MM_Short | 20,417 contracts |
| MM_Net | +105,863 contracts |
| MM_Net_Change | −6,316 vs. prior week (2026-06-02: +112,179) |
| MM_Net % of OI | 31.8% |
| **Sentiment** | **Neutral zone (50,000–150,000)** |

### Sentiment Interpretation (as of June 9)

MM_Net of +105,863 falls in the **Neutral zone (50,000–150,000 contracts)**. Managed Money trimmed net exposure modestly — longs fell from 129,367 to 126,280 (−3,087), while shorts rose from 17,188 to 20,417 (+3,229). Both legs moved in a bearish direction, but the scale is modest.

**Week-over-week change of −6,316 contracts** is well below the ±20,000 significant shift threshold — no flag. This is consistent with the NFP-driven gold price pullback in the week ending June 9 (gold fell from ~$4,499 to ~$4,339, −3.6%), with managed money reducing exposure cautiously rather than aggressively liquidating.

**Open Interest recovered slightly:** OI rose from 326,052 (June 2) to 332,709 (June 9), +6,657 contracts (+2.0%). This is a tentative stabilisation after the June 2 OI hit a multi-month low.

**Historical context:** This is the third consecutive week in the Neutral zone. MM_Net has pulled back from the May 19 reading of +93,540, recovered to +112,179 on June 2 (short-covering driven), and now sits at +105,863. The pattern suggests no strong directional conviction from managed money.

---

## Prior Week Reference

> **Report_Date:** 2026-06-02 | **MM_Net:** +112,179 | **OI:** 326,052 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-05-19 | **MM_Net:** +93,540 | **OI:** 379,325 | **Sentiment:** Neutral zone

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
