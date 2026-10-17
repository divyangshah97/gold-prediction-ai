# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand. **July 29 update**: Global gold ETFs saw **$8.9bn of outflows in June** (though H1 2026 overall remained net positive at $8bn); AUM fell 6% in H1 to $526bn on lower gold prices even as collective holdings rose 18t to 4,047t. CFTC: COMEX managed-money net longs **jumped 16% m/m in June to 538t** — the highest month-end position since January 2026 — rising even as the gold price weakened, a notable divergence. Note: this page's Factor 6 description below (GLD/CFTC-based) is superseded — Factor 6 in the live signal methodology is now "Dollar Pressure" (DXY + USD/INR), not ETF/CFTC flows; see [[signal-methodology]].

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures), https://www.gold.org/goldhub/research/gold-etfs-holdings-and-flows/2026/07, https://en.macromicro.me/series/8308/gold-futures-and-options-manage-money-net-position, https://www.etfchannel.com/article/202607/spdr-gold-shares-gld-sees-notable-etf-inflows-as-investors-add-gold-exposure-GLD07162026inflow.htm/

**August 3 note**: As of July 30, 2026, GLD 5-day net flows were **+$189.64M**, 1-month net flows **+$581.24M**, but 3-month net flows remained **−$4.25B** — near-term inflows resuming after a sharply negative Q3-to-date. No August-dated GLD tonnage or fresh weekly CFTC COT print (next due Friday) found today; this factor is informational only (superseded by Factor 6 Dollar Pressure in the live signal, see [[signal-methodology]]).

**September 10 note**: New global context data point (not GLD-specific): China, India and Japan are reportedly driving renewed Asian gold-ETF demand, with **global gold ETF inflows hitting $18bn in August 2026** (Business Today, Sept 10, 2026) — directionally consistent with the July29-flagged H1 2026 net-positive trend, no contradicting signal found. No fresher GLD daily tonnage or CFTC COT print located this window; this factor remains informational only (superseded by Factor 6 Dollar Pressure in the live signal, see [[signal-methodology]]).

**Last updated**: 2026-10-17

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

> **Report_Date (as-of Tuesday):** 2026-10-13  
> **Published by CFTC:** 2026-10-16 (Friday)  
> **Retrieved:** 2026-10-16T22:56:50Z via GitHub Action (fetch_cot.yml) — CFTC direct disaggregated futures  
> **cot.csv:** Updated 2026-10-17 (Saturday routine)

| Field | Value |
|---|---|
| Report_Date | 2026-10-13 |
| Open_Interest | 396,345 contracts |
| MM_Long | 124,747 contracts |
| MM_Short | 17,658 contracts |
| MM_Net | +107,089 contracts |
| MM_Net_Change | −20,300 vs. last recorded week (2026-09-22: +127,389) |
| MM_Net % of OI | 27.0% |
| **Sentiment** | **Neutral zone (50,000–150,000)** |

### Sentiment Interpretation (as of October 13)

MM_Net of +107,089 sits in the **Neutral zone (50,000–150,000 contracts)**. Managed money net longs fell by −20,300 contracts versus the last recorded reading (2026-09-22: +127,389), the largest equivalent move since early September 2026, and the first reading below 110,000 contracts since early June 2026.

The composition shows a double-sided bearish shift: MM_Long declined from 135,699 to 124,747 (−10,952 contracts) while MM_Short simultaneously surged from 8,310 to 17,658 (+9,348 contracts) — longs exiting and fresh shorts entering at the same time. Open interest contracted from 412,800 to 396,345 (−16,455 contracts), consistent with net position liquidation across the board. MM_Net as % of OI stands at 27.0%, down sharply from 30.8% on 2026-09-22 — the lowest reading since early 2026.

**⚠️ SIGNIFICANT POSITIONING SHIFT**: Change of −20,300 contracts exceeds the ±20,000 threshold. Both long liquidation and new short-side entry are occurring simultaneously — hedge funds are actively reducing gold exposure and some are turning directionally short. This is a de-risking signal to watch.

**Data gap note**: Three weeks of COT data (2026-09-29, 2026-10-06) were not retrieved by the GitHub Action; the MM_Net_Change above spans the move from 2026-09-22 to 2026-10-13, not a strict week-over-week comparison. The pace of the shift may be distributed across multiple weeks.

---

## Historical COT Reference

> **Report_Date:** 2026-10-13 | **MM_Net:** +107,089 | **OI:** 396,345 | **Sentiment:** Neutral zone ⚠️ significant shift (−20,300)  
> **Report_Date:** 2026-09-22 | **MM_Net:** +127,389 | **OI:** 412,800 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-09-15 | **MM_Net:** +133,116 | **OI:** 409,899 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-09-08 | **MM_Net:** +134,972 | **OI:** 411,227 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-09-01 | **MM_Net:** +136,771 | **OI:** 415,196 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-08-25 | **MM_Net:** +144,747 | **OI:** 427,957 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-08-18 | **MM_Net:** +141,648 | **OI:** 406,260 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-08-11 | **MM_Net:** +137,662 | **OI:** 400,309 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-08-04 | **MM_Net:** +130,766 | **OI:** 371,551 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-07-28 | **MM_Net:** +119,795 | **OI:** 384,603 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-07-21 | **MM_Net:** +124,831 | **OI:** 383,368 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-07-14 | **MM_Net:** +120,779 | **OI:** 383,689 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-07-07 | **MM_Net:** +116,161 | **OI:** 371,776 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-06-23 | **MM_Net:** +115,395 | **OI:** 352,167 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-06-16 | **MM_Net:** *not retrieved* | **OI:** *n/a* | **Sentiment:** qualitative: 14-week high (speculators boosted bets 3rd straight week)  
> **Report_Date:** 2026-06-09 | **MM_Net:** +105,863 | **OI:** 332,709 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-06-02 | **MM_Net:** +112,179 | **OI:** 326,052 | **Sentiment:** Neutral zone  
> **Report_Date:** 2026-05-19 | **MM_Net:** +93,540 | **OI:** 379,325 | **Sentiment:** Neutral zone

## Related pages

- [[central-bank-gold-demand]]
- [[gold-geopolitical-risk-premium]]
- [[goldman-sachs-gold-forecast]]
- [[global-cb-activity-log]]
