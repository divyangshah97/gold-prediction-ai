# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand.

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures).

**Last updated**: 2026-06-20 (COT June 16 data retrieval failed — all sources blocked by network egress; qualitative signals noted)

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

> **Report_Date (as-of Tuesday):** 2026-06-16 — **DATA RETRIEVAL FAILURE**  
> **Published by CFTC:** 2026-06-19 (Friday)  
> **Retrieved:** 2026-06-20 (Saturday routine) — Nasdaq Data Link API blocked (network egress); all financial data sites (CFTC.gov, barchart, metalcharts, tradingster, macromicro, ycharts, investing.com, titanfx, etc.) returned HTTP 403 Forbidden; WebSearch returned qualitative signals only (no verified exact figures).  
> **cot.csv:** NOT updated — no verified figures to append.

### What WebSearch Found (Qualitative Only)

The article "Metals Speculators Boost Gold Bets For 3rd Week To 14-Week Highs" (investing.com/analysis, published ~June 19–20, 2026) appeared in search results for the June 16 COT release. This suggests:
- MM_Net *increased* for the third consecutive week as of June 16
- Positions reached a **14-week high** (implying MM_Net is above all readings since approximately early March 2026)
- This is directionally bullish for Managed Money sentiment

**Prior confirmed reading (June 9, 2026):** MM_Net = +105,863 | OI = 332,709 | MM_Long = 126,280 | MM_Short = 20,417

### Prior Week Reference (Last Confirmed)

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

### Sentiment Interpretation (as of June 9 — last confirmed)

MM_Net of +105,863 falls in the **Neutral zone (50,000–150,000 contracts)**. Qualitative signals from the June 16 report suggest positioning increased to a 14-week high; the next confirmed data point will update this section.

**Prior-week-over-week change (June 9):** −6,316 contracts — below the ±20,000 significant shift threshold.

---

## Historical COT Reference

> **Report_Date:** 2026-06-09 | **MM_Net:** +105,863 | **OI:** 332,709 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-06-02 | **MM_Net:** +112,179 | **OI:** 326,052 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-05-19 | **MM_Net:** +93,540 | **OI:** 379,325 | **Sentiment:** Neutral zone

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
