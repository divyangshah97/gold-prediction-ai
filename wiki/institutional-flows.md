# Institutional & Hedge Fund Gold Flows

**Summary**: Tracks daily GLD ETF tonnage changes (institutional demand proxy) and weekly CFTC COT Managed Money positioning (hedge fund futures sentiment) to assess non-central-bank gold demand. **July 29 update**: Global gold ETFs saw **$8.9bn of outflows in June** (though H1 2026 overall remained net positive at $8bn); AUM fell 6% in H1 to $526bn on lower gold prices even as collective holdings rose 18t to 4,047t. CFTC: COMEX managed-money net longs **jumped 16% m/m in June to 538t** — the highest month-end position since January 2026 — rising even as the gold price weakened, a notable divergence. Note: this page's Factor 6 description below (GLD/CFTC-based) is superseded — Factor 6 in the live signal methodology is now "Dollar Pressure" (DXY + USD/INR), not ETF/CFTC flows; see [[signal-methodology]].

**Sources**: SPDR GLD ETF (State Street), CFTC Commitment of Traders report (weekly, disaggregated futures), https://www.gold.org/goldhub/research/gold-etfs-holdings-and-flows/2026/07, https://en.macromicro.me/series/8308/gold-futures-and-options-manage-money-net-position, https://www.etfchannel.com/article/202607/spdr-gold-shares-gld-sees-notable-etf-inflows-as-investors-add-gold-exposure-GLD07162026inflow.htm/

**August 3 note**: As of July 30, 2026, GLD 5-day net flows were **+$189.64M**, 1-month net flows **+$581.24M**, but 3-month net flows remained **−$4.25B** — near-term inflows resuming after a sharply negative Q3-to-date. No August-dated GLD tonnage or fresh weekly CFTC COT print (next due Friday) found today; this factor is informational only (superseded by Factor 6 Dollar Pressure in the live signal, see [[signal-methodology]]).

**Last updated**: 2026-08-03

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

> **Report_Date (as-of Tuesday):** 2026-07-28  
> **Published by CFTC:** 2026-08-01 (Friday)  
> **Retrieved:** 2026-07-31T21:37:12Z via GitHub Action (fetch_cot.yml) — CFTC direct disaggregated futures  
> **cot.csv:** Updated 2026-08-01 (Saturday routine)

| Field | Value |
|---|---|
| Report_Date | 2026-07-28 |
| Open_Interest | 384,603 contracts |
| MM_Long | 135,093 contracts |
| MM_Short | 15,298 contracts |
| MM_Net | +119,795 contracts |
| MM_Net_Change | −5,036 vs. prior week (2026-07-21: +124,831) |
| MM_Net % of OI | 31.1% |
| **Sentiment** | **Neutral zone (50,000–150,000)** |

### Sentiment Interpretation (as of July 28)

MM_Net of +119,795 falls in the **Neutral zone (50,000–150,000 contracts)**. After six consecutive weeks of increases, managed money net longs pulled back modestly by −5,036 contracts — the first week-over-week decline since May 19. This is a mild reversal, not a trend break: at +119,795, the net position remains well above historically bearish extremes (<50,000) and well below crowded-long territory (>250,000).

Open interest ticked slightly higher to 384,603 from the prior week's 383,368 — essentially flat, suggesting the pullback was driven by gross long reduction (135,093 vs. 141,487 prior week) rather than a surge in new shorts. Gross shorts continued to decline (15,298 vs. 16,656 prior week), partially offsetting the long reduction. The overall picture is one of modest profit-taking on longs after a multi-week grind higher, with shorts continuing to cover.

**Week-over-week change:** −5,036 contracts — well below the ±20,000 significant positioning shift threshold. No extreme move flagged. The slight pull-back in net longs coincides with FOMC week (hawkish Warsh press conference, multi-decade yield highs) and Iran-escalation-driven USD strength — consistent with de-risking rather than a conviction-shift against gold.

---

## Historical COT Reference

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
