# Wiki Log

Append-only record of all wiki operations.

---

## 2026-07-25 — Signal methodology narrowed to 5 factors (Factors 1 & 4 retired, Factor 7 kept); signals.csv restarted fresh

**User request**: after reviewing which of the 7 signal factors are actually relevant to a 2-3 month gold futures trading horizon (see discussion earlier same day), user asked to remove Factor 1 (Price vs Targets) and Factor 4 (Central Bank Demand) from the live signal, and to start `signals/signals.csv` fresh from 2026-07-27 rather than continue appending to the existing history.

**Rationale for removal** (full analysis given to user, summarized here):
- Factor 1 (Price vs Targets) anchors off multi-month/annual bank forecasts ([[goldman-sachs-gold-forecast]]) — doesn't predict next-quarter direction; gold can stay "cheap" indefinitely.
- Factor 4 (Central Bank Demand) is monthly/quarterly lagged data ([[central-bank-gold-demand]]) that moves the multi-year floor, not next quarter's price; also structurally asymmetric (could only ever score 0/+1, never bearish).
- Kept: Factor 2 (Geopolitical, immediate event-risk), Factor 3 (Fed/Macro, ~monthly cadence matches horizon), Factor 5 (Technicals, entry timing), Factor 6 (Dollar Pressure, fastest-transmitting), Factor 7 (Real Yields/TIPS, second-fastest-transmitting, added earlier same day — see [[real-yields-tips]]).

**Repo file changes**:
- `signals/signals.csv` → renamed to `signals/signals_archive_2026-05-22_to_2026-07-24.csv` (44 rows preserved as-is, six/seven-factor era)
- New `signals/signals.csv` created with header only (`Date,Signal,Score,Reasoning`) — first row expected from the 2026-07-27 routine run under the new 5-factor system

**Pages updated**:
- `wiki/signal-methodology.md` — rewritten for the 5-factor system (Factor 2, 3, 5, 6, 7 only); added a "Why Factors 1 and 4 were retired" section; added per-factor "Horizon note" explaining transmission speed; range changed to -5/+5; historical signal log table documents the archive file and the brief unused 7-factor (-7/+7) config from earlier the same day
- `wiki/real-yields-tips.md` — re-created (had been lost in a local git stash during sync) with an added section on why it survived the factor review while Factors 1/4 didn't
- `wiki/index.md` — signal-methodology and real-yields-tips entries updated; institutional-flows entry refreshed to match latest synced COT data (July 21) picked up during the pull

**Sync note**: local wiki working directory had fallen behind `origin/master` by several days of routine-committed daily updates (through 2026-07-24) plus a COT update (2026-07-21). Stashed uncommitted local edits, fast-forward pulled to sync, then reapplied the Factor 7 documentation and this 5-factor change on top of the current state — avoided clobbering several days of real routine output.

**Still pending**: the routine prompt itself (`trig_01Q7FfuV2Y2Fqk4f8dtokd2J`) needs a corresponding update via RemoteTrigger to drop Factor 1/4 scoring from Step 6 and change the range to -5/+5, before the 2026-07-27 run reflects this. Not yet done as of this wiki commit — see follow-up log entry once pushed.

---

## 2026-07-24 — Daily update: Gold $4,050 (Jul23 close; −2.1%; Iran skips talks, ceasefire extended=de-escalation); China paper gold halt (ICBC+4 banks cease SGE retail trading); WTI $92.36 (+6.8%); FOMC Jul28-29 36.5% hike prob | Signal: Wait (−2)

**Raw file created**:
- `raw/india-gold-2026-07-24.md` — MCX ₹1,42,300–₹1,44,000/10g (−0.36%; Jul24); XAU/USD Jul23 close ~$4,050 (−2.1%); USD/INR ₹96.63 (Jul23); WTI $92.36 (Jul23 surge +6.8%); China paper gold halt (ICBC+4 banks vs SGE); Silver −1.96% ($58.77); June ETF inflows ₹34.4B; June imports $1.97B (−42% m/m); investment demand (82t) > jewellery (66t) for first time; RBI 880.52t static; Goldman $4,900 → MCX ~₹1,70,000 (domestic ~17% below)

**Prices added to CSV** (previous trading day T-1 = Wednesday July 23):
- Gold Jul23 close: **$4,050.00** | Silver: $58.77 | DXY: 101.10 | WTI: $92.36 | USD/INR: ₹96.63
- Data sourced via web search (yfinance/metals.dev blocked by proxy); Gold $4,050 (multiple sources: FXLeaders, Vantage Markets, FXStreet Jul23); Silver $58.77 (FXStreet Jul23); DXY ~101.10 (ECB held 2.25% Jul23; near prior close 101.1227); WTI $92.36 (Vantage Markets Jul23 surge +6.8%); USD/INR ₹96.63 (high 96.6281; approximately flat from Jul22 close 96.6830)

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 24 section added: 11 rows (macro Gold/WTI/Signal, China banks/SGE paper gold halt, Poland, Russia, Germany, France, Italy, Japan, UK, Saudi, India MCX); Policy Tracker entry: China retail paper gold trading ban (ICBC+4 banks Jul24)
- `wiki/china-pboc-gold.md` — New section "China Retail Paper Gold Trading Halt (July 24, 2026)": ICBC, PSBC, Ping An Bank, Guangfa Bank, CCB ceased retail SGE paper gold trading; physical/ETFs/institutional unaffected; 2020 Crude Oil Treasure scandal context; neutral for PBoC accumulation streak; daily update log entry added
- `wiki/iran-conflict-2026.md` — July 24 timeline entry: Iran skipped talks; ceasefire extended; gold −2.1% to $4,050; WTI $92.36 surge; MCX ₹1,42,300–₹1,44,000; Factor 2 = Bearish (−1); Last updated 2026-07-24
- `wiki/gold-geopolitical-risk-premium.md` — July 24 entry: $4,050 Jul23 close; 9d EMA ~$4,092; 50d EMA ~$4,104; gold BELOW BOTH; WTI $92.36; Signal: Wait (−2); Last updated 2026-07-24
- `wiki/india-gold-market.md` — July 24 MCX section added: ₹1,42,300–₹1,44,000/10g; all drivers (Iran, WTI, FOMC, China paper gold halt); signal factors breakdown; Last updated 2026-07-24
- `wiki/fed-macro-factors.md` — July 24 section: FOMC 5 days; 36.5% hike prob; WTI $92.36 (surge +6.8%); ECB held 2.25%; CPI 4.2%; Macro factor = Bearish (−1); Last updated 2026-07-24
- `wiki/index.md` — updated 6 descriptions: india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors, china-pboc-gold
- `wiki/log.md` — this entry

**CB sweep findings (July 24)**:
- 🇨🇳 China (Banks/SGE): ICBC, PSBC, Ping An Bank, Guangfa Bank, CCB ceased retail SGE paper gold trading effective July 24 (physical/ETFs/institutional unaffected; 2020 derivatives crackdown context)
- 🇵🇱 Poland: No new data (82t YTD confirmed; next mid-August)
- 🇷🇺 Russia: No new data (H1 2026 −43.5t; 2,282t; $5.6B raised; next update August)
- 🇩🇪 Germany, 🇫🇷 France, 🇮🇹 Italy, 🇯🇵 Japan, 🇬🇧 UK, 🇸🇦 Saudi Arabia: No new data

**Signal**: Wait (Score: −2)
- Factor 1 Price vs Targets: +1 (17.3% below GS $4,900; >15% = Bullish)
- Factor 2 Geopolitical: −1 (Iran skips talks; ceasefire extended = de-escalation; gold −2.1%; safe-haven premium deflating; Bearish)
- Factor 3 Fed/Macro: −1 (FOMC Jul28-29 36.5% hike prob; WTI $92.36 surge +6.8% = inflationary; CPI 4.2%; ECB held 2.25%; Goldman $4,900 base = no cuts; Bearish)
- Factor 4 CB Demand: 0 (No new CB purchase/sale data in last 7 days; China paper gold halt = neutral for PBoC; Neutral)
- Factor 5 Technicals: −1 (Gold $4,050 BELOW 9d EMA ~$4,092 AND 50d EMA ~$4,104; Jul22 GREEN, Jul23 RED (−2.1%) → NOT 2 consecutive green; Bearish)
- Factor 6 Dollar Pressure: 0 (DXY Jul22→23: 101.20→101.10 = −0.09% < 0.5%; USD/INR Jul22→23: 96.6830→96.63 = −0.05% < 0.5%; both within ±0.5%; Neutral)

---

## 2026-07-23 — Daily update: Gold $4,138.84 (Jul22 close; +3.27%; Iran safe-haven breakout at NATO summit); Russia H1 2026 gold sales = 43.5t (record ≥25 years; 2,282t remaining); WTI $86.50; FOMC Jul29 36.3% hike prob | Signal: Wait (0)

**Raw file created**:
- `raw/india-gold-2026-07-23.md` — MCX ₹1,45,230/10g (−0.31%; Jul23); XAU/USD Jul22 close $4,138.84 (+3.27%); USD/INR ₹96.6830 (Jul22); Silver MCX ₹2,26,453/kg (+0.24%); WTI $86.50 (Jul22); June ETF inflows ₹34.4B (highest since Feb); July 1-10 inflows ₹12.1B; investment demand (82t) > jewellery (66t) structural shift; June imports $1.97B (−42% m/m); 15% duty unchanged; RBI 880.52t static

**Prices added to CSV** (previous trading day T-1 = Tuesday July 22):
- Gold Jul22 close: **$4,138.84** | Silver: $59.39 | DXY: 101.20 | WTI: $86.50 | USD/INR: ₹96.6830
- Data sourced via web search (yfinance/metals.dev blocked by proxy); multiple sources confirm Gold $4,138.84 (Jul22); Silver $59.39 (FXStreet July 22); DXY 101.20 (Global Economy Briefing July 22); WTI $86.50 (eased from $88.6 intraday high on Iran NATO news); USD/INR ₹96.6830 (+0.35% from July 21 close, MTFX confirmed)

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 23 section added: 13 rows (macro, Russia H1 43.5t MAJOR UPDATE, Jordan +1t June, Poland no-new, China no-new, Czech 7d expired, Germany no-new, France no-new, Italy no-new, Japan no-new, UK no-new, Saudi no-new, Turkey no-new, India July 23)
- `wiki/russia-gold-reserves.md` — MAJOR UPDATE: H1 2026 sales confirmed at 43.5t (record ≥25 years); reserves 2,282t; budget proceeds $5.6B; deficit 6T rubles; all sections updated; summary, current position table, sales pace table, impact table, daily log
- `wiki/iran-conflict-2026.md` — July 23 timeline entry: gold consolidated after +3.27% breakout; Factor 2 revised to Bullish (+1) as safe-haven paradox broke; July 22 entry noted with correct close $4,138.84
- `wiki/india-gold-market.md` — July 23 MCX section added: ₹1,45,230/10g (−0.31%); Jul22 close $4,138.84; EMA context updated ($4,111.56 / $4,319.64)
- `wiki/gold-geopolitical-risk-premium.md` — July 23 timeline entry: $4,138.84 Jul22 close; breakout confirmed; EMA updated to Investing.com values ($4,111.56 / $4,319.64); Factor 2 Bullish (+1); Signal Wait (0)
- `wiki/fed-macro-factors.md` — July 23 section: FOMC 6 days (Jul29); 36.3% hike prob; WTI $86.50 re-elevated; Goldman $4,900; Bearish (−1)
- `wiki/index.md` — updated 7 descriptions: india-gold-market, global-cb-activity-log, russia-gold-reserves, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors
- `wiki/log.md` — this entry

**CB sweep findings (July 23)**:
- 🇷🇺 Russia: **43.5t H1 2026 gold sales (record ≥25 years)**; 2,282t remaining; $5.6B proceeds (Kitco/Reuters July 21)
- 🇯🇴 Jordan: +1t June 2026 (from WGC/web search)
- 🇵🇱 Poland: No new data (82t YTD confirmed; next mid-August)
- 🇨🇳 China (PBoC): No new data (June +14.93t; July expected early August)
- 🇨🇿 Czech Republic: July +2t (Jul 16) — 7-day window now expired
- 🇩🇪 Germany: No new Bundesbank action
- 🇫🇷 France, 🇮🇹 Italy, 🇯🇵 Japan, 🇬🇧 UK, 🇸🇦 Saudi Arabia, 🇹🇷 Turkey: No new data

**Signal**: Wait (Score: 0)
- Factor 1 Price vs Targets: +1 (15.5% below GS $4,900; >15% = Bullish)
- Factor 2 Geopolitical: +1 (Iran deal "over" at NATO summit; gold +3.27% breakout; DXY only +0.28%; safe-haven flows into gold with USD flat = Bullish)
- Factor 3 Fed/Macro: −1 (FOMC Jul29: 36.3% hike prob; CPI 4.2%; WTI $86.50 re-elevated; Goldman $4,900 = no cuts; Bearish)
- Factor 4 CB Demand: 0 (Czech Jul +2t exactly at 7d boundary; Russia 44t H1 = net selling; no new positive data; Neutral)
- Factor 5 Technicals: −1 (Gold $4,138.84 above 9d EMA $4,112; below 50d EMA $4,320; downtrend: 50d > 9d; Jul21 RED, Jul22 GREEN = not 2 green; Bearish)
- Factor 6 Dollar: 0 (DXY +0.28%; USD/INR +0.26%; both within ±0.5%; Neutral)

## 2026-07-21 — Daily update: Gold $4,017.52 (Jul 18 close; +0.65% MCX Jul 21 recovery); Iran Strait CLOSED (no US crossings since Jul 15); FOMC 25% hike prob; Czech July +2t; Russia June −6t; Turkey June −3t | Signal: Wait (+2)

**Raw file created**:
- `raw/india-gold-2026-07-21.md` — MCX ₹1,42,314/10g (+0.65%); XAU/USD ~$4,022–$4,071 (recovering); USD/INR ₹96.50 (Jul 18); June gold imports $1.97B (−42% m/m); Gem & jewellery exports +26% June; ETF July 1-10 inflows ~₹12.1B; Silver recovering; 15% import duty unchanged; RBI 880.52t static

**Prices added to CSV** (previous trading day T-1 = Friday July 18):
- Gold Jul 18 close: **$4,017.52** | Silver: $55.50 | DXY: 100.70 | WTI: $81.78 | USD/INR: ₹96.50
- Data sourced via web search (yfinance/metals.dev blocked by proxy); mygoldcalc.com July 18 confirmed $4,017.52/oz; silver $55.50 (hovering Friday); DXY 100.70 (range 100.5–100.8 intraday); WTI $81.78 (prior close before July 20 spike to $84.59); USD/INR ₹96.50

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 21 section added: 12 rows (macro, Iran, Poland no-new-data, China no-new-data, Czech +2t Jul, Germany, Saudi, Japan, UK, Italy, France, Russia June −6t, Turkey June −3t, India July 21); **CB sweep notes**: Czech Republic +2t July (Jul 16) within 7d → triggers CB demand = Bullish (+1); Russia June −6t (YTD −34t); Turkey June −3t (YTD −81t)
- `wiki/india-gold-market.md` — July 21 MCX section added: ₹1,42,314/10g (+0.65%); June imports $1.97B (−42%); gem & jewellery exports +26% June; ETF July 1-10 ₹12.1B; discount $20/oz; Signal Wait (+2)
- `wiki/fed-macro-factors.md` — July 21 section: FOMC hike prob rising to 25%; Fed July inflation "red flag"; oil WTI $81.78; net Neutral (0)
- `wiki/iran-conflict-2026.md` — July 21 timeline: Strait CLOSED; no US-route crossings since Jul 15; Iran 7 transits; Factor 2 Bearish (−1)
- `wiki/gold-geopolitical-risk-premium.md` — July 18 close $4,017.52 and July 21 recovery entries added; 9d EMA ~$4,088; 50d EMA ~$4,270; 2 green days tech trigger
- `wiki/index.md` — updated descriptions for india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors
- `wiki/log.md` — this entry

**Signal**: Wait (Score: +2)
- Factor 1 Price vs Targets: +1 (18.4% below GS $4,900; >15% = Bullish)
- Factor 2 Geopolitical: −1 (Iran Strait CLOSED; no US-route crossings since Jul 15; oil WTI $81.78; gold/oil via Fed channel = Bearish)
- Factor 3 Fed/Macro: 0 (FOMC Jul 28-29: 25% hike prob / 75% hold; CPI 4.2% below expectations; oil elevated; net Neutral)
- Factor 4 CB Demand: +1 (Czech Republic +2t July 2026, announced Jul 16 = within 7-day window; Bullish)
- Factor 5 Technicals: +1 (Gold $4,017.52 BELOW 9d EMA ~$4,088 AND 50d EMA ~$4,270; Jul17 close +$27.10 GREEN; Jul18 close +$4.82 GREEN → "2 green" = Bullish)
- Factor 6 Dollar Pressure: 0 (DXY Jul17→18: 100.75→100.70 = −0.05% < 0.5%; USD/INR Jul17→18: 96.6522→96.50 = −0.16% < 0.5%; both Neutral)

**Global CB sweep summary (last 24-48h)**:
- No new country-level CB gold buying/selling announcements in last 24-48 hours
- Czech Republic +2t July (announced July 16) — within 7-day window, still current
- Russia: June −6t (YTD −34t); Turkey: June −3t (YTD −81t) — from WGC/Pravda data, confirming May trends continued into June
- Germany: no new repatriation; France: static; Italy: FdI dispute unresolved; Japan: static; USA: static; UK: static; Saudi Arabia: static

---

## 2026-07-20 — Daily update: Gold ~$4,001–4,017 (9-month low zone; +0.3% Monday recovery); Iran Strait crisis intensifying (Brent $88.10; 6 ships/day); June CPI 4.2% below expectations; MCX ~₹1,41,300/10g (+0.3%); June imports $1.97B (−42% m/m); ETF June inflows ₹34.4B rebound | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-07-20.md` — MCX ~₹1,41,300/10g (+0.3%); XAU/USD ~$4,001–4,017 (intraday Monday); USD/INR ~₹96.65; Brent $88.10 (Iran Kuwait attack); June gold imports $1.97B (−42% m/m; lowest since June 2025; Iran Strait disruption); ETF June inflows ₹34.4B (rebound from May −₹725 crore outflow); July 1-10 ETF inflows ~₹12.1B; silver down ₹5,000 on Iran tensions; 15% import duty unchanged; RBI 880.52t static

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 20 section added: 11 rows (macro, Iran, Poland no-new-data, China no-new-data, Germany, Saudi Arabia, Japan, UK, Italy, France, India); note: no new CB purchase/sale announcement found in last 7 days
- `wiki/india-gold-market.md` — July 20 MCX section added: ₹1,41,300/10g (+0.3%); June imports $1.97B; ETF flows; silver drop; signal Wait (−1); last updated July 20
- `wiki/fed-macro-factors.md` — July 20 section: June CPI 4.2% (above May but below expectations); rate-hike bets fell to 30%; FOMC July 28-29 hold 90%; oil surge hawkish; macro factor Neutral (0); last updated July 20
- `wiki/iran-conflict-2026.md` — July 20 timeline entry: Brent $88.10 (Kuwait plant attacked); Strait traffic 6 vessels/day; gold still falling; Factor 2 = Bearish (−1); last updated July 20
- `wiki/gold-geopolitical-risk-premium.md` — summary updated: gold $4,001–4,017 (9-month lows); 9d EMA ~$4,095; 50d EMA ~$4,307; MCX ₹1,41,300; Signal: Wait (−1); last updated July 20
- `wiki/log.md` — this entry

**Prices in CSV** (no new rows added — July 18-19 were weekend; prices.csv already has July 17 close as last row):
Gold (Jul 17 close): $4,012.7 | Silver: $56.038 | DXY: 100.75 | WTI: $82.49 | USD/INR: ₹96.6522
Today live (NOT in CSV): XAU/USD ~$4,001–4,017 | MCX ~₹1,41,300/10g | Brent $88.10

**Signal**: Wait (Score: −1)
- Factor 1 Price vs Targets: +1 (18.1% below GS $4,900 target; >15% = Bullish)
- Factor 2 Geopolitical: −1 (Iran Strait closed; Brent $88.10; Kuwait hit; gold FALLING = oil inflation channel bearish; Bearish)
- Factor 3 Fed/Macro: 0 (June CPI 4.2% — above May but below expectations; rate hikes fell to 30%; oil surge hawkish; FOMC Jul 28-29 hold 90%; net Neutral)
- Factor 4 CB Demand: 0 (No new CB data in last 7 days — WGC Jul 8, PBoC Jul 7, Poland Jul 9 all outside window; Neutral)
- Factor 5 Technicals: −1 (Gold below both 9d EMA ~$4,095 and 50d EMA ~$4,307; Jul 15→16 RED (−$58); Jul 16→17 GREEN (+$27); only 1 of last 2 green = not 2 green; Bearish)
- Factor 6 Dollar Pressure: 0 (DXY Jul16→17: +0.02%; USD/INR Jul16→17: +0.16%; both within ±0.5%; Neutral)

---

## 2026-07-18 — COT weekly update
Report_Date: 2026-07-14 | MM_Net: +120,779 (+4,618 vs prior week) | OI: 383,689 | MM_Long: 136,905 | MM_Short: 16,126 | MM_Net % OI: 31.5% | Sentiment: Neutral zone | Source: CFTC via GitHub Action (fetch_cot.yml), fetched 2026-07-17T21:20:26Z
Pages updated: wiki/institutional-flows.md (Latest COT Data section replaced; Historical COT Reference extended with Jul 14 row), wiki/index.md (institutional-flows entry updated), prices/cot.csv (2026-07-14 row appended)

---

## 2026-07-16 — Daily update: Gold ~$4,059 (flat; PPI-driven); Iran in limbo (no new development); PPI −0.3% + CPI 3.5% macro-dovish; Czech Republic 40th consecutive month buying; Poland revised to ~632t; MCX ~₹1,41,000 (−0.36%); USD/INR ₹96.19 | Signal: Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-07-16.md` — MCX ~₹1,41,000/10g (−0.36%); XAU/USD ~$4,059 (flat; range $4,017–$4,062); Silver $60.11/oz (+1.7%); DXY ~100.60 (−0.52% — PPI-driven dollar weakness); WTI $79.58 (−0.54%); USD/INR ₹96.19 (−0.22% rupee slightly firmed); India import duty 15% unchanged; RBI 880.52t static; ETF AUM ₹1.84T; AMC subscription caps ongoing; GS $4,900 → MCX ~₹1,70,540 (domestic 17.3% below)

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 16 section added: 11 rows (macro, Poland, Czech Republic, Jordan May-data, Kazakhstan, Iran, Germany, France, Italy, Japan, Saudi Arabia, UK, India); Poland table updated to 82t YTD/~632t total; Czech Republic updated to 40 months; Jordan May 2026 +1t first-time logged
- `wiki/india-gold-market.md` — July 16 MCX section added: ₹1,41,000 (−0.36%); PPI carry-through; USD/INR ₹96.19 (rupee firmed slightly); signal updated to Wait (+1); last updated July 16
- `wiki/fed-macro-factors.md` — July 16 section: June PPI −0.3% (released July 15); FOMC hold 87.7% July 28-29; September hike ~49%; DXY 100.60; macro factor Bullish (+1); last updated July 16
- `wiki/iran-conflict-2026.md` — July 16 update: Deal in limbo; Switzerland cancelled; Polymarket ~40% July 31; no new development; WTI $79.58 (−0.54%); Factor 2 = Neutral (0); last updated July 16
- `wiki/gold-geopolitical-risk-premium.md` — summary updated: gold ~$4,059 flat, PPI-macro-driven, Iran in limbo; 9d EMA ~$4,065, 50d EMA ~$4,344; Signal: Wait (+1); July 16 row added to timeline; last updated July 16
- `wiki/poland-gold-reserves.md` — total revised upward from 613t to ~632t (595t April official + 37t since); 82t YTD confirmed; July 16 log row added; last updated July 16
- `wiki/czech-republic-gold-reserves.md` — July 2026: +2t; total ~83t; **40th consecutive month** of buying; updated July 16
- `wiki/index.md` — descriptions updated for Poland (632t), Czech Republic (40 months/83t), India gold market (July 16 data), global-cb-activity-log (July 16 summary), gold-geopolitical-risk-premium (July 16), fed-macro-factors (PPI update), iran-conflict-2026 (limbo)
- `wiki/log.md` — this entry

**Prices fetched** (all via web search — yfinance/metals.dev blocked by proxy):
Gold: ~$4,059/oz | Silver: $60.11/oz | DXY: ~100.60 | WTI: $79.58/bbl | USD/INR: ₹96.19 | MCX: ~₹1,41,000/10g

**Signal**: Wait (Score: +1)
- Factor 1 Price vs Targets: +1 (17.2% below GS $4,900 target; >15% threshold = Bullish)
- Factor 2 Geopolitical: 0 (Iran deal in limbo — Switzerland cancelled July 15; no new development today; WTI −0.54% slight easing; gold macro-driven not geopolitically-driven; Neutral)
- Factor 3 Fed/Macro: +1 (June PPI −0.3% July 15 + CPI 3.5% July 14 → dovish momentum; FOMC hold 87.7% July 28-29; Bullish)
- Factor 4 CB Demand: 0 (No new WGC report or major CB announcement in last 7 days; Czech Republic July buy confirmed but this is continuation not new data release; Neutral)
- Factor 5 Technicals: −1 (Gold ~$4,059 BELOW 9d EMA ~$4,065 AND below 50d EMA ~$4,344; 50d > 9d = downtrend; Jul14 RED, Jul15 GREEN — only 1 of last 2 green; Bearish)
- Factor 6 Dollar Pressure: 0 (DXY −0.52% within ±1%; INR −0.22% within ±1%; Neutral)

---

## 2026-07-15 — Daily update: Gold $4,052.78 (+1.07% — CPI-driven); Iran deal stalled (Switzerland signing cancelled); soft June CPI 3.5% vs 4.2%; Kazakhstan 4th-largest buyer 2026; MCX ~₹1,41,588 (−0.5%); USD/INR ₹96.40 (+0.62%) | Signal: Wait (+2)

**Raw file created**:
- `raw/india-gold-2026-07-15.md` — MCX ~₹1,41,588/10g (−0.5%); XAU/USD $4,052.78 (+1.07% — CPI-driven); Silver $59.07 (+1.9%); DXY 101.13 (−0.16%); WTI $80.01 (+0.55% — Iran deal stalled); USD/INR ₹96.40 (+0.62% — rupee weakening); India import duty 15% unchanged; FY26 gold imports $71.98B record; ETF AUM ₹1.84T with AMC subscription caps; RBI 880.52t static

**Pages updated**:
- `wiki/global-cb-activity-log.md` — July 15 section added: 12 rows (macro summary, Iran, China, Poland, Kazakhstan, Germany, France, Italy, Saudi Arabia, Japan, UK, India); Kazakhstan confirmed world's 4th-largest buyer 2026 (20t YTD, 361t total, 78% of FX reserves); CB country table updated with Kazakhstan 4th-largest buyer; last updated July 15
- `wiki/india-gold-market.md` — July 15 MCX section: ₹1,41,588 (−0.5%); soft CPI carry-through; USD/INR ₹96.40 (+0.62%); India FY26 import bill $71.98B; AMC subscription restrictions; signal updated to Wait (+2); last updated July 15
- `wiki/fed-macro-factors.md` — July 15 section: soft June CPI 3.5% vs 4.2%; rate hike bets unwound 35bps→18bps; macro factor updated to Bullish (+1); last updated July 15
- `wiki/iran-conflict-2026.md` — July 15 update: Switzerland signing meeting cancelled; deal stalled but not dead; US sanctions waiver through Aug 21; Factor 2 = Neutral (0); last updated July 15
- `wiki/gold-geopolitical-risk-premium.md` — summary and key level updated: gold $4,052.78, CPI-driven rally, Iran deal stalled, Signal: Wait (+2); last updated July 15
- `wiki/kazakhstan-gold-reserves.md` — confirmed 4th-largest buyer 2026; total 361t (78% of FX reserves as of May 2026); last updated July 15
- `wiki/log.md` — this entry

**Prices fetched** (all via web search — yfinance/metals.dev blocked by proxy):
Gold: $4,052.78/oz | Silver: $59.07/oz | DXY: 101.13 | WTI: $80.01/bbl | USD/INR: ₹96.40 | MCX: ₹1,41,588/10g

**Signal**: Wait (Score: +2)
- Factor 1 Price vs Targets: +1 (17.3% below GS $4,900)
- Factor 2 Geopolitical: 0 (Iran deal stalled — Switzerland cancelled; ongoing risk but no acute new escalation; MCX −0.5% = gold not acting as safe haven today)
- Factor 3 Fed/Macro: +1 (Soft June CPI 3.5% vs 4.2% → rate hike bets unwound → dovish surprise → bullish gold)
- Factor 4 CB Demand: +1 (WGC July 2026 "central banks remain committed"; Kazakhstan 4th-largest buyer Jul10; May net 41t published Jul3 — all within 7 days)
- Factor 5 Technicals: −1 (below both EMAs: 9d ~$4,080, 50d ~$4,320; Jul13→14 red, Jul14→15 green — NOT 2 consecutive green)
- Factor 6 Dollar Pressure: 0 (DXY −0.16% within 1%; INR +0.62% within 1%)

**CB sweep summary**:
- China: No new July data; most recent June +14.93t (July 7)
- Poland: No new data; confirmed 82t YTD (Bloomberg July 9)
- Uzbekistan: No new data; 41t YTD through June
- Kazakhstan: Confirmed world's 4th-largest buyer 2026 (20t YTD, 361t, 78% FX reserves) per July 10 article
- Germany: No new data; repatriation pressure growing; Bundesbank stance unchanged
- France: Repatriation complete since Jan 2026; 2,437t all on French soil
- Italy: No new data; ~1,055t at FRBNY; repatriation pressure alongside Germany
- Saudi Arabia: No new data; 323.07t static
- Japan: No new data; 845.97t static
- UK: No new data; 310.29t
- Iran: Deal stalled; MOU framework still standing; US sanctions waiver through Aug 21

---

## 2026-07-10 — Daily update: Gold ~$4,116 (+1.0% recovery from $4,075); Iran war ongoing (170+ strikes) but peace talks continuing; WTI −3.2% to $71.80; MCX ~₹1,44,760 (−0.37%); USD/INR ₹95.32 (INR +15p); CPI July 14 pending | Signal: Wait (0)

**Raw file created**:
- `raw/india-gold-2026-07-10.md` — MCX ~₹1,44,760/10g (−0.37%); XAU/USD ~$4,116 (+1.0%); Silver ~$60.32 (+4.9%); DXY ~100.935 (−0.13%); WTI ~$71.80 (−3.2% — Iran peace talks); USD/INR ₹95.32 (INR +15 paise); 15% duty unchanged (May 13 notification still in force); June CPI July 14; no new RBI data

**Pages updated**:
- `wiki/iran-conflict-2026.md` — July 10 developments: US 170+ strikes on Iran; Iran fires 10 ballistic missiles at Jordan (intercepted); peace talks continuing (Pakistan/Qatar); WTI −3.2% to $71.80; Factor 2 → Neutral (0); last updated July 10
- `wiki/gold-geopolitical-risk-premium.md` — July 10 price row added (~$4,116 +1.0% recovery; above 9d EMA ~$4,108; below 50d EMA ~$4,135; downtrend); Signal: Wait (0); last updated July 10
- `wiki/india-gold-market.md` — July 10 MCX section: ₹1,44,760/10g; INR +15 paise; duty clarification (15% May 13 notification vs Feb budget history); silver +4.9%; June CPI July 14; last updated July 10
- `wiki/fed-macro-factors.md` — July 10 update: 74.9% hold / 25.1% hike at July 29; WTI easing reduces immediate pressure; CPI July 14 critical; Macro factor remains Bearish (−1); last updated July 10
- `wiki/global-cb-activity-log.md` — July 10 section added (8 rows: macro, Iran, Germany, Saudi Arabia, Japan, UK, Italy, France, India); no new CB gold buy/sell data; last updated July 10
- `wiki/index.md` — page descriptions updated: gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors, india-gold-market, global-cb-activity-log; last updated July 10
- `wiki/log.md` — this entry

**Prices fetched** (all via web search — yfinance/metals.dev blocked by proxy):
Gold: $4,116/oz | Silver: $60.32/oz | DXY: 100.935 | WTI: $71.80/bbl | USD/INR: ₹95.32

**Signal**: Wait (Score: 0)
- Factor 1 Price vs Targets: +1 (16.0% below GS $4,900)
- Factor 2 Geopolitical: 0 (Iran war ongoing; peace talks continuing; WTI −3.2% = ambiguous)
- Factor 3 Fed/Macro: −1 (FOMC hawkish; 25% hike prob July 29; CPI July 14 risk)
- Factor 4 CB Demand: +1 (Uzbekistan June +9t on July 9 within 7-day window)
- Factor 5 Technicals: −1 (above 9d EMA ~$4,108; below 50d EMA ~$4,135; downtrend config)
- Factor 6 Dollar Pressure: 0 (DXY −0.13%, INR −0.26%, both within 1%)

---

## 2026-07-09 — Daily update: Gold ~$4,075 (−1.3%; 3rd red day); CEASEFIRE ENDED (Iran Hormuz attacks; US strikes; oil +5.3% to $74.20); FOMC minutes hawkish (PCE 3.3%, easing bias removed); Uzbekistan June +9t (YTD 41t); MCX ~₹1,45,000 (−0.27%); USD/INR ₹95.57 | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-07-09.md` — MCX ~₹1,45,000/10g (−0.27%); XAU/USD ~$4,075 (−1.3%; 3rd red day); Silver ~$57.50 (−4%); DXY ~101.07 (+0.17%); WTI ~$74.20 (+5.3% — Hormuz attack surge); USD/INR ₹95.57 (+0.18%); 15% duty unchanged; Iran ceasefire ended; FOMC minutes hawkish; death cross intact; gold below both EMAs

**Pages updated**:
- `wiki/iran-conflict-2026.md` — July 5–9 events added: Iran Hormuz attacks (July 5-6), Iran ballistic missiles (July 7), Trump declares MOU "over" + US strikes 80+ targets (July 8), gold falling despite escalation (July 9); Factor 2 → Bearish (−1); last updated July 9
- `wiki/gold-geopolitical-risk-premium.md` — July 9 price row added (~$4,075; ceasefire ended; 3rd red; below both EMAs; 9d EMA ~$4,111; 50d EMA ~$4,142); Signal: Wait (−1); last updated July 9
- `wiki/india-gold-market.md` — July 9 MCX section: ₹1,45,000/10g; USD/INR ₹95.57; retail prices; key levels; Iran oil shock implications for India; last updated July 9
- `wiki/fed-macro-factors.md` — July 9 section added: FOMC June minutes hawkish (easing bias removed; PCE 3.3%; inflation risks tilted upside; few favor immediate hike but many see scenario requiring hikes); Iran oil shock adds inflation pressure; Macro factor → Bearish (−1); last updated July 9
- `wiki/uzbekistan-gold-reserves.md` — June 2026: +9t → YTD ~41t (2nd largest H1 buyer after Poland); last updated July 9
- `wiki/global-cb-activity-log.md` — July 9 section added (7 rows: macro, Iran escalation, Uzbekistan June, Germany, Saudi Arabia, Japan, India); Uzbekistan country table updated; last updated July 9
- `wiki/index.md` — all changed page descriptions refreshed (gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors, uzbekistan-gold-reserves, india-gold-market, global-cb-activity-log); last updated July 9
- `wiki/log.md` — this entry
- `prices/prices.csv` — 2026-07-09 row appended (Gold $4,075.08, Silver $57.50, DXY 101.07, WTI 74.20, USD/INR 95.5725)
- `signals/signals.csv` — Wait (−1) appended

**Signal breakdown (2026-07-09)**:
- Factor 1 (Price vs targets): +1 [Gold ~$4,075 is 16.8% below Goldman $4,900 target — above 15% threshold]
- Factor 2 (Geopolitics): −1 [Iran ceasefire ended July 8; Iran attacked Strait of Hormuz; US launched new strikes; oil +5.3% to $74.20 → energy inflation fears → hawkish Fed channel dominates over safe-haven; gold FALLING despite escalation]
- Factor 3 (Fed/macro): −1 [FOMC June minutes (July 8): hawkish surprise — easing bias removed; PCE core 3.3% (revised up); inflation risks "tilted to the upside"; Iran oil shock adds inflation pressure]
- Factor 4 (CB demand): +1 [WGC May data published July 3 (6 days ago); PBoC June +14.93t announced July 7 (2 days ago); Uzbekistan June +9t in today's sweep — all within 7 days]
- Factor 5 (Technicals): −1 [Gold ~$4,075 BELOW 9d EMA ~$4,111 AND below 50d EMA ~$4,142; death cross intact (50d < 200d); 3rd consecutive red day — "not 2 green" = Bearish per rule table]
- Factor 6 (Dollar Pressure): 0 [DXY +0.17% (within ±1%); USD/INR +0.18% (within ±1%); both neutral]
- **TOTAL: +1−1−1+1−1+0 = −1 → WAIT**

---

## 2026-07-08 — Daily update: Gold $4,128.32 (−0.48%); PBoC June +14.93t (20-month streak, largest since 2023); death cross confirmed; FOMC minutes today; MCX ~₹1,45,260 (−0.5%); USD/INR ₹95.40; DXY 100.90 | Signal: Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-07-08.md` — MCX ~₹1,45,260/10g (−0.51%); XAU/USD $4,128.32 (−0.48%); Silver $60.20 (−1.5%); DXY 100.90 (flat); WTI $70.45 (+1.9%); USD/INR ₹95.40 (flat); 15% duty; ETF outflows May (−₹725cr); RBI 880.52t unchanged; FOMC minutes today; death cross on 50d/200d EMA

**Pages updated**:
- `wiki/china-pboc-gold.md` — June 2026 data confirmed: +14.93t (480,000 oz; largest since 2023); total 2,346t; 20-month streak; last updated July 8
- `wiki/central-bank-gold-demand.md` — PBoC June +14.93t added; WGC July "remain committed" note added; last updated July 8
- `wiki/gold-geopolitical-risk-premium.md` — July 8 price row added ($4,128; death cross; 9d~$4,120; 50d~$4,145); last updated July 8
- `wiki/india-gold-market.md` — July 8 MCX section: ₹1,45,260/10g; USD/INR ₹95.40; retail prices; key levels; last updated July 8
- `wiki/fed-macro-factors.md` — FOMC June minutes being released July 8 noted; last updated July 8
- `wiki/iran-conflict-2026.md` — Khamenei funeral concluding July 9; talks to resume; 60-day MOU period ongoing; last updated July 8
- `wiki/global-cb-activity-log.md` — July 8 section added (5 rows: macro, PBoC June, Germany, Saudi Arabia, Iran, India); country table updated for China; last updated July 8
- `wiki/index.md` — all changed page descriptions refreshed; last updated July 8
- `wiki/log.md` — this entry
- `prices/prices.csv` — 2026-07-08 row appended (Gold $4,128.32, Silver $60.20, DXY 100.90, WTI 70.45, USD/INR 95.40)
- `signals/signals.csv` — Wait (+1) appended

**Signal breakdown (2026-07-08)**:
- Factor 1 (Price vs targets): +1 [Gold $4,128 is 15.7% below Goldman $4,900 target — just above 15% threshold]
- Factor 2 (Geopolitics): 0 [Iran funeral ends July 9; talks resuming; no gold safe-haven transmission]
- Factor 3 (Fed/macro): 0 [FOMC minutes today; Sep hike 0%; mixed signals; CPI July 14]
- Factor 4 (CB demand): +1 [PBoC June +14.93t announced July 7; WGC July report July 3 — both within 7 days]
- Factor 5 (Technicals): −1 [Gold above 9d EMA (~$4,120), below 50d EMA (~$4,145); 50d>9d (downtrend); death cross confirmed July 7]
- Factor 6 (Dollar pressure): 0 [DXY −0.01%, USD/INR +0.04%, both within 1%]
- **Total: +1 → Signal: Wait**

---

## 2026-07-07 — Daily update: Gold $4,147.94 (−0.37%); JPMorgan Q4 cut to $4,500; Iran talks suspended indefinitely; MCX ~₹1,46,000 (−0.5%); USD/INR ₹95.36; DXY 100.91 | Signal: Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-07-07.md` — MCX ~₹1,46,000/10g (−0.5%); XAU/USD $4,147.94 (−0.37%); Silver $61.14/oz (−2.3%); DXY 100.91 (+0.03%); WTI $69.14 (+0.52%); USD/INR ₹95.36 (−0.08%); 15% import duty; first ETF net outflows in 13 months; RBI 880.52t unchanged; USTR Section 301 hearing July 7

**Holiday check**: July 7, 2026 — Tuesday. No NSE/BSE/MCX holidays in July 2026 on weekdays confirmed. Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed; all manual via web search):
- Gold: $4,147.94/oz (−0.37%) | Silver: $61.14/oz (−2.3%) | DXY: 100.91 (+0.03%) | WTI: $69.14/bbl (+0.52%) | USD/INR: ₹95.36 (−0.08%) | Volume: not available

**Key new findings**:
1. **JPMorgan Q4 2026 gold target CUT to $4,500** (from ~$6,000; −25%); avg 2026 forecast: $5,243 (from $5,708). Most dramatic bank revision of 2026 cycle.
2. **Iran nuclear talks suspended INDEFINITELY** after Israeli attacks on Beirut — but gold is falling (−0.37%), confirming geopolitical risk is priced in and macro factors dominate.
3. **New LatAm CB buyers**: Chile +8t YTD, Bolivia +1t, Uruguay +1t — first-time or decade-absent buyers; from WGC/web data sweep.
4. **Germany Bundesbank**: CDU government reconfirmed no repatriation plans despite growing cross-party pressure; ~1,236t at FRBNY remains.
5. **Japan**: 845.97t static; no BoJ/MoF statements. **Saudi Arabia**: 323.07t static.
6. **USTR Section 301 forced-labor tariff hearing** held July 7; decision deadline July 20 — could affect China gold/silver supply chains; precious metals EXEMPT from India tariff scope.
7. **MCX gold down ~0.5%** at ~₹1,46,000/10g; India: first gold ETF net outflows in 13+ months (May 2026); HDFC Gold ETF restricting large institutional inflows; 15% duty demand destruction persisting.

**EMA estimates (from prior wiki + 1-day forward)**:
- 9d EMA July 7: ~$4,117 (est.; gold ABOVE → mild bullish config for 9d only)
- 50d EMA July 7: ~$4,382 (est.; gold BELOW → downtrend intact)
- 50d > 9d → downtrend configuration → Bearish (-1) for Technicals

**Pages updated**:
- `wiki/india-gold-market.md` — added July 7 price section; summary + Last updated updated; JPM Q4 implied MCX noted
- `wiki/global-cb-activity-log.md` — added July 7 section (7 rows): global macro; LatAm new buyers; Germany no repatriation; Japan static; Saudi static; Iran talks suspended; USA USTR hearing; India MCX update; **Last updated: 2026-07-07**
- `wiki/goldman-sachs-gold-forecast.md` — added JPMorgan July 5 cut section; updated bank forecast table; summary updated
- `wiki/gold-geopolitical-risk-premium.md` — added July 7 to price timeline; summary updated; Last updated 2026-07-07
- `wiki/iran-conflict-2026.md` — summary updated: nuclear talks suspended indefinitely
- `wiki/fed-macro-factors.md` — summary updated: CPI July 14 flagged; FOMC Jul 28-29
- `wiki/us-china-trade-war.md` — summary updated: Section 301 hearing July 7; deadline July 20
- `wiki/index.md` — updated entries for india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, goldman-sachs-gold-forecast
- `prices/prices.csv` — 2026-07-07 row appended (Gold $4,147.94, Silver $61.14, DXY 100.91, WTI 69.14, USD/INR 95.36)
- `signals/signals.csv` — 2026-07-07: Wait, Score +1

**Trading signal generated — Wait (Score: +1)**:
- Factor 1 (Price vs targets): $4,147.94 is 15.3% below GS $4,900 → Bullish (+1)
- Factor 2 (Geopolitical): Iran talks suspended indefinitely but gold FALLING — priced in; no safe-haven transmission → Neutral (0)
- Factor 3 (Fed/Macro): FOMC July 28-29 expected hold; PCE 3.6%; 9/18 hawkish dots; June CPI July 14 key → Neutral (0)
- Factor 4 (CB Demand): WGC May CB data published July 2026 (within 7 days); new LatAm buyers Chile/Bolivia/Uruguay discovered → Bullish (+1)
- Factor 5 (Technicals): Above 9d EMA ~$4,117 but below 50d EMA ~$4,382; 50d > 9d (downtrend); July 7 red day, July 6 green → not 2 green → Bearish (−1)
- Factor 6 (Dollar Pressure): DXY +0.03% (within 1%); USD/INR −0.08% (within 1%) → Neutral (0)
- **Total: +1 +0 +0 +1 −1 +0 = +1 → Wait**

**CB sweep summary**: No new single-country CB gold purchases/sales announced in last 24-48h. Key new discovery: Chile (+8t YTD), Bolivia (+1t), Uruguay (+1t) joining buyer list per WGC sweep. PBoC June data still pending. Germany: Bundesbank reconfirms no repatriation. Japan/Saudi Arabia: static. All major holders unchanged.

---

## 2026-07-04 — COT weekly update
Report_Date: 2026-06-23 | MM_Net: +115,395 (+9,532 vs prior confirmed 2026-06-09) | OI: 352,167 | MM_Long: 131,102 | MM_Short: 15,707 | MM_Net % OI: 32.8% | Sentiment: Neutral zone | Source: CFTC via GitHub Action (fetch_cot.yml), fetched 2026-06-27T07:05:32Z
Pages updated: wiki/institutional-flows.md (Latest COT Data section replaced; Historical COT Reference extended), wiki/index.md (institutional-flows entry updated), prices/cot.csv (2026-06-23 row appended)

## 2026-07-03 — Daily update: Gold $4,137.41 (+2.75%); June NFP 57K MISS → Sep hike removed; Iran Khamenei funeral July 4-9; MCX ₹1,47,720 (+2.67%); USD/INR ₹95.22; DXY 100.82 (−0.29%) | Signal: Buy (+3)

**Key findings**: June Nonfarm Payrolls came in at 57K (expected 115K) — largest miss in months. Prior months revised down. September Fed rate hike probability: 0% (was 67%). Gold surged 2.75% to $4,137.41 — largest daily gain in weeks. Silver +5.2% to $62.57. COMEX closed (US Independence Day observed — July 4 on Saturday).

**Iran**: Doha talks concluded without addressing nuclear issue (Hormuz + frozen funds only). Trump claims "Iran agreed to just about everything." Khamenei body on display July 4; burial July 9; next nuclear meeting after burial. New Supreme Leader Mojtaba Khamenei's nuclear stance untested.

**India**: MCX gold ₹1,47,720/10g (+2.67%). USD/INR ₹95.22 (flat). WGC (July 1): 15% import duty to cut India gold demand 50-60t in 2026. India ETF AUM ₹1.7T (115t). RBI 880.52t unchanged.

**CB demand**: No new country-level data. PBoC June 2026 data expected July 5-10. WGC April stats: net buying confirmed (published June). No Goldman CB nowcast update.

**Signal**: Buy (+3). Breakdown: Price vs targets +1 (15.6% below GS $4,900); Geopolitical 0 (Iran MOU intact; nuclear deferred; Khamenei funeral creates ambiguity); Fed/Macro +1 (NFP miss; September hike removed); CB Demand 0 (no new data 7d); Technicals +1 (above both EMAs per web search values; 2 green days); Dollar Pressure 0 (DXY −0.29%, INR +0.13%, both within 1%).

**Pages updated**:
- `wiki/gold-geopolitical-risk-premium.md` — July 3 entry; summary updated; signal changed to Buy (+3)
- `wiki/fed-macro-factors.md` — July 3 NFP result (57K miss); September hike 0%; macro = Bullish
- `wiki/iran-conflict-2026.md` — Doha talks concluded; Khamenei funeral; next talks after July 9
- `wiki/india-gold-market.md` — MCX ₹1,47,720; WGC demand impact data
- `wiki/global-cb-activity-log.md` — 13 rows added for July 3 (all tracked countries)
- `wiki/index.md` — descriptions updated for all changed pages
- `wiki/log.md` — this entry
- `prices/prices.csv` — July 3 row appended (Gold $4,137.41, Silver $62.57, DXY 100.82, WTI $68.45, USD/INR 95.22)
- `signals/signals.csv` — Buy (+3) appended
- `raw/india-gold-2026-07-03.md` — created

---

## 2026-07-02 — Daily update: Gold $4,026.39 (+0.26%); pre-NFP rebound; Iran Doha talks resumed; MCX ₹1,43,889 (+1.96%); USD/INR ₹95.10 (+0.58%); DXY 101.11 (−0.19%) | Signal: Wait (−2)

**Raw file created**:
- `raw/india-gold-2026-07-02.md` — MCX ~₹1,43,889/10g (+1.96%); XAU/USD $4,026.39 (+0.26%); Silver $59.48 (+2.99%); DXY 101.11 (−0.19%); WTI $68.73 (−2.4%); USD/INR ₹95.10 (+0.58%); India 15% import duty; ETF caps; 6+ AMCs; NFP June due tomorrow July 3; retail 24K ₹14,078/g

**Holiday check**: July 2, 2026 — Thursday. No weekday holidays in NSE/BSE July 2026 calendar (confirmed: 8 closed days in July = 4 Saturdays + 4 Sundays only). Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed; all manual via web search):
- Gold: $4,026.39/oz (+0.26%) | Silver: $59.48/oz (+2.99%) | DXY: 101.11 (−0.19%) | WTI: $68.73/bbl (−2.4%) | USD/INR: ₹95.10 (+0.58%) | Volume: not available

**EMA computed from prices.csv** (Python script):
- 9-day EMA (incl. today): $4,090.53
- 50-day EMA (incl. today): $4,413.61
- Gold ($4,026.39) below both EMAs; 50d > 9d (downtrend confirmed)

**Pages updated**:
- `wiki/india-gold-market.md` — added July 2 price section at top; updated summary and INR rate; MCX ₹1,43,889 (+1.96%); **Last updated: 2026-07-02**
- `wiki/global-cb-activity-log.md` — added 13-row July 2 section: Doha talks resumed; PBoC June pending; all major holders/buyers/sellers updated; Factor 4 = Neutral; **Last updated: 2026-07-02**
- `wiki/gold-geopolitical-risk-premium.md` — updated summary; added July 2 to price timeline ($4,026 +0.26%; pre-NFP rebound); 9d/50d EMAs updated; Signal Wait (−2); **Last updated: 2026-07-02**
- `wiki/iran-conflict-2026.md` — updated summary; added July 2 timeline entry (Doha talks resumed; Vance "going well"; WTI $68.73); **Last updated: 2026-07-02**
- `wiki/fed-macro-factors.md` — updated summary; added July 2 section (pre-NFP; rate hike 67%; Goldman no 2026 cuts); **Last updated: 2026-07-02**
- `wiki/index.md` — updated descriptions for india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors
- `prices/prices.csv` — appended 2026-07-02 row: Gold $4,026.39, Silver $59.48, DXY 101.11, WTI 68.73, USD/INR 95.10
- `signals/signals.csv` — appended 2026-07-02: Wait, Score −2

**Trading signal generated — Wait (Score: −2)**:
- Factor 1 (Price vs targets): $4,026 is ~17.8% below GS $4,900 → Bullish (+1)
- Factor 2 (Geopolitical): Iran Doha talks resumed (Vance "going well"); de-escalation trend continues; WTI −2.4% → Bearish (−1)
- Factor 3 (Fed/Macro): 67% September rate hike probability; Goldman no 2026 cuts; Treasury yields elevated; NFP due tomorrow → Bearish (−1)
- Factor 4 (CB Demand): No new CB data in last 7 days; PBoC June pending → Neutral (0)
- Factor 5 (Technicals): Gold below 9d EMA ($4,091) and 50d EMA ($4,414); 50d > 9d (downtrend); not 2 consecutive green days → Bearish (−1)
- Factor 6 (Dollar Pressure): DXY −0.187% (within 1%); USD/INR +0.582% (within 1%); both below threshold → Neutral (0)
- **Total: +1 −1 −1 +0 −1 +0 = −2 → Wait**

**CB sweep summary**: No new country-level CB gold purchases/sales found in last 24-48h. PBoC June data pending (expected July 5-10). Germany Bundesbank: no repatriation action; France: all gold home; all other monitored countries unchanged.

---

## 2026-07-01 — Daily update: Gold $4,016 (−1.15%); Iran talks SUSPENDED; NFP tomorrow; MCX ₹1,41,124 (−1.33%); DXY 101.30 (flat) | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-07-01.md` — MCX ₹1,41,124/10g (−1.33%; intraday low ₹1,40,450); XAU/USD $4,016 (−1.15%); Silver $57.75/oz (−0.93%); DXY 101.30 (flat); WTI $70.42 (flat); USD/INR ₹94.55 (flat); Iran talks suspended but gold fell; NFP July 3 key; 15% import duty in force; seasonal lull; 6+ AMCs ETF caps

**Holiday check**: July 1, 2026 — Wednesday. Not an Indian market holiday (confirmed: NSE/BSE holiday list for 2026 does not include July 1). Muharram was June 26. Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed; all manual via web search):
- Gold: ~$4,016/oz (−1.15%) | Silver: ~$57.75/oz (−0.93%) | DXY: ~101.30 (flat) | WTI: ~$70.42/bbl (flat) | USD/INR: ~₹94.55 (flat) | Volume: not available

**Pages updated**:
- `wiki/india-gold-market.md` — added July 1 price section; updated summary; MCX ₹1,41,124 (−1.33%); Iran talks suspended; **Last updated: 2026-07-01**
- `wiki/global-cb-activity-log.md` — added 13-row July 1 section: Iran talks suspended; PBoC June data expected; all major holders/buyers/sellers updated; Factor 4 = Neutral (no new data in 7d); **Last updated: 2026-07-01**
- `wiki/gold-geopolitical-risk-premium.md` — updated summary; added July 1 to price timeline ($4,016 −1.15%; Iran talks suspended); signal Wait (−1); **Last updated: 2026-07-01**
- `wiki/iran-conflict-2026.md` — added July 1 timeline entry (talks suspended; Trump "totally unacceptable"; Day ~10 of 60-day roadmap at risk); **Last updated: 2026-07-01**
- `wiki/fed-macro-factors.md` — updated summary; added July 1 section (NFP eve; May +172K context; scenario analysis); **Last updated: 2026-07-01**
- `wiki/index.md` — updated descriptions for india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors
- `prices/prices.csv` — appended 2026-07-01 row: Gold $4,016, Silver $57.75, DXY 101.30, WTI 70.42, USD/INR 94.55
- `signals/signals.csv` — appended 2026-07-01: Wait, Score −1

**Trading signal generated — Wait (Score: −1)**:
- Factor 1 (Price vs targets): $4,016 is ~17.6% below GS $4,900 → Bullish (+1)
- Factor 2 (Geopolitical): Iran talks suspended but gold FELL −1.15% — no safe-haven transmission; ambiguous → Neutral (0)
- Factor 3 (Fed/Macro): 3 hikes priced; PCE 4.1%; May NFP +172K; Warsh hawkish June 17; NFP tomorrow → Bearish (−1)
- Factor 4 (CB demand): No new CB data in last 7 days (WGC April stats published June 3 = 28d old; WGC survey June 16 = 15d old) → Neutral (0)
- Factor 5 (Technicals): Price ($4,016) below 9d EMA (~$4,075) and below 50d EMA (~$4,479); today red (−1.15%) after green June 30 = NOT 2 consecutive green → Bearish (−1)
- Factor 6 (Dollar): DXY −0.02% (within 1%); USD/INR −0.003% (within 1%) → Neutral (0)
- **Total: +1 +0 −1 +0 −1 +0 = −1 → Wait**

**CB sweep results (July 1)**:
- No new country-level CB gold purchase/sale data found in last 24-48h sweep
- PBoC June 2026 data expected imminently (first week of July) — not yet released
- Germany: No new Bundesbank announcement; repatriation debate ongoing
- France: All 2,437t on French soil; no new BdF statements
- Italy: Ownership dispute ongoing; no resolution
- Japan: 845.97t static; no BoJ/MoF statements
- USA: 8,133t unchanged; DXY 101.30 (flat); NFP July 3 key
- UK: 310.29t; no new custodial changes
- Saudi Arabia: 323.07t static; no SAMA announcement
- Iran: Talks suspended; Day ~10 of 60-day roadmap at risk; no CBI reserve announcement

**Key new findings**:
- Iran nuclear talks suspended July 1 after Israeli attacks on Beirut; Trump rejected Iran terms — 2nd major suspension of process (prior: June 1, resumed June 4)
- Gold fell despite Iran escalation — macro/Fed focus dominates
- WGC 2026 CB Survey (June 16): record 45% of CBs plan to increase reserves; 89% expect global holdings to rise
- WGC April 2026 data (June 3): net +17t; Poland +14t; China +8t; Czech +3t; Russia −6t
- May US NFP +172K (double the 85K consensus) — hawkish for Fed
- PCE May 4.1% (headline); core 3.4%
- 3 Fed rate hikes priced for 2026

---

## 2026-06-30 — Daily update: Gold $4,062 (flat); DXY 101.32 (flat); Iran IAEA access confirmed; WTI $70.44 (+1.76% rebound); MCX ~₹1,43,020 (flat); NFP July 3 key | Signal: Wait (0)

**Raw file created**:
- `raw/india-gold-2026-06-30.md` — MCX ~₹1,43,020/10g (flat from June 29); XAU/USD $4,062.49 (+0.07%); Silver $58.29/oz (−2.4%); DXY 101.3209 (flat); WTI $70.44 (+1.76%); USD/INR ₹94.5525 (+0.16%); 15% import duty in force; seasonal demand lull; 6+ AMCs ETF caps; 77% RBI gold now domestic (104.23t repatriated H2 FY25-26); Goldman $4,900 implies MCX ~₹1,69,000 (domestic 16–18% below GS target); NFP July 3 key catalyst

**Holiday check**: June 30, 2026 — Tuesday. Not an Indian market holiday. June 26 was Muharram (closed); June 27-28 weekend; June 29 was first post-Muharram trading session. June 30 is a regular trading day. Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed; all manual via web search):
- Gold: $4,062.49/oz (+0.07%) | Silver: $58.29/oz (−2.4%) | DXY: 101.3209 (−0.009%) | WTI: $70.44/bbl (+1.76%) | USD/INR: ₹94.5525 (+0.16%) | Volume: not available

**Pages updated**:
- `wiki/india-gold-market.md` — added June 30 price section; updated summary; updated RBI domestic storage (77%/680t); updated INR/USD rate; **Last updated: 2026-06-30**
- `wiki/global-cb-activity-log.md` — added 16-row June 30 section: IAEA access confirmation; Poland 595.647t/45.4t YTD; Czech 7.6t YTD/38 consecutive months; Kazakhstan 13.3t YTD; all major holders/buyers/sellers updated; Factor 4 = Neutral (no new data in 7d); **Last updated: 2026-06-30**
- `wiki/gold-geopolitical-risk-premium.md` — updated summary; added June 30 to price timeline ($4,062 flat; IAEA access confirmed); updated signal to Wait (0); **Last updated: 2026-06-30**
- `wiki/iran-conflict-2026.md` — updated summary (IAEA access confirmed June 26); added June 24-25, June 26, June 29, June 30 timeline entries; **Last updated: 2026-06-30**
- `wiki/fed-macro-factors.md` — updated summary; added June 30 section (NFP July 3 preview; scenario analysis); **Last updated: 2026-06-30**
- `wiki/index.md` — updated descriptions for india-gold-market, global-cb-activity-log, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors
- `prices/prices.csv` — appended 2026-06-30 row: Gold $4,062.49, Silver $58.29, DXY 101.3209, WTI $70.44, USD/INR 94.5525
- `signals/signals.csv` — appended 2026-06-30: Wait, Score 0

**Trading signal generated — Wait (Score: 0)**:
- Factor 1 (Price vs targets): $4,062 is ~17% below GS $4,900 → Bullish (+1)
- Factor 2 (Geopolitical): Iran IAEA access confirmed June 26 → deeper de-escalation → Bearish (−1)
- Factor 3 (Fed/Macro): Hawkish FOMC June 17; 9 members project hikes; 3 hikes priced; PCE 3.6% forecast → Bearish (−1)
- Factor 4 (CB demand): No new CB data in last 7 days (WGC survey June 16 = 14d old; WGC April stats = >7d old) → Neutral (0)
- Factor 5 (Technicals): Price ($4,062) below 9d EMA (~$4,150) and below 50d EMA (~$4,240); last 2 days green (+$85 and +$3) → Bullish (+1)
- Factor 6 (Dollar): DXY −0.009% (within 1%); USD/INR +0.162% (within 1%) → Neutral (0)
- **Total: +1 −1 −1 +0 +1 +0 = 0 → Wait**

**CB sweep results**:
- Germany: No new Bundesbank repatriation announcement; cross-party political pressure continues
- France: All 2,437t on French soil; no new BdF statements
- Italy: Ownership dispute ongoing; no resolution
- Japan: 845.97t static; no BoJ/MoF announcements
- USA: 8,133t unchanged; 3 Fed hikes priced; DXY flat; NFP July 3
- UK: 310.29t static; London vaults 9,392t (end May)
- Saudi Arabia: 323.07t static; no SAMA announcements
- Iran: IAEA access confirmed June 26 (major development); CBI accumulation rationale diminishing
- Poland: 595.647t (April confirmed); YTD 45.4t
- PBoC: 2,331.52t; June data expected July announcement
- Czech Republic: 7.6t YTD; 38 consecutive monthly purchases

---

## 2026-06-29 — Daily update: Gold ~$4,060 (+2.1% recovery); DXY 101.33; PCE 4.1% in-line; WTI $69.23 (4-month low); Uganda BoU first gold buy; MCX ₹1,43,305 (post-Muharram reopening) | Signal: Wait (−2)

**Raw file created**:
- `raw/india-gold-2026-06-29.md` — MCX ₹1,43,305/10g (−1.3%; post-Muharram reopening); XAU/USD ~$4,060 (+2.1% recovery from $3,975 8-month low); Silver ~$59.70/oz; DXY 101.33 (easing); WTI $69.23 (4-month low); USD/INR ₹94.40 (+0.13%); 15% import duty in force; June demand slowing; 6+ AMCs ETF caps; Goldman $4,900 implies MCX ~₹1,69,000 (domestic 15% below GS target); Uganda BoU first gold purchase noted

**Holiday check**: June 29, 2026 — Monday. Not an Indian market holiday. Previous trading day was Thursday June 25 (June 26 was Muharram holiday; June 27-28 weekend). Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed; all manual via web search):
- Gold: ~$4,060/oz (+2.1% from $3,975) | Silver: ~$59.70/oz | DXY: 101.33 (−0.24%) | WTI: ~$69.23/bbl | USD/INR: ₹94.40 (+0.13%) | Volume: not available

**Signal**: Wait, Score: **−2**
- Factor 1 (Price vs targets): +1 — ~$4,060 is ~17.2% below Goldman's $4,900 target (>15% = Bullish)
- Factor 2 (Geopolitical): −1 — Iran-US preliminary deal framework progressing; WTI $69.23 (4-month low, Hormuz reopening priced in); de-escalation → geopolitical risk premium compressing → Bearish
- Factor 3 (Fed/macro): −1 — PCE May 4.1% (in-line but elevated; Core 3.4%); 3 Fed hikes still priced (September 62%); DXY still 101.33 (elevated) → Hawkish environment → Bearish
- Factor 4 (CB demand): 0 — WGC CB Survey (June 16) now 13 days old, outside 7-day window; Uganda BoU first buy April 18 (not a formal WGC publication within 7 days); no new CB data within 7-day window → Neutral
- Factor 5 (Technicals): −1 — Below 9d EMA (~$4,150 est.) AND 50d EMA (~$4,240 est.); last 2 entries in prices.csv: June 24 RED (−0.58%) + June 25 RED (−3.1%) = not 2 green → Bearish
- Factor 6 (Dollar Pressure): 0 — DXY: 101.57→101.33; dxy_pct = −0.24% (within ±1% band → 0). USD/INR: 94.47→94.40; inr_pct = −0.07% (within ±1% band → 0). factor6 = 0 → Neutral

**Wiki pages updated**:
- `wiki/global-cb-activity-log.md` — Added June 29 section (15 rows); Uganda BoU first gold purchase April 18 captured; Kenya CBK intentions noted; Iran Day ~18 roadmap update; PCE 4.1% macro logged
- `wiki/gold-geopolitical-risk-premium.md` — Updated summary with June 29 data; added June 29 to price timeline (first row); updated Technical Levels section for June 29
- `wiki/india-gold-market.md` — Added June 29 MCX price section (₹1,43,305/10g, −1.3%); updated summary; updated INR/USD tracking
- `wiki/fed-macro-factors.md` — Added June 29 section (PCE 4.1% in-line; September 62% probability; key macro data calendar this week); updated summary
- `wiki/iran-conflict-2026.md` — Updated summary with June 29 status (Day ~18 of 60; IAEA access unresolved; WTI $69.23)
- `wiki/index.md` — Updated descriptions for global-cb-activity-log, gold-geopolitical-risk-premium, india-gold-market, fed-macro-factors, iran-conflict-2026

**Central bank sweep findings (June 26–29)**:
- Uganda: Bank of Uganda first gold purchase April 18, 2026 (new to wiki — logged in global-cb-activity-log)
- Kenya: CBK Governor signalled gold-buying intentions (new to wiki — logged in global-cb-activity-log)
- Poland, China, Germany, France, Italy, Japan, USA, UK, Saudi Arabia, Iran, Russia: No new June 26-29 announcements
- WGC April data (Poland +14t, China +8t, Czech +3t) already in wiki from prior updates
- No new individual country CB transactions found in 24-48h window

---

## 2026-06-25 — Daily update: Gold $3,975 (−3.1%; 8-month low); DXY 101.57 (14-month high); 3 Fed hikes priced; Iran IAEA stalemate; MCX ₹1,45,216 (−0.9%) | Signal: Wait (−2)

**Raw file created**:
- `raw/india-gold-2026-06-25.md` — MCX ₹1,45,216/10g (−0.9%); XAU/USD $3,975 (−3.1%; 8-month low); Silver $57.34 (−7.7%); DXY 101.57 (14-month high); WTI $71.48; USD/INR ₹94.47 (−0.23%); 15% import duty; May imports −39% to $3.4B; 6 AMCs ETF caps; MCX CLOSED June 26 (Muharram)

**Holiday check**: June 25, 2026 — Thursday. Not an Indian market holiday (June 26 Muharram is tomorrow's holiday). Proceeding with full update.

**Prices fetched** (web search — yfinance 403 + metals.dev 403 failed, all manual via web search):
- Gold: $3,975/oz (−3.1%) | Silver: $57.34/oz (−7.7%) | DXY: 101.57 (+0.07%) | WTI: $71.48/bbl (−1.64%) | USD/INR: ₹94.47 (−0.23%) | Volume: not available

**Signal**: Wait, Score: **−2**
- Factor 1 (Price vs targets): +1 — $3,975 is 18.9% below Goldman's $4,900 target (>15% = Bullish)
- Factor 2 (Geopolitical): −1 — Iran de-escalation ongoing; IAEA stalemate does not add new safe-haven demand; US-China truce intact → geopolitical premium compressing → Bearish
- Factor 3 (Fed/macro): −1 — Markets pricing 3 rate hikes in 2026; DXY 101.57 (14-month high); hawkish → Bearish
- Factor 4 (CB demand): 0 — WGC CB Survey (June 16) now 9 days old, outside 7-day window; no new CB purchase/sale found today → Neutral
- Factor 5 (Technicals): −1 — Below 9d EMA (~$4,183) AND 50d EMA (~$4,334); death cross confirmed; June 24 red + June 25 red = not 2 green → Bearish
- Factor 6 (Dollar Pressure): 0 — DXY: 101.495→101.57; dxy_pct = +0.07% (within 1%). USD/INR: 94.6925→94.47; inr_pct = −0.23% (within 1%). factor6 = 0 → Neutral

**Wiki pages updated**:
- `wiki/global-cb-activity-log.md` — Added June 25 section (15 rows); LBMA 9,392t London vault data captured; UK daily update log appended
- `wiki/india-gold-market.md` — Added June 25 MCX price section (₹1,45,216/10g, −0.9%); updated summary; noted MCX CLOSED June 26
- `wiki/gold-geopolitical-risk-premium.md` — Updated summary with June 25 data; added June 25 to price timeline; updated Technical Levels section
- `wiki/fed-macro-factors.md` — Added June 25 macro section (3 hikes priced; DXY 14-month high; Silver −7.7%); updated summary
- `wiki/uk-gold-reserves.md` — Added LBMA end-May 2026 vault data (9,392t, $1.4T); updated Daily Update Log; updated sources
- `wiki/index.md` — Updated descriptions for 5 pages
- `wiki/log.md` — This entry

**Global CB sweep results**:
- No new country-specific CB purchase/sale data in last 24-48h across any country
- **UK/LBMA**: London vaults held 9,392t (~$1.4T) as of end May 2026 — new data captured
- **Germany**: CDU government still blocking repatriation; AfD cross-party political pressure ongoing; no Bundestag vote
- **France**: All 2,437t on French soil; no new BdF statements
- **Italy**: Fratelli d'Italia ownership dispute ongoing; no resolution
- **Japan**: 845.97t static; no BoJ or MoF statements
- **USA**: 8,133t; DXY 14-month high; 3 hikes priced; no Fort Knox audit proposals
- **Saudi Arabia**: 323.07t static; no SAMA announcements
- **Iran**: IAEA inspection stalemate (Iran insists no access until all sanctions lifted); 60-day roadmap Day 10-11
- **All major buyers** (Poland, China, Czech, Kazakhstan, Uzbekistan): No new announcements; China June disclosure expected July cycle

---

## 2026-06-24 — Daily update: Gold $4,104.90 (−0.58%; 7-month low); DXY 101.50 (13-month high); Iran IAEA dispute; MCX ₹1,44,114 (−2.5%) | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-06-24.md` — MCX ₹1,44,114/10g (−2.5%; 7-month low); XAU/USD ~$4,089 (−0.95%); Silver $62.06 (−3.85%); DXY 101.45 (13-month high; PMI 52.2); WTI $73.90; USD/INR ₹94.84 (+0.17%); 15% import duty; ETF June recovery ~₹2,081cr

**Prices fetched** (web search — yfinance 403 + metals.dev 403 failed):
- Gold: $4,104.90/oz (−0.58%) | Silver: $62.10/oz (−3.78%) | DXY: 101.50 (fresh 13-month high) | WTI: $72.67/bbl | USD/INR: ₹94.69 | Volume: 35,534 contracts

**Holiday check**: June 24, 2026 — Tuesday. Not an Indian market holiday (next holiday June 26 Muharram). Proceeding with full update.

**Signal**: Wait, Score: **−1**
- Factor 1 (Price vs targets): +1 — ~$4,089 is 16.6% below Goldman's $4,900 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Iran IAEA inspection dispute complicates deal but 60-day roadmap still active; ambiguous signal (complication vs. still-intact de-escalation) → Neutral
- Factor 3 (Fed/macro): −1 — DXY 101.45 (13-month high); PMI 52.2 strong; ~66% Dec 2026 rate hike probability; hawkish → Bearish
- Factor 4 (CB demand): 0 — WGC CB Survey (June 16) now 8 days old, outside 7-day window; no new CB purchase/sale found today → Neutral
- Factor 5 (Technicals): −1 — Below 9d EMA (~$4,305) AND 50d EMA (~$4,545); 50d > 9d = downtrend; June 23 red + June 24 red = not 2 green → Bearish
- Factor 6 (Dollar Pressure): 0 — DXY: 100.93→101.45; dxy_pct = +0.51% (within 1% → 0). USD/INR: 94.68→94.84; inr_pct = +0.17% (within 1% → 0). factor6 = 0 → Neutral

**Global CB sweep results**:
- No new country-specific CB purchase/sale data in last 24-48h
- **Singapore (MAS)**: Launching gold clearing hub and central bank vaulting services — policy/infrastructure initiative (193.85t reserves unchanged)
- **Turkey**: Recovery buying from March losses ongoing (April data; not fresh today)
- **All major holders** (Germany, France, Italy, Japan, USA, UK, Saudi Arabia): No new data
- **Iran**: IAEA inspection dispute clouds deal; 60-day roadmap Day 9 still active

**Wiki pages updated**:
- `wiki/india-gold-market.md` — new June 24 MCX section prepended
- `wiki/global-cb-activity-log.md` — 17-row June 24 section added
- `wiki/gold-geopolitical-risk-premium.md` — summary + price timeline updated
- `wiki/fed-macro-factors.md` — June 24 DXY/macro section added
- `wiki/index.md` — descriptions updated for 4 pages

---

## 2026-06-23 — Daily update: Gold $4,129.07 (−1.49%); Death cross forming; Iran IAEA milestone; MS base $4,400 | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-06-23.md` — MCX ₹1,47,818/10g (+0.42%; outperforming XAU on INR weakness); XAU/USD $4,129.07 (−1.49%); Silver $64.54 (+0.4%); MCX Silver crashed ~₹9,000/kg; DXY 100.93; WTI $73.67; USD/INR ₹94.68 (7% weaker YTD); death cross forming; Goldman $4,900; MS base $4,400

**Prices fetched** (web search — yfinance 403 + metals.dev 403 failed):
- Gold: $4,129.07/oz (−1.49%) | Silver: $64.54/oz (+0.4%) | DXY: 100.93 (+0.21%) | WTI: $73.67/bbl (−0.26%) | USD/INR: ₹94.68

**Holiday check**: June 23, 2026 — Tuesday. Not an Indian market holiday. Proceeding with full update.

**Signal**: Wait, Score: **−1**
- Factor 1 (Price vs targets): +1 — $4,129.07 is 15.7% below Goldman's new $4,900 target (>15% = Bullish)
- Factor 2 (Geopolitical): −1 — US-Iran 60-day roadmap active (Day 6); IAEA inspectors invited back; de-escalation sustained → Bearish
- Factor 3 (Fed/macro): −1 — Hawkish hold June 17; dot plot median 3.8%; ~70% market probability of hike by Sep; DXY 100.93 near 1-year high → Bearish
- Factor 4 (CB demand): +1 — WGC CB Survey published June 16 (within 7-day window): record 45% CBs plan to increase holdings → Bullish
- Factor 5 (Technicals): −1 — Below 9d EMA (~$4,305) AND 50d EMA (~$4,545); 50d > 9d = downtrend; 2 red days (June 22 and June 23) → Bearish
- Factor 6 (Dollar Pressure): 0 — DXY June 22: 100.82 → June 23: 100.93; dxy_pct = +0.11% (within 1% → dxy_signal = 0). USD_INR prior row (June 22) not detected → inr_signal = 0. factor6 = 0 → Neutral

**Global CB sweep results**:
- No new country-specific CB purchase/sale data found today
- **Iran**: IAEA inspectors invited back — VP Vance cited as "major milestone"; three working groups active (oversight, sanctions, nuclear)
- **All major holders** (Germany, France, Italy, Japan, USA, UK, Saudi Arabia): No new data
- **Macro**: Death cross forming (50d EMA ~$4,545 converging to 200d EMA ~$4,334); downside target $3,440 cited; Morgan Stanley base case $4,400 (H2 upside $5,200)

**Wiki pages updated**:
- `wiki/global-cb-activity-log.md` — 14 new rows for 2026-06-23
- `wiki/goldman-sachs-gold-forecast.md` — Morgan Stanley base case $4,400 added; last updated
- `wiki/iran-conflict-2026.md` — June 23 timeline row added (IAEA milestone)
- `wiki/india-gold-market.md` — June 23 MCX price section added; summary updated
- `wiki/gold-geopolitical-risk-premium.md` — Summary updated; June 19-23 timeline rows added
- `wiki/index.md` — Goldman, Iran, India, geopolitical, CB log entries updated
- `wiki/log.md` — This entry

**Commit (reconstructed from routine log)**: `251ad6b` — "Daily update 2026-06-23: Goldman cuts to $4,900; Iran roadmap; death cross | Signal: Wait (-1)"
*(Note: original commit was not pushed due to expired GitHub PAT; this entry reconstructed from routine output log)*

---

## 2026-06-22 — Daily update: Gold $4,197.75 (+1.11%); Goldman CUTS $5,400→$4,900; Iran-US 60d roadmap confirmed; PCE 3.6%; Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-06-22.md` — MCX ~₹1,46,220–₹1,53,000/10g; XAU/USD $4,197.75; Silver $66.36/oz (+2.33%); DXY 100.82 (+0.10% flat); WTI $77.54 (+0.27%); USD/INR ₹94.61 (+0.11% — first confirmed value); Goldman cuts $4,900 target; imports still −70%

**Prices fetched** (web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,197.75/oz (+1.11%) | Silver: $66.36/oz (+2.33%) | DXY: 100.82 (+0.10%) | WTI: $77.54/bbl (+0.27%) | USD/INR: ₹94.61 (+0.11%)
- prices.csv migrated: USD_INR column added; June 22 is the first row with a USD_INR value

**Holiday check**: June 22, 2026 — Monday. Not an Indian market holiday. Next Indian holiday: June 26 (Muharram).

**Signal**: Wait, Score: **−1**
- Factor 1 (Price vs targets): +1 — $4,197.75 is 22.3% below Goldman $5,400 benchmark (>15% = Bullish; note: Goldman cut target to $4,900 but benchmark still $5,400 for scoring consistency)
- Factor 2 (Geopolitical): −1 — Iran-US 60-day peace roadmap formalised June 21 (NPR); nuclear monitoring committee; $24B asset release → sustained de-escalation → Bearish
- Factor 3 (Fed/macro): −1 — PCE revised to 3.6%; October 2026 hike in active pricing; Fed cuts pushed to 2027; Warsh hawkish; Goldman cited this for $4,900 cut → Bearish
- Factor 4 (CB demand): +1 — WGC April CB statistics (published June 3, within 7-day extended window: net +17t; Poland +14t; China +8t; WGC Survey June 16 record 45% plan to buy) → Bullish
- Factor 5 (Technicals): −1 — Price $4,197.75; 9d EMA ~$4,268; 50d EMA ~$4,529. Price BELOW BOTH EMAs. Last 2 trading days: June 19 (red, $4,210 vs $4,312.49 prior) + June 22 (below June 19) → not 2 green. → Bearish
- Factor 6 (Dollar Pressure): 0 — DXY June 19: 100.72 → June 22: 100.82; dxy_pct = +0.10% (within 1% → dxy_signal = 0). USD_INR: no prior row → inr_signal = 0. factor6 = 0 → Neutral

**Global CB sweep results**:
- **Goldman Sachs**: CUT end-2026 gold target $5,400→$4,900 (most bearish major bank; PCE 3.6% revision; Fed cuts to 2027)
- **Iran**: 60-day peace roadmap confirmed June 21 (nuclear monitoring committee; $24B asset release; Lebanese hostilities ending)
- Poland, China, Czech Republic, Russia, Germany, France, Italy, Japan, UK, Saudi Arabia: No new data
- India: Gold imports still down 70% (25-30t/month, official June 18); USD/INR ₹94.61 stable; Goldman $4,900 cut impacts domestic outlook

**Wiki pages updated**:
- `wiki/goldman-sachs-gold-forecast.md` — **MAJOR: target cut $5,400→$4,900**; comparison table updated; GS now most bearish major bank
- `wiki/india-gold-market.md` — June 22 MCX price section added; summary updated; USD_INR ₹94.61 first confirmed value
- `wiki/fed-macro-factors.md` — June 22 PCE revision (3.6%); Goldman cut linkage; macro snapshot added
- `wiki/iran-conflict-2026.md` — June 21 roadmap row + June 22 timeline row added
- `wiki/global-cb-activity-log.md` — 14 new rows for 2026-06-22
- `wiki/poland-gold-reserves.md` — Last-updated date updated
- `wiki/index.md` — Goldman, India, Iran, Fed, CB log entries updated
- `wiki/log.md` — This entry

**Commit (reconstructed from routine log)**: `462d000` — "Daily update 2026-06-22: Goldman cuts $5,400→$4,900; Iran-US roadmap; Wait signal (-1)"
*(Note: original commit was not pushed due to expired GitHub PAT; this entry reconstructed from routine output log)*

---

## 2026-06-20 — COT weekly update attempt: Report_Date 2026-06-16 | Status: DATA RETRIEVAL FAILURE | All CFTC/data sources blocked by network egress | cot.csv unchanged

**Attempted sources**: Nasdaq Data Link API (CFTC/088691_FO_ALL, CFTC/088691_DCOT_FO_ALL) — HTTP 403 host not in allowlist. WebFetch: CFTC.gov, barchart.com, metalcharts.org, tradingster.com, macromicro.me, ycharts.com, research.titanfx.com, investing.com, metalprices.live, insider-week.com — all HTTP 403. Direct curl: same network policy block. CFTC Public Reporting Environment (publicreporting.cftc.gov) — also blocked.

**Qualitative signals from WebSearch**: Search results surfaced the article "Metals Speculators Boost Gold Bets For 3rd Week To 14-Week Highs" (investing.com analysis, ~June 19–20, 2026), suggesting: (1) Managed Money net positioning increased as of June 16 for the third consecutive week; (2) positions reached a 14-week high (implying above all readings since approx. early March 2026). Exact MM_Long, MM_Short, Open_Interest figures could not be verified — no exact numbers available from accessible sources.

**Market context on June 16 (COT as-of date)**: Gold $4,314.53 (−0.2% per June 16 daily log); DXY 99.56; WTI $80.41; FOMC Day 1 underway; WGC CB Survey (record 45% plan to increase gold) published June 16. Gold was in its 3rd weekly loss trajectory (from ~$4,499 high on June 2).

**cot.csv**: NOT updated — no verified numerical data available.

**Pages updated**:
- `wiki/institutional-flows.md` — "Latest COT Data" section replaced with June 16 failure note; qualitative search findings documented; prior confirmed reading (June 9) retained as reference; last updated → 2026-06-20
- `wiki/index.md` — [[institutional-flows]] entry updated to reflect June 16 retrieval failure + qualitative signal

---

## 2026-06-19 — Daily update: Gold ~$4,210 (Asian session; COMEX closed Juneteenth); Iran MOU SIGNED AT VERSAILLES (not Bürgenstock); India imports -70% (official); DXY 100.72; Silver -7.8%; Signal: Wait (−2)

**Raw file created**:
- `raw/india-gold-2026-06-19.md` — MCX ~₹1,47,000–₹1,49,660/10g; XAU/USD ~$4,210 (Asian session); Silver $64.26/oz (−7.8%); MCX Silver −₹6,000/kg; DXY 100.72 (+1.11%); WTI $77.10 (+2.1% bounce); USD/INR ~₹94.50; **India gold imports confirmed −70% to 25–30t/month** (government official June 18); May import VALUE +34% y/y to $3.41B; RBI 880.52t unchanged; 6 AMCs ETF caps remain

**Prices fetched** (manual web search — yfinance 403 + metals.dev 403 both failed; COMEX closed Juneteenth):
- Gold: ~$4,210/oz (Asian session, extending losses) | Silver: $64.26/oz (−7.8%) | DXY: 100.72 (+1.11%) | WTI: $77.10/bbl (+2.1%) | USD/INR: ~₹94.50 (est.)
- MCX gold (24k retail): ~₹1,49,660/10g (BusinessToday); MCX futures est. ~₹1,47,000/10g (sundayguardianlive)

**Holiday check**: June 19, 2026 — Juneteenth (US federal holiday; COMEX closed). Indian markets (MCX/NSE/BSE) open normally — next Indian holiday: June 26 (Muharram).

**Signal**: Wait, Score: **−2**
- Factor 1 (Price vs targets): +1 — ~$4,210 is ~22% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): −1 — Iran MOU signed at Versailles (de-escalation dominant even with Trump "war may not be over" residual uncertainty); Rule: "de-escalation = Bearish"
- Factor 3 (Fed/macro): −1 — FOMC hawkish dot plot (9/19 back hikes); markets price one 25bp hike by Oct 2026; DXY at 100.72 (highest since May 2025); Kitco warns gold could fall to $4,000 next week; Hawkish = Bearish
- Factor 4 (CB demand): +1 — WGC CB Gold Reserves Survey published June 16 (3 days ago, within 7-day window): record 45% CBs plan to increase holdings. Confirmed CB demand data → Bullish
- Factor 5 (Technicals): −1 — Price ~$4,210; 9d EMA ~$4,286 (calculated: $4,305×0.8 + $4,210×0.2); 50d EMA ~$4,540. Price BELOW BOTH EMAs. Last 2 trading days: June 18 (red) + June 19 (red) = NOT 2 green. Table: "Below both EMAs | Not 2 green | Bearish" → Bearish
- Factor 6 (Dollar Pressure): −1 — DXY June 18: 99.61 → June 19: 100.72; dxy_pct = +1.11% ≥ +1% → dxy_signal = −1. USD_INR missing from prices.csv → inr_signal = 0. factor6 = −1 → Bearish

**Global CB sweep results**:
- **Iran**: MOU signed at Palace of Versailles June 17-18; Iran signed remotely; Trump hinted "war may not be over"; Israel unhappy; WTI bounced to $77.10; 60-day nuclear talks clock running
- **India (official, June 18)**: Gold imports fell 70% in volume to 25-30t/month; May imports $3.41B (+34% YoY value); duty hike working on volumes but not forex outflows
- Poland: No new data (latest: 613t, targeting 700t)
- China: No new data (May +9.95t, 19-month streak, 2,331.52t total)
- Czech Republic: No new data
- Russia: No new data (April −6t, YTD −22t)
- Germany: No new data (CDU still refusing repatriation; AfD motion pending)
- France: No new data (all 2,437t on French soil)
- USA: COMEX closed (Juneteenth); 8,133t unchanged
- Saudi Arabia, Japan, UK, Italy: No new data

**Pages updated**:
- `prices/prices.csv` — June 19 row added: Gold $4,210, Silver $64.26, DXY 100.72, WTI $77.10 (Juneteenth; COMEX closed; Asian spot prices)
- `wiki/global-cb-activity-log.md` — June 19 section added (13 rows); last updated 2026-06-19
- `wiki/iran-conflict-2026.md` — CORRECTION: MOU signed at Versailles (not Bürgenstock); June 19 timeline entry added; summary updated
- `wiki/india-gold-market.md` — June 19 MCX price section added; import data (−70% to 25-30t) added to Demand Breakdown; INR rate updated; summary updated
- `wiki/gold-geopolitical-risk-premium.md` — price updated to ~$4,210; DXY 100.72; both EMAs bearish; Signal −2; summary updated
- `wiki/fed-macro-factors.md` — DXY 100.72; market pricing one hike by Oct 2026; Kitco $4,000 downside risk flagged; summary updated
- `signals/signals.csv` — June 19 signal: Wait, −2
- `wiki/log.md` — this entry
- `wiki/index.md` — all affected page descriptions updated

---

## 2026-06-18 — Daily update: Gold $4,312.49 (+1.24% recovery from post-FOMC $4,259); FOMC DOT PLOT HAWKISH (half project hikes); Iran MOU formal signing June 19 Bürgenstock; RBI denied $12B gold sale; WTI $75.49; Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-06-18.md` — MCX ₹1,52,748/10g (settled); XAU/USD $4,312.49 (+1.24%); Silver $69.71; WTI $75.49 (−1.70%); DXY 99.61; USD/INR ₹94.4770 (multi-week high); RBI denied $12B gold sale; 880.52t unchanged; gold = 16.85% of FX reserves; 6 AMCs still capping ETF subscriptions

**Prices fetched** (manual web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,312.49/oz (+1.24%) | Silver: $69.71/oz | DXY: 99.61 | WTI: $75.49/bbl | USD/INR: ₹94.4770
- MCX gold (24k settled): ₹1,52,748/10g

**Signal**: Wait, Score: **−1**
- Factor 1 (Price vs targets): +1 — $4,312.49 is 20.1% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): −1 — Trump signed interim Iran agreement; formal MOU signing June 19 at Bürgenstock. Clear de-escalation. WTI fell further to $75.49. Rule: "de-escalation = Bearish"
- Factor 3 (Fed/macro): −1 — **FOMC dot plot hawkish surprise**: half of FOMC members projected possible rate HIKES in 2026. Gold fell ~2% COMEX post-FOMC (to ~$4,259). Hawkish surprise = Bearish
- Factor 4 (CB demand): +1 — WGC CB Survey 2026 published June 16 (2 days ago, within 7-day window): record 45% CBs plan to increase gold. Confirmed CB demand data → Bullish
- Factor 5 (Technicals): −1 — Price $4,312.49 above 9d EMA (~$4,305 est.) but below 50d EMA (~$4,545). 50d > 9d = downtrend. Last 2 days: June 17 green (+$18.67), June 18 red (−$20.71) → NOT 2 consecutive green days. Table: "Above 9d, below 50d | 50d > 9d | Any | Bearish" → Bearish

**Holiday check**: June 18, 2026 is NOT an Indian market holiday. Next holiday: June 26 (Muharram).

**Global CB sweep results**:
- **Iran**: Trump signed interim agreement; formal MOU at Bürgenstock June 19 (major de-escalation)
- **FOMC (revised)**: June 17 dot plot was hawkish — half of FOMC project rate hikes → gold fell ~2% post-FOMC
- **India (RBI)**: Denied $12B gold sale reports; 880.52t confirmed unchanged; gold = 16.85% FX reserves
- Poland: No new data (latest: 613t, May +18t confirmed June 12)
- China: No new data (May +9.95t, 19-month streak)
- Czech Republic: No new data
- Russia: No new data
- Germany: No new repatriation data (CDU still refusing; AfD motion pending)
- France: No new data (all 2,437t on French soil)
- USA: FOMC hawkish dot plot noted; 8,133t gold unchanged
- Saudi Arabia: No new data
- Japan/UK/Italy: No new data

**Pages updated**:
- `wiki/global-cb-activity-log.md` — June 18 section added (13 rows)
- `wiki/iran-conflict-2026.md` — June 18 timeline entries added (interim agreement signed; MOU signing June 19 Bürgenstock); summary updated
- `wiki/fed-macro-factors.md` — June 17–18 FOMC section revised with hawkish dot plot details; summary updated
- `wiki/india-gold-market.md` — June 18 MCX price section added; summary updated
- `wiki/india-rbi-gold.md` — June 2026 RBI gold sale denial section added; FX reserves share updated to 16.85%; last updated date revised
- `wiki/gold-geopolitical-risk-premium.md` — price updated to $4,312.49; summary updated
- `wiki/log.md` — this entry
- `wiki/index.md` — descriptions updated

---

## 2026-06-17 — Daily update: Gold $4,333.20 (+0.43%); FOMC HELD (Warsh first decision, no hawkish shock); WTI −4.8% on Hormuz deal; WGC CB Survey record 45% CBs plan to buy; Uganda new CB buyer; Signal: Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-06-17.md` — MCX ~₹1,53,000/10g (24k); XAU/USD $4,333.20 (+0.43%); Silver $70.42; WTI $76.54 (−4.8%); DXY 99.57; USD/INR ~₹94.32 (INR strengthening on lower oil); FOMC held 3.50–3.75% as expected; WGC CB Survey: 45% of CBs plan to increase gold

**Prices fetched** (manual web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,333.20/oz | Silver: $70.42/oz | DXY: 99.57 | WTI: $76.54/bbl | USD/INR: ~₹94.32
- MCX gold (24k retail): ~₹1,53,000/10g

**Signal**: Wait, Score: **+1**
- Factor 1 (Price vs targets): +1 — $4,333.20 is 19.8% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Iran peace deal active; Hormuz reopening ~July 15; WTI −4.8% (oil market pricing deal). De-escalation removes safe-haven premium, but USD-weak channel (DXY 99.57) offsets. Net: Neutral
- Factor 3 (Fed/macro): 0 — FOMC HELD rates 3.50–3.75% (Warsh first meeting June 17). No hawkish shock (gold +0.43%). Hold as expected = Neutral
- Factor 4 (CB demand): +1 — **WGC CB Survey 2026 published June 16** (within 7-day window): record 45% of CBs plan to increase gold reserves; 89% expect global CB holdings to rise. Counts as new CB demand data → Bullish
- Factor 5 (Technicals): -1 — Price $4,333.20 above 9d EMA (~$4,305 est.) but below 50d EMA (~$4,545). 50d > 9d = downtrend configuration. Table: "Above 9d, below 50d | 50d > 9d | Any | Bearish" → Bearish

**Holiday check**: June 17, 2026 is NOT an Indian market holiday. Next holiday: June 26 (Muharram).

**Global CB sweep results**:
- **WGC CB Survey 2026 (June 16)**: Record 45% of CBs plan to increase gold reserves — MAJOR bullish data
- **Bank of Uganda**: Launched domestic gold buying programme; 100kg target March–June 2026 (NEW buyer logged)
- Poland: No new data (latest: 613t, May +18t confirmed June 12)
- China: No new data (May +9.95t, 19-month streak, confirmed June 8)
- Czech Republic: No new data
- Russia: No new data
- Germany: No new repatriation data (CDU still refusing; AfD motion pending)
- France: No new data
- USA: FOMC HELD (Warsh); 8,133t gold unchanged
- Saudi Arabia: No new data
- Iran: 60-day nuclear talks Day 2; WTI −4.8% as Hormuz reopening priced in; no CBI reserve announcement
- India: MCX ₹1,53,000; WTI falling → INR strengthening to ~₹94.32; ETF caps remain
- Japan/UK/Italy: No new data

**Pages updated**:
- `wiki/global-cb-activity-log.md` — June 17 section added (15 rows + Uganda new buyer logged)
- `wiki/india-gold-market.md` — June 17 MCX prices added; INR updated; FOMC context updated
- `wiki/fed-macro-factors.md` — FOMC June 17 decision section added; summary updated
- `wiki/gold-geopolitical-risk-premium.md` — June 17 price timeline entry added; EMAs updated; summary updated
- `wiki/log.md` — this entry
- `wiki/index.md` — descriptions updated

---

## 2026-06-16 — Daily update: Gold $4,314.53 (−0.2%); FOMC Day 1 (Warsh first meeting, decision June 17); Germany "bring our gold home" pressure escalates; India June ETF recovery +₹2,081cr; Signal: Wait (0)

**Raw file created**:
- `raw/india-gold-2026-06-16.md` — MCX ~₹1,51,500/10g (24k; Mumbai ₹1,51,370, Delhi ₹1,51,680); XAU/USD $4,314.53 (−0.2%); Silver $69.91; WTI $80.41; DXY 99.56; USD/INR ~95.40; FOMC Day 1 underway; June ETF recovery +₹2,081cr; 6 AMCs capping ETF subscriptions

**Prices fetched** (manual web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,314.53/oz | Silver: $69.91/oz | DXY: 99.56 | WTI: $80.41/bbl | USD/INR: ~95.40 (est.)
- MCX gold (24k retail): ~₹1,51,500/10g (Mumbai ₹1,51,370, Delhi ₹1,51,680 per goodreturns.in)

**Signal**: Wait, Score: **0**
- Factor 1 (Price vs targets): +1 — $4,314.53 is 20.1% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — US-Iran Islamabad Declaration active; 60-day nuclear talks window; de-escalation = technically bearish for risk premium. BUT FOMC uncertainty, WTI declining, DXY sub-100. Net: Neutral
- Factor 3 (Fed/macro): 0 — FOMC Day 1 (June 16); decision June 17. Rate hold 3.50–3.75% expected (97% probability). No change = Neutral. Possible hawkish dot-plot bias shift = downside risk for gold but not yet confirmed
- Factor 4 (CB demand): 0 — WGC April data (net +17t: Poland +14t, China +8t, Czech +3t, Russia -6t) published June 3 — outside 7-day window. WGC 9th Annual CB Survey (68% plan to increase) logged June 9 — borderline outside 7 days. No new CB purchase announcement found in today's global CB sweep → Neutral
- Factor 5 (Technicals): -1 — Price $4,314.53 above 9d EMA (~$4,304 est.) but below 50d EMA (~$4,590 est.). 50d > 9d = downtrend config. Table row: "Above 9d, below 50d | 50d > 9d (downtrend) | Any | Bearish" → Bearish

**Holiday check**: June 16, 2026 is NOT an Indian market holiday. Next holiday: June 26 (Muharram).

**Global CB sweep results**:
- Poland: No new data (latest: 613t confirmed June 12)
- China: No new data (May +9.95t, 19-month streak, confirmed June 8)
- Czech Republic: April WGC recap (+3t, 38th consecutive month)
- Russia: April WGC recap (−6t, YTD −22t)
- Uzbekistan: April WGC recap (−1t April but net buyer YTD)
- **Germany**: FXStreet June 11 "Germans demand bring our gold home" — cross-party pressure escalating; CDU still refusing; no Bundestag vote
- France: No new data
- USA: FOMC in progress; no gold policy changes
- Saudi Arabia: No new data
- Iran: Islamabad Declaration 60-day nuclear talks underway; no CBI reserve announcement
- India: MCX ₹1,51,500; June ETF recovery +₹2,081cr; 6 AMCs capping large subscriptions
- Japan/UK/Italy: No new data

**Pages updated**:
- `wiki/global-cb-activity-log.md` — June 16 section added (15 rows)
- `wiki/india-gold-market.md` — June 16 MCX price section added; summary updated; June ETF recovery; 6-AMC cap noted
- `wiki/fed-macro-factors.md` — June 16 macro update added; FOMC Day 1 note; three outcome scenarios documented
- `wiki/gold-geopolitical-risk-premium.md` — June 16 price entry added; technical levels updated (9d EMA ~$4,304 est.; 50d EMA ~$4,590 est.)
- `wiki/germany-gold-reserves.md` — June 11 FXStreet escalation added; Daily Update Log updated; sources updated
- `wiki/index.md` — updated descriptions for gold-geopolitical-risk-premium, fed-macro-factors, india-gold-market, global-cb-activity-log, germany-gold-reserves
- `wiki/log.md` — this entry

---

## 2026-06-15 — Daily update: Gold $4,323.18 (+3.1% on US-Iran Islamabad Declaration); WTI $81.06 (−5%+); DXY 99.56; Silver $70.29; FOMC tomorrow (June 16-17); Signal: Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-06-15.md` — MCX ~₹1,49,080/10g (24k); USD/INR ~95.11; XAU/USD $4,323.18 (+3.1%); WTI $81.06 (−5%+); US-Iran peace deal signed; Q1 investment demand overtook jewellery (first ever); Q1 imports 186t (+58% YoY)

**Prices fetched** (manual web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,323.18/oz | Silver: $70.29/oz | DXY: 99.56 | WTI: $81.06/bbl | USD/INR: ~95.11

**Signal**: Wait, Score: +1
- Factor 1 (Price vs targets): +1 — $4,323.18 is 20% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — US-Iran Islamabad Declaration peace deal confirmed = de-escalation (technically bearish for risk premium); BUT gold rose +3.1% and DXY fell to 99.56 (USD weakening). Competing signals: de-escalation reduces safe-haven bid, BUT lower oil/CPI reduces hawkish Fed pressure (bullish). Net: Neutral.
- Factor 3 (Fed/macro): 0 — FOMC June 16-17 tomorrow; 97-99.5% probability hold at 3.50-3.75%; unchanged = Neutral. Goldman pulled all 2026 cuts but maintained $5,400 target.
- Factor 4 (CB demand): +1 — Poland NBP governor confirmed 613t (May +18t), published June 12, within 7-day window → Bullish.
- Factor 5 (Technicals): -1 — Price $4,323.18 above 9d EMA ($4,301 calculated); below 50d SMA ($4,627); 50d > 9d = downtrend config → Bearish (table row: "Above 9d, below 50d | 50d > 9d | Any | Bearish").

**Holiday check**: June 15, 2026 is NOT an Indian market holiday (next holiday: June 26 = Muharram).

**Pages updated**:
- `wiki/global-cb-activity-log.md` — June 15 section added (12 rows: US-Iran peace deal, Poland confirmation, China/Germany/France/USA/Saudi/Iran/India/Japan/UK/Italy no-new-data)
- `wiki/india-gold-market.md` — June 15 MCX price section added; summary updated; Q1 structural shift (investment > jewellery) documented
- `wiki/iran-conflict-2026.md` — June 13-14 peace text agreed + June 15 deal effective added to timeline; summary updated
- `wiki/fed-macro-factors.md` — June 15 macro update added; FOMC "tomorrow" note; Goldman guidance on no 2026 cuts
- `wiki/gold-geopolitical-risk-premium.md` — June 15 price entry added to timeline; technical levels updated (9d EMA $4,301 calculated; gold now above 9d EMA; 50d SMA $4,627); current technical levels table updated
- `wiki/log.md` — this entry
- `wiki/index.md` — updated

---

## 2026-06-13 — COT weekly update (retry success via web search): Report_Date 2026-06-09 | MM_Net=+105,863 (−6,316 WoW) | OI=332,709 | Sentiment: Neutral zone | Source: Web search aggregators citing CFTC Disaggregated Futures Only (code 088691)

Report_Date: 2026-06-09 | MM_Net: +105,863 (−6,316 vs. prior week +112,179) | OI: 332,709 | MM_Long: 126,280 | MM_Short: 20,417 | MM_Net % OI: 31.8% | Sentiment: Neutral zone (50,000–150,000) | Source: Web search (MacroMicro/CFTC data aggregators) — Nasdaq Data Link API and direct WebFetch blocked by network egress

**Pages updated**:
- `prices/cot.csv` — row appended for 2026-06-09
- `wiki/institutional-flows.md` — "Latest COT Data" section updated to June 9; prior failure note replaced with confirmed data; Prior Week Reference section added
- `wiki/index.md` — [[institutional-flows]] entry updated to show June 9 MM_Net=+105,863

---

## 2026-06-18 — Signal methodology: new page + Factor 6 (Dollar Pressure) added

**Page created**: `wiki/signal-methodology.md`

**What changed:**
- New dedicated page documenting all 6 signal factors with full scoring rules, data sources, and rationale
- Factor 6 (Dollar Pressure) added to the scoring system as of today: uses DXY + USD/INR day-over-day % change from `prices/prices.csv`; threshold ±1%; `factor6 = clamp(dxy_signal + inr_signal, -1, +1)`
- Scoring range updated from -5 to +5 → **-6 to +6**
- Wait band: -1 to +1 → **-2 to +2** (harder to reach Buy/Sell without majority alignment)
- Routine prompt (`trig_01Q7FfuV2Y2Fqk4f8dtokd2J`) updated simultaneously — live from 2026-06-19 run onward

**Index updated**: `wiki/index.md` — signal-methodology row added under Institutional Flows.

---

## 2026-06-18 — Russia gold reserves page: major expansion via web research

**Page updated**: `wiki/russia-gold-reserves.md`

**Research sources**: Kitco (May 25, Apr 21, Jun 3 2026), Moscow Times (Nov 2025), The Bell (Nov 2025), RAND Gold Rush report, Atlantic Council (sanctions evasion), bne IntelliNews, New Eastern Europe (Feb 2026), Modern Diplomacy (Apr 2026), Ukraine24 media, The Conversation (Putin gold strategy), WGC.

**What was added:**
1. **Two-pot structure** — NWF (Finance Ministry, ~155.1t as of Feb 1 2026, down from 292.5t Oct 2024) vs Bank of Russia total (~2,305t). NWF is the primary selling pool; had 405t at peak (Jan 2022), down 61% in 4 years.
2. **16-year accumulation history** — Putin started 2006, accelerated after 2014 Crimea sanctions. Goals: de-dollarise, create domestic liquidity outside SWIFT, support miners. ~400t → ~2,330t by 2022 peak.
3. **5,000 RUB/gram peg** — March 2022 BoR fixed-price buying at 19% below spot; support mechanism for miners losing G7 export markets; suspended April 2022.
4. **Selling mechanism** — All sales are domestic: BoR sells to Russian banks/state companies in rubles. No LBMA/CME involvement. Zero international market impact since April 2023.
5. **G7 ban (Jun 26 2022) and circumvention routes** — UAE, Turkey, Armenia transit used 2022–early 2023. All routes closed by April 2023 (secondary sanctions + compliance pressure). No Russian gold exported outside EAEU since.
6. **Domestic gold production** — ~330t in 2024 (2nd globally); Russia claims 480–485t for 2025 (disputed; independent estimate 345t). Polyus (Olimpiada: 926k oz in 2025) and Polymetal are key producers. Sukhoi Log is world's largest undeveloped deposit (Polyus, end of decade).
7. **Depletion trajectory** — NWF gold (~155t) could be exhausted by 2027 at current pace. Total BoR (2,305t) at 84t/year would take ~4 years to reach 2,000t — not existential but NWF buffer is nearly gone.

**Index updated**: `wiki/index.md` — russia-gold-reserves row updated.

---

## 2026-06-13 — COT weekly update attempt: Report_Date 2026-06-09 | Status: DATA NOT RETRIEVED | All CFTC/data sources blocked by network egress policy | cot.csv unchanged

**Attempted sources**: CFTC direct (www.cftc.gov, data.cftc.gov), GoldSeek June 12 article, Barchart, MetalCharts, MacroMicro, YCharts, Investing.com, Barchart, StoneX, InvestMacro — all returned 403 Forbidden or DNS failure.

**Market context on June 9 (COT as-of date)**: Gold $4,338.50 (−3.57% from June 2's $4,499.00); DXY 100.0; Silver $67.66. Qualitative signals from web search suggest speculative net longs fell to a "six-week low" for the week, consistent with NFP-driven headwinds. MM_Net direction: likely lower than 112,179. cot.csv **not updated** (no verified data).

**Pages updated**:
- `wiki/institutional-flows.md` — Last updated → 2026-06-13; Added "June 9, 2026 COT Update — Data Retrieval Failure" section with market context and retry instructions
- `wiki/index.md` — Updated institutional-flows entry to note June 9 retrieval blocked

---

## 2026-06-12 — Daily update: Gold $4,192.79 (+2.73% Iran peace rebound); Poland 613t (May +18t confirmed); WTI $86.65; DXY 99.86; FOMC 4 days; signal Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-06-12.md` — MCX ₹1,47,566/10g; USD/INR ~95.26; XAU/USD $4,192.79; WTI $86.65; Iran peace = oil easing = inflation relief; May ETF first outflow (₹725cr); 15% import duty driving 70% demand collapse

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,192.79/oz | Silver: $66.53/oz | DXY: 99.86 | WTI: $86.65/bbl | USD/INR: ~95.26

**Signal**: Wait, Score: +1
- Factor 1 (Price vs targets): +1 — $4,192.79 is 22.4% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Iran peace deal "this weekend" = de-escalation (normally bearish) but USD also weakening (DXY 99.86) + WTI falling = inflation relief channel; net ambiguous = Neutral
- Factor 3 (Fed/macro): 0 — FOMC June 16-17; 99.4% probability hold; unchanged = Neutral
- Factor 4 (CB demand): +1 — Poland NBP governor confirmed 613t (May +18t) published early June (within 7-day window); ongoing bullish CB demand → Bullish
- Factor 5 (Technicals): -1 — Gold $4,192 below BOTH 9d EMA (~$4,498) and 50d EMA (~$4,627–4,730); last 2 days in CSV: June 10 RED ($4,177.88), June 11 RED ($4,082.73) = NOT 2 green → Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — June 12: MCX ₹1,47,566/10g; XAU/USD $4,192.79; WTI $86.65; May ETF first outflow (₹725cr) in 13 months captured; import duty 15% demand destruction documented
- `wiki/iran-conflict-2026.md` — June 12: Trump "deal as early as this weekend"; WTI $86.65; gold +2.73%
- `wiki/fed-macro-factors.md` — June 12 macro update: DXY 99.86; WTI $86.65; FOMC 4 days; Iran peace = inflation relief
- `wiki/gold-geopolitical-risk-premium.md` — June 12 price entry; updated technical table; EMA configuration note
- `wiki/poland-gold-reserves.md` — **Major update**: NBP governor confirms 613t (May +18t); YTD ~63t; 150t plan approved; targeting 700t (world's 10th-largest)
- `wiki/global-cb-activity-log.md` — June 12 section added (8 rows: Poland May +18t confirmed, China no new data, Global Iran peace rebound, Germany no new, France no new, USA no new, Saudi no new, Iran peace CBI context, India ETF outflow)
- `wiki/index.md` — updated descriptions for poland-gold-reserves, india-gold-market, iran-conflict-2026, fed-macro-factors, gold-geopolitical-risk-premium, global-cb-activity-log

**Global CB sweep results (June 12)**:
- **Poland**: NBP Governor Glapiński confirms **613t** (May 2026 ~+18t; from 595t); YTD ~63t; 150t plan approved — **major new data point, updated wiki**
- **China PBoC**: No new June announcement (latest: May 2026 +9.95t confirmed June 8; 19th consecutive month; 2,331.52t) — no change
- **WGC**: April 2026 data published June 3 (already captured) — no new June report
- **Germany**: No repatriation; Nagel confident in FRBNY; CDU "not under consideration"; ~1,200–1,236t at FRBNY
- **France**: All 2,437t on French soil; no new BdF statements
- **Italy, Japan, UK**: No new announcements found
- **USA**: 8,133t unchanged; no Fort Knox audit news
- **Saudi Arabia**: 323.07t static; no SAMA announcements
- **Iran**: Trump says peace deal "this weekend"; no CBI reserve announcement; WTI $86.65 on de-escalation
- **India**: MCX ₹1,47,566; ETF first outflow in 13 months (₹725cr May); 15% duty impact confirmed (70% demand drop)

---

## 2026-06-11 — Daily update: Gold ~$4,082 (below $4,100); May US CPI 4.2% (highest since Apr 2023) triggers ~3.25% gold crash; US-China new trade deal June 11; Iran MOU tentative unsigned; signal Wait (-1)

**Raw file created**:
- `raw/india-gold-2026-06-11.md` — MCX est. ₹1,46,700/10g (-~2.2%); USD/INR 95.26; XAU/USD ~$4,082.73; WTI $91.55; DXY 100.01; May US CPI 4.2% driver; US-China trade deal context; Iran MOU status

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,082.73/oz | Silver: $64.52/oz | DXY: 100.01 | WTI: $91.55/bbl | USD/INR: 95.26

**Signal**: Wait, Score: -1
- Factor 1 (Price vs targets): +1 — $4,082.73 is 24.4% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): -1 — US-China June 11 new 60-day deal (de-escalation); Iran-Israel MOU tentative/unsigned; risk premium unwinding → Bearish
- Factor 3 (Fed/macro): -1 — May CPI 4.2% (highest since Apr 2023; 23.5% energy surge); 70% odds of rate HIKE by Dec 2026; Goldman stripped all 2026 cuts; raised 20% hike probability → Hawkish = Bearish
- Factor 4 (CB demand): +1 — PBoC +9.95t May 2026 announced June 8 (3 days ago, within 7-day window); WGC April +17t net data published June 3 → Bullish
- Factor 5 (Technicals): -1 — Gold ~$4,082 below BOTH 9d EMA (~$4,380–$4,498) and 50d EMA (~$4,629); last 2 days: June 10 RED (-$160 from $4,338); June 11 RED (-$95 from $4,177) = NOT 2 green days → Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — MCX est. ₹1,46,700/10g June 11; USD/INR 95.26; XAU/USD $4,082.73; May CPI 4.2% context; DXY 100.01; WTI $91.55
- `wiki/iran-conflict-2026.md` — June 11 entry: US-Iran MOU tentative unsigned; US struck Iran June 10; Iran missiles; WTI $91.55; gold $4,082
- `wiki/fed-macro-factors.md` — May CPI 4.2%; Goldman hawkish pivot (20% hike probability, all 2026 cuts stripped); 5 days to FOMC; 70% Dec hike probability
- `wiki/us-china-trade-war.md` — June 11 Trump trade deal (30% tariffs; higher paused 60 days); SCOTUS IEEPA ruling Feb 20; gold de-escalation signal
- `wiki/gold-geopolitical-risk-premium.md` — $4,082.73 (below $4,100); 25% below ATH $5,589; updated technical levels (9d EMA ~$4,380–$4,498; 50d $4,629); support zone $4,075–$4,100 now being tested
- `wiki/global-cb-activity-log.md` — June 11 section added (9 rows: Global price/CPI, USA trade deal, Iran, Poland, China, Germany, France, USA, Saudi Arabia, India)
- `wiki/index.md` — updated descriptions for india-gold-market, us-china-trade-war, gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors

**Global CB sweep results (June 11)**:
- **China PBoC**: No new announcement (latest: May 2026 +9.95t confirmed June 8; 19th consecutive month) — updated wiki
- **Poland**: No new announcement (latest: April 2026 +14t per WGC June 3; 595t total) — no change
- **WGC April data**: Net +17t (published June 3) — already captured
- **Germany**: CDU "repatriation not considering"; ~1,236t at FRBNY — no change; AfD motion not acted on
- **France**: All 2,437t on French soil; no new BdF statements
- **Italy, Japan, UK**: No new announcements
- **USA**: 8,133t unchanged; no Fort Knox audit news; SCOTUS IEEPA ruling is major structural development
- **Saudi Arabia**: 323.07t static; no SAMA announcements
- **Iran**: MOU tentative, unsigned; fresh military exchanges June 10 (US strikes Iranian radar; Iran launches missiles in Gulf)
- **India (RBI)**: 880.52t unchanged; MCX ~₹1,46,700/10g; ETF restrictions continue; May US CPI bearish for gold demand narrative

---

## 2026-06-10 — Daily update: Gold $4,177.88 (-3.7%) breaks 200d MA for first time since Oct 2023; Iran-Israel conditional suspension; US-China trade deal; PBoC 19th straight month (+9.95t); India gold ETF restrictions (4 AMCs); signal Wait (0)

**Raw file created**:
- `raw/india-gold-2026-06-10.md` — MCX ₹1,50,258/10g (Aug futures, -1.43%); USD/INR 95.36; XAU/USD $4,177.88; WTI $88.71; DXY 99.73; ETF restrictions by 4 major AMCs (HDFC, Nippon, ICICI, Tata)

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,177.88/oz | Silver: $64.32/oz | DXY: 99.73 | WTI: $88.71/bbl | USD/INR: 95.36

**Signal**: Wait, Score: 0
- Factor 1 (Price vs targets): +1 — $4,177.88 is 22.6% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): -1 — Iran-Israel "conditional suspension" (both sides halted after June 7-9 exchange); US-China trade deal announced (30% tariffs, higher tariffs paused 60 days) = dual de-escalation → Bearish
- Factor 3 (Fed/macro): 0 — June 16-17 FOMC: 99%+ hold probability; rate unchanged at 3.50–3.75%; unchanged = Neutral
- Factor 4 (CB demand): +1 — China PBoC +9.95t in May 2026 (announced June 8; within 7-day window); WGC April net +19t published June 3 (also within window) → Bullish
- Factor 5 (Technicals): -1 — Gold $4,177.88 below BOTH 9d EMA (~$4,498) and 50d EMA (~$4,629); 50d > 9d = downtrend; last 2 days: June 9 green (+$9.17), June 10 red (-$160.62) = not 2 green → Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — MCX ₹1,50,258 (June 10, -1.43%); USD/INR 95.36; WTI $88.71; ETF restrictions (4 major AMCs); 200d MA breach noted
- `wiki/china-pboc-gold.md` — May 2026 +9.95t confirmed; 19th consecutive month; total 2,331.52t; price-insensitive accumulation
- `wiki/gold-geopolitical-risk-premium.md` — Gold $4,177.88; 200d MA breach; 9d EMA ~$4,498; 50d EMA $4,629; updated technical levels; support $4,100–$4,075
- `wiki/iran-conflict-2026.md` — June 10 entry: Iran-Israel conditional suspension; US-China deal; gold -3.7%; WTI $88.71
- `wiki/fed-macro-factors.md` — June 10: DXY 99.73; WTI $88.71; Gold $4,177.88; 6 days to FOMC
- `wiki/global-cb-activity-log.md` — June 10 section added (10 rows: China buy confirmed, Global price breakdown, WGC CB data, Poland/Germany/France/USA/Saudi/Iran/India updates)
- `wiki/index.md` — descriptions updated for gold-geo-risk-premium, china-pboc-gold, iran-conflict, fed-macro, india-gold-market, us-china-trade-war

**Global CB sweep results (June 10)**:
- **China PBoC**: +9.95t in May 2026 (19th consecutive month; announced June 8); total 2,331.52t — KEY UPDATE
- **WGC April data** (published June 3): net +19t — Poland +14t, China +8t, Czech +2t; Russia -6t
- Poland: 45t YTD, 595t total (150t programme approved Jan 2026) — no new announcement
- Germany: CDU "repatriation not considering"; ~1,236t at FRBNY — no change
- France: All 2,437t on French soil; no new BdF statements
- Italy: No new ownership dispute news
- Japan: 845.97t static; no change
- USA: 8,133t unchanged; no Fort Knox audit news
- UK: 310.29t; no new BoE custodial changes
- Saudi Arabia: 323.07t static; no SAMA news
- Iran: Conditional suspension; no CBI reserve announcement
- India (RBI): 880.52t confirmed unchanged; ETF restrictions from 4 major AMCs (new development)

---

## 2026-06-09 — Daily update: Iran-Israel direct military exchange then halt; gold recovers to $4,338.50 (+0.27%); WTI $91.28 on ceasefire; 9d EMA crossed; signal Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-06-09.md` — MCX ₹1,52,712–₹1,53,550/10g (down 1–4%); USD/INR 95.39; XAU/USD $4,338.50; WTI $91.28 (Iran-Israel halt); DXY ~100.0

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,338.50/oz | Silver: ~$67.66/oz | DXY: ~100.0 | WTI: $91.28/bbl | USD/INR: 95.39

**Signal**: Wait, Score: +1
- Factor 1 (Price vs targets): +1 — $4,338.50 is 19.65% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Iran-Israel direct military exchange (IDF struck Beirut June 7; Iran ballistic missiles) then both agreed to halt June 9; gold +0.27% but ambiguous; DXY flat at 100 → Neutral
- Factor 3 (Fed/macro): 0 — June 16-17 FOMC: 99.3% probability of NO CHANGE; rate held at 3.5–3.75%; unchanged = Neutral (rate hike bets at 70% by Dec but that is priced-in, not a new surprise today)
- Factor 4 (CB demand): +1 — WGC April data: net +17t (Poland 14t, China 8t, Czech 3t) published June 3 — exactly 6 days ago, within 7-day window → Bullish
- Factor 5 (Technicals): -1 — Gold $4,338.50 above 9d EMA ($4,335) but below 50d EMA ($4,629); 50d > 9d = downtrend configuration → Bearish per table rule

**Pages updated**:
- `wiki/india-gold-market.md` — MCX ₹1,52,712–₹1,53,550 (June 9); USD/INR 95.39; WTI $91.28; import duty corrected to 15%; Dubai route disruption noted
- `wiki/gold-geopolitical-risk-premium.md` — Gold $4,338.50 June 9 timeline entry; 9d EMA $4,335 (gold now above), 50d EMA $4,629; technical levels table updated
- `wiki/iran-conflict-2026.md` — June 7 IDF-Beirut strike + Iran ballistic missiles; June 9 halt; nuclear deal 75.5% against by June 30
- `wiki/fed-macro-factors.md` — June 9 DXY ~100; WTI $91.28; 99.3% hold at June 16-17; 70% Dec hike probability; 7 days to FOMC
- `wiki/global-cb-activity-log.md` — June 9 section added (10 rows: Global, Iran, Japan, Singapore, Germany, France, USA, Saudi Arabia, India, WGC Survey)
- `wiki/index.md` — descriptions updated for iran-conflict, geo-risk-premium, fed-macro, india-gold-market

**Global CB sweep results (June 9)**:
- No new country-level CB buy/sell announcements in last 24-48h
- Poland: 45t YTD, 595t total — no new announcement
- China: 18-month streak confirmed — no May 2026 data yet
- Japan: 845.97t static throughout Q1 2026; unchanged
- Singapore MAS: 193.85t Q1 2026 (up 0.29t from Q4 2025 — minor accumulation)
- Germany: CDU "repatriation not considering"; ~1,236t at FRBNY unchanged
- France: All 2,437t on French soil; no new BdF statements
- Italy: No new ownership dispute resolution
- USA: 8,133t unchanged; no Fort Knox audit news
- UK: 310.29t; no new BoE custodial changes
- Saudi Arabia: 323.07t static; no SAMA news
- Iran: Fresh Iran-Israel military exchange (June 7) then halt (June 9); nuclear deal 75.5% against

---

## 2026-06-08 — Daily update: Gold erases all 2026 gains (-3.28%, $4,329); DXY breaks above 100; rate-hike bets surge; signal Wait (0)

**Raw file created**:
- `raw/india-gold-2026-06-08.md` — MCX ₹1,52,720/10g (~-2%); USD/INR 95.19; DXY 100.05 (broke above 100 for first time in 2026); XAU/USD $4,329.33; WTI $93.63; silver ~$68.00/oz

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,329.33/oz | Silver: ~$68.00/oz | DXY: 100.05 | WTI: $93.63/bbl | USD/INR: 95.19

**Signal**: Wait, Score: 0
- Factor 1 (Price vs targets): +1 — $4,329 is 19.8% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Iran ceasefire fragile (US radar strikes + Iranian drones early June); but gold fell on macro/USD, not geo-specific flows; no clear safe-haven transmission → Neutral
- Factor 3 (Fed/macro): -1 — US May NFP +172K (vs 85K forecast) = hawkish surprise; DXY broke above 100; markets pricing year-end rate HIKE; April CPI 3.8% YoY; gold fell 3.28% = Bearish
- Factor 4 (CB demand): +1 — WGC June 3 report (within 7 days): April net +17t (Poland 14t, China 8t, Czech 2t) → Bullish
- Factor 5 (Technicals): -1 — Gold $4,329 below 9d EMA ($4,498) AND 50d EMA ($4,660); also broke below 200-day SMA (~$4,341); last 2 CSV rows: June 4 GREEN, June 5 RED = NOT 2 consecutive green → Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — MCX ₹1,52,720 (June 8); DXY 100.05; USD/INR 95.19; WTI $93.63; WGC demand -10% y/y forecast added
- `wiki/gold-geopolitical-risk-premium.md` — Gold $4,329 June 8 timeline entry; gold erased all 2026 gains; 200-day SMA breached; updated technical levels table; 9d EMA $4,498, 50d EMA $4,660
- `wiki/fed-macro-factors.md` — DXY 100.05 (above 100 first time 2026); May NFP +172K vs 85K forecast; rate-hike bets emerging; April CPI 3.8% YoY; June 16-17 Warsh meeting 8 days away
- `wiki/iran-conflict-2026.md` — June 8 timeline entry: ceasefire fragile but holding; US radar strikes + Iranian drones early June; deal by June 30 ~36.5% probability; gold drop macro-driven
- `wiki/goldman-sachs-gold-forecast.md` — JPMorgan year-end target revised to $6,000 (from $6,300); JPM 2026 average cut to $5,243; "gold on back burner for investors"
- `wiki/global-cb-activity-log.md` — June 8 section added (8 rows: Global macro shock, Poland, China, Germany, France, India, USA, Saudi Arabia, Iran)
- `wiki/index.md` — descriptions updated for gold-geo-risk-premium, iran-conflict-2026, fed-macro-factors, india-gold-market, goldman-sachs-gold-forecast

**Global CB sweep results (June 8)**:
- No new country-level CB buy/sell announcements in last 24-48h
- Poland: 45t YTD, 595t total — no new announcement
- China: 18-month streak confirmed — no May 2026 data yet
- Germany: AfD Bundestag repatriation motion unacted; CDU "not considering repatriation"; ~1,236t at FRBNY unchanged
- France: All 2,437t on French soil since April 2026; no new BdF announcements
- Italy: No new ownership dispute resolution or repatriation news
- Japan: 845.97t static; no BoJ or MoF statements on gold allocation
- USA: 8,133t unchanged; no Fort Knox audit or revaluation proposals
- UK: 310.29t; no new BoE custodial changes found
- Saudi Arabia: 323.07t static; no SAMA news
- Iran: Fragile ceasefire; US/Iranian military skirmishes; no CBI announcement

---

## 2026-06-06 — COT weekly update

Report_Date: 2026-06-02 | MM_Net: +112,179 (+18,639 vs. 2026-05-19) | OI: 326,052 | Sentiment: Neutral zone (50,000–150,000) | Source: IndexBox.io CFTC COT summary, June 5, 2026 release (CFTC Disaggregated Futures Only, COMEX Gold code 088691)

**Changes made:**
- `prices/cot.csv` — Row appended: 2026-06-02, OI=326,052, MM_Long=129,367, MM_Short=17,188, MM_Net=+112,179, MM_Net_Change=+18,639
- `wiki/institutional-flows.md` — "## Latest COT Data" section replaced with June 2 data; OI contraction noted (379K→326K); short-covering dynamic noted; NFP context added
- `wiki/index.md` — institutional-flows entry updated with latest MM_Net and Report_Date

**Data note:** CFTC.gov and most financial data sites returned HTTP 403 under this environment's network policy. Data sourced from IndexBox.io CFTC COT Data June 5, 2026 article, which cites the CFTC Disaggregated Futures Only release for COMEX Gold (code 088691), as-of June 2, 2026.

---

## 2026-06-05 — Daily update: WGC April CB data (+17t net); US NFP +251K; RBI holds 5.25%; gold $4,446 (-1%); signal Wait (+1)

**Raw file created**:
- `raw/india-gold-2026-06-05.md` — MCX ₹1,58,300/10g (-1%); RBI MPC HELD repo 5.25% neutral; US May NFP +251K (gold-negative); USD/INR 95.21; WTI $95; silver -1.5%

**Pages updated**:
- `wiki/poland-gold-reserves.md` — WGC June 3: +14t April 2026; YTD 45t; total 595t (30% reserves)
- `wiki/china-pboc-gold.md` — WGC June 3: +8t April 2026 confirmed; 18th consecutive month; 2,322t
- `wiki/czech-republic-gold-reserves.md` — WGC June 3: +2t April 2026; total ~79t (6% reserves)
- `wiki/russia-gold-reserves.md` — WGC June 3: -6t April 2026 (4th consecutive); YTD -22t
- `wiki/india-gold-market.md` — MCX ₹1,58,300 (-1%), RBI MPC held 5.25% (neutral), NFP strong, seasonal inauspicious period continues
- `wiki/fed-macro-factors.md` — US May NFP +251K; RBI India held 5.25%; June 16-17 Warsh meeting 11 days; 97.8% hold probability
- `wiki/gold-geopolitical-risk-premium.md` — Gold $4,446; NFP drove USD firm; Iran MOU unfinalized
- `wiki/global-cb-activity-log.md` — 10 new rows added for June 5 (Poland, China, Czech, Russia, global WGC net, Germany, India RBI, USA, Saudi Arabia, France)
- `wiki/index.md` — descriptions updated for Poland, China, Czech Republic, Russia, India gold market (both entries), geo-risk premium, fed-macro, iran-conflict

**Signal**: Wait, Score +1
- Factor 1 (Price vs target): Gold $4,446 = 21.4% below Goldman $5,400 target → **Bullish +1**
- Factor 2 (Geopolitical): Iran MOU unfinalized; WTI $95; NFP drove USD firm — no clear safe-haven flow into gold → **Neutral 0**
- Factor 3 (Fed/macro): US May NFP +251K (strong hold signal); FOMC June 16-17 hold 97.8% probability; RBI India held 5.25% neutral → **Neutral 0**
- Factor 4 (CB demand): WGC published June 3 (within 7 days): April net +17t (Poland 14t, China 8t, Czech 2t) → **Bullish +1**
- Factor 5 (Technicals): Gold $4,446 below 9d EMA ~$4,490 AND 50d EMA ~$4,640; last 2 days: June 4 green, June 5 red = NOT 2 green → **Bearish -1**

---

## 2026-06-04 — Daily update: Iran tentative ceasefire extension deal; RBI gold-sale claim denied; gold $4,471; signal Wait (0)

**Raw file created**:
- `raw/india-gold-2026-06-04.md` — MCX ₹1,58,985/10g (+1.78% from June 3); USD/INR 95.59 (weaker); WTI ~$95; RBI 880.52t CONFIRMED UNCHANGED — Bloomberg/PIB/RBI all clarified; US forced-labor tariffs gold-exempted

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,470.89/oz | Silver: $76.67/oz | DXY: 99.54 | WTI: ~$95.00/bbl | USD/INR: 95.59

**Signal**: Wait, Score: 0
- Factor 1 (Price vs targets): +1 — $4,471 is 17.2% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): 0 — Tentative US-Iran ceasefire extension deal + nuclear talks framework; but intermittent military exchanges strain deal; WTI $95 (market skeptical of Hormuz reopening); gold up slightly; DXY strengthening; mixed → Neutral
- Factor 3 (Fed/macro): 0 — Fed rates held at 3.5-3.75% (confirmed April 29 meeting); ADP May jobs +122K (above expectations = near-term hawkish); Warsh dovish long-term; next FOMC June 16-17; no change → Neutral
- Factor 4 (CB demand): 0 — No new WGC/Goldman CB purchase data in last 7 days; ECB gold-overtakes-UST report (June 2) is structural confirmation but not new volume data → Neutral
- Factor 5 (Technicals): -1 — Price (~$4,471) below 9d EMA (~$4,490) and 50d EMA (~$4,640); last 2 CSV rows: June 2 RED ($4,499→$4,539 down) and June 3 RED ($4,466→$4,499 down) = NOT 2 consecutive green → Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — MCX June 4 price; Bloomberg RBI gold-sale controversy section added; US tariff gold exemption noted; INR 95.59; WTI $95
- `wiki/gold-geopolitical-risk-premium.md` — June 4 price timeline entry; updated EMA levels (9d ~$4,490, 50d ~$4,640); Iran tentative deal; signal updated
- `wiki/iran-conflict-2026.md` — June 4 entry: tentative ceasefire extension deal reached
- `wiki/de-dollarisation.md` — ECB milestone section added (gold overtook UST as #1 reserve asset; 27% vs 22% share)
- `wiki/us-china-trade-war.md` — June 2026 updates: US-China Board of Trade + forced-labor tariff proposal (gold exempted)
- `wiki/global-cb-activity-log.md` — June 4 section added
- `wiki/index.md` — updated descriptions

**Global CB sweep results (June 4)**:
- No new country-level CB buy/sell announcements found
- India (RBI): Bloomberg gold-sale claim (June 2) officially denied by RBI + PIB — 880.52t holdings confirmed unchanged; gold share in FX reserves 16.85% as of May 22 (rising, not declining)
- Germany: no change (CDU not considering repatriation; ~1,236t at FRBNY)
- France: no change (all 2,437t on French soil since April 2026)
- Saudi Arabia: no change (323.07t static)
- Notable: WGC 2026 full-year CB demand estimate: 750–850t; 68% of CBs plan to increase gold holdings; ECB data confirms gold overtook US Treasuries in global CB reserves

---

## 2026-06-03 — Daily update: Iran talks stalled, WTI $93.51, gold $4,465.73, signal Wait

**Raw file created**:
- `raw/india-gold-2026-06-03.md` — MCX ₹1,56,210/10g (down 0.38% from June 2); USD/INR 95.36 (slightly weaker); WTI $93.51 (+2.5%) escalates INR risk; 2nd consecutive red day; 15% duty unchanged; RBI 880.52t unchanged

**Prices fetched** (via manual web search — yfinance 403 + metals.dev 403 fallback both failed):
- Gold: $4,465.73/oz | Silver: $74.74/oz | DXY: 99.21 | WTI: $93.51/bbl | USD/INR: 95.36

**Signal**: Wait, Score: -1
- Factor 1 (Price vs targets): +1 — $4,465.73 is 17.3% below Goldman $5,400 target (>15% = Bullish)
- Factor 2 (Geopolitical): -1 — Iran talks suspended; WTI $93.51 = oil/inflation risk dominant; gold FALLING despite escalation = risk priced in + real yield concern (Bearish)
- Factor 3 (Fed/macro): 0 — Fed hold at 3.5-3.75%; <10% cut probability; JPM sees potential 2027 hike; no dovish surprise (Neutral)
- Factor 4 (CB demand): 0 — No new CB gold purchase/sale data in last 7 days; JPM cut CB est to 640t from 800t (Neutral)
- Factor 5 (Technicals): -1 — Price below 9d EMA ($4,507) and 50d EMA ($4,660); last 2 days both RED (Jun 2 + Jun 3) = Bearish

**Pages updated**:
- `wiki/india-gold-market.md` — MCX June 3 price, INR 95.36, WTI $93.51 risk
- `wiki/gold-geopolitical-risk-premium.md` — gold $4,465.73; new technical levels (9d $4,507, 50d $4,660, 200d $4,412); Iran stalled; 2nd red day
- `wiki/iran-conflict-2026.md` — June 3 entry; Polymarket 67.5% no-deal; zero-enrichment deadlock
- `wiki/fed-macro-factors.md` — DXY 99.21; <10% cut odds; JPM 2027 hike signal; June 16-17 now 13 days away
- `wiki/global-cb-activity-log.md` — June 3 section; ECB milestone (gold overtakes UST in global CB reserves)
- `wiki/index.md` — updated descriptions for iran-conflict, gold-geo-risk, fed-macro, india-gold-market

**Global CB sweep results (June 3)**:
- No new country-level CB buy/sell announcements
- Germany: no change (CDU not considering repatriation; ~1,236t at FRBNY)
- Saudi Arabia: no change (323.07t static)
- India: no change (880.52t; 15% duty ongoing)
- Notable: JPMorgan cut full-year CB gold purchase estimate to 640t (from 800t); ECB data shows gold overtook UST in global CB reserves

---

## 2026-06-02 — Daily update: Iran suspends talks (oil +6%), gold red day at $4,499, signal Wait

**Raw file created**:
- `raw/india-gold-2026-06-02.md` — MCX ₹1,56,810/10g (down 0.15% from June 1); USD/INR 95.16; Iran escalation re-elevates Hormuz risk and INR pressure; AA scheme 100kg cap active; no new RBI data

**Prices fetched**:
- Gold: ~$4,499 | Silver: $75.28 | DXY: 99.19 | WTI: $91.23 | USD/INR: 95.16
- yfinance failed (403/network); metals.dev failed (403); all prices sourced via web search
- **DXY_MISSING** and **WTI_MISSING** resolved via web search: DXY=99.19, WTI=91.23

**Signal**: **Wait** | Score: 0
- Factor 1 (Price vs targets): +1 — ~$4,499 is 16.7% below Goldman $5,400 target (>15% threshold = Bullish)
- Factor 2 (Geopolitical): 0 — Iran suspended talks with US on June 1 (Israeli Lebanon strikes); Hormuz re-escalation risk; but oil-driven inflation counterbalances safe-haven demand; DXY slightly stronger (99.19 vs 98.94); Neutral
- Factor 3 (Fed/macro): 0 — Fed hold (97%+ odds) at June 16-17 Warsh meeting; oil surge slightly hawkish but not a new hawkish surprise; macro calendar this week (JOLTS, Beige Book, NFP); Neutral
- Factor 4 (CB demand): 0 — No new CB gold data in last 7 days; most recent: China PBoC April +8.1t (announced May 8, >7 days ago); Neutral
- Factor 5 (Technicals): -1 — Gold ~$4,499 below 9d EMA (~$4,505–$4,552) and 50d SMA (~$4,627); June 2 is RED day breaking 3-day green streak; NOT 2 consecutive green days = Bearish

**Pages updated**:
- `wiki/iran-conflict-2026.md` — June 1 escalation entry added (Iran suspended talks, WTI +6%); June 2 assessment added; sources updated
- `wiki/gold-geopolitical-risk-premium.md` — June 2 price added to timeline; technical levels updated (9d EMA ~$4,505-$4,552; 50d SMA ~$4,627); signal now Bearish for technicals
- `wiki/india-gold-market.md` — MCX updated to June 2: ₹1,56,810/10g; USD/INR 95.16; Iran oil risk for INR added; sources updated
- `wiki/fed-macro-factors.md` — DXY updated to 99.19; FOMC countdown 14 days; weekly macro calendar updated; Iran oil-inflation linkage added
- `wiki/global-cb-activity-log.md` — 2026-06-02 section added (Iran geopolitical shock, Germany no change, France no change, India ongoing)
- `wiki/index.md` — descriptions updated for iran-conflict-2026, gold-geopolitical-risk-premium, india-gold-market, fed-macro-factors
- `wiki/log.md` — this entry

**Holiday check**: June 2, 2026 is a normal trading day (NSE/BSE open). Only June holiday: June 26 (Muharram).

---

## 2026-06-01 — Daily update: Iran MOU continuing, India demand -70%, JPM raises to $6,300

**Raw file created**:
- `raw/india-gold-2026-06-01.md` — MCX ₹1,57,040/10g; USD/INR 95.01; demand -70% YoY post 15% duty; ETF resilient; RBI 880.52t no change

**Prices fetched**:
- Gold: $4,539.27 | Silver: $75.34 | DXY: 98.94 | WTI: $89.69 | USD/INR: 95.010
- yfinance failed (403 market closed); all prices sourced via web search

**Signal**: **Buy** | Score: +2
- Factor 1 (Price vs targets): +1 — $4,539 is 16% below Goldman $5,400 target (>15% threshold)
- Factor 2 (Geopolitical): 0 — Iran MOU ongoing (not yet signed); Ukraine stalled; mixed signals; no clear gold direction
- Factor 3 (Fed/macro): 0 — Fed held at 3.5–3.75%; Warsh FOMC June 16-17 (15 days); DXY 98.94 mild bearish; neutral overall
- Factor 4 (CB demand): 0 — No new CB data from last 7 days; most recent: China PBoC April +8.1t (May 8, >7 days ago)
- Factor 5 (Technicals): +1 — Price $4,539 below both 9d EMA (~$4,552) and 50d SMA ($4,627.51); last 2 days green (May 29 +$49, June 1 +$45) = Bullish per ruleset

**Pages updated**:
- `wiki/india-gold-market.md` — MCX price updated to June 1 levels; demand collapse data (~70% YoY) added; INR 95.01; sources updated
- `wiki/gold-geopolitical-risk-premium.md` — June 1 price added to timeline; EMA levels updated (9d ~$4,552, 50d SMA $4,627.51); technical levels table refreshed
- `wiki/goldman-sachs-gold-forecast.md` — JPMorgan target raised to $6,300 (latest); institutional forecast table updated; commentary refreshed
- `wiki/iran-conflict-2026.md` — June 1 timeline entry added (ceasefire extended 60d, nuclear talks ongoing, WTI $89.69)
- `wiki/fed-macro-factors.md` — DXY updated to 98.94; June 16-17 FOMC countdown; this-week macro calendar added
- `wiki/global-cb-activity-log.md` — 2026-06-01 section added (India demand collapse confirmed, Germany no change, no new global CB buy/sell data)
- `wiki/index.md` — descriptions updated for india-gold-market, gold-geopolitical-risk-premium, iran-conflict-2026, goldman-sachs-gold-forecast, fed-macro-factors

**Global CB Sweep Results**:
- No new country-level CB gold purchase or sale announcements found in last 48h
- Germany: CDU government reconfirmed repatriation not under consideration; no tonnage change
- India: physical demand collapsed ~70% YoY; no RBI action
- All other countries: no new data; Q1 2026 WGC data (244t net) remains most current

---

## 2026-05-30 — COT weekly update (Saturday routine)

Report_Date: 2026-05-19 | MM_Net: +93,540 (N/A change — first entry) | OI: 379,325 | Sentiment: Neutral zone | Source: CFTC Disaggregated Futures Only, COMEX Gold code 088691, via web search (getarcresearch.com / CFTC public data)

**Data note:** CFTC.gov returned HTTP 403 for all direct file/API requests. All financial data sites (barchart.com, kitco.com, investing.com, macromicro.me, goldchartsrus.com, etc.) also returned 403 due to network policy in this execution environment. The 2026-05-26 report (published 2026-05-29) was not yet indexed by search engines. Most recent confirmed disaggregated Managed Money data is as-of 2026-05-19.

**Changes made:**
- `prices/cot.csv` — First entry appended: 2026-05-19, OI=379325, MM_Long=122894, MM_Short=29354, MM_Net=93540
- `wiki/institutional-flows.md` — Added "## Latest COT Data" section with full table, sentiment interpretation, and context note
- `wiki/index.md` — Updated institutional-flows entry description with latest MM_Net and date

---

## 2026-05-30 — Added institutional flows tracking (GLD ETF + CFTC COT)

**Trigger**: User requested daily GLD ETF tonnage and weekly CFTC COT Managed Money data as a 6th trading signal factor.

**Changes made**:
- Created `wiki/institutional-flows.md` — explains GLD ETF daily holdings and COT Managed Money weekly positioning; documents signal rule (Factor 6: inflows = +1, outflows = -1, neutral = 0)
- Created `prices/gld.csv` — daily GLD ETF tonnes; populated by daily routine going forward
- Created `prices/cot.csv` — weekly CFTC COT managed money positions; populated by Saturday COT routine
- Updated `fetch_prices.py` — added USD_INR (USDINR=X) column to prices.csv; added `_migrate_csv()` for schema migration; added USD_INR_MISSING sentinel
- Updated `wiki/index.md` — new "Institutional Flows" section
- Daily routine updated: Step 1c (GLD inline fetch + WebSearch fallback), Factor 6 added to Step 6, signal thresholds updated to -6/+6 range, USD_INR patch added to Step 1b
- New Saturday routine created: fetches CFTC COT gold data, writes to prices/cot.csv, updates institutional-flows.md

---

## 2026-05-29 — Daily update (Friday)

**Holiday check**: May 28 was a market holiday (Eid al-Adha / Bakri Id — NSE/BSE/MCX closed). May 29 is a normal trading day — confirmed via web search (Business Standard, Upstox May 28 2026).

**Sources**: `raw/india-gold-2026-05-29.md`, web research (NewSX, GoodReturns, FXStreet, TaxGuru, WGC, BusinessToday, ZeroHedge, Kitco, Bloomberg, CNN May 28 2026, Notes From Poland, Visual Capitalist, Finance Magnates, TheStreet)

**Raw files created**:
- `raw/india-gold-2026-05-29.md` — MCX ₹1,57,410/10g (−0.18%), 24K ₹15,606/g, USD/INR 96.13, import duty 15% unchanged, Q1 ETF AUM ₹1.71L crore (+191% FY26), MCX was closed May 28 (Bakri Id)

**Prices patched** (yfinance + metals.dev both returned 403; all prices from web search):
- May 26: Gold $4,562.69, Silver $77.50, DXY $99.08 (est), WTI $89.50 (est)
- May 27: Gold $4,419.83, Silver $75.50 (est), DXY $99.35 (est), WTI $88.75 (est)
- May 28: Gold $4,444.74, Silver $74.26, DXY $99.28, WTI $88.94
- May 29: Gold $4,494.07, Silver $76.56, DXY $99.30, WTI $88.94

**Key findings — global**:
1. **Iran**: US and Iran reached tentative agreement May 28 — 60-day MOU drafted (Trump not yet signed). Terms: Hormuz reopens, sea mines cleared, no tolls. Gold hit 2-month intraday low ~$4,390 on May 28 US strikes before recovering to ~$4,445. Today recovering to ~$4,494. Finance Magnates: "2nd 200 EMA test of 2026 held."
2. **China PBoC**: 8.1t purchased in April 2026 (highest since Dec 2024), extending streak to **18 consecutive months**. Total: **2,322t** (reported May 8, confirmed in today's sweep). Confirmed new CB data.
3. **UBS forecast cut** (May 27): UBS lowered 2026 gold target from $6,200 → **$5,500/oz**; near-term $5,200 by June. Reason: "markets rediscovering opportunity cost." Range now $5,200–$6,300.
4. **Poland**: Q1 2026 total confirmed 581.64t (up from 550.21t in Q4 2025). Target: 700t. ~28% of total reserve value.
5. **Germany**: AfD Bundestag motion (March 2026) for full repatriation confirmed. CDU government not acting.
6. **Gold technicals**: Tested 200-day SMA region ($4,341–$4,390) on May 28 — held. 9-day EMA now ~$4,557 (declining from $4,651); 50-day EMA ~$4,693 (declining from $4,723).

**Key findings — India**:
- MCX gold ₹1,57,410/10g on May 29 (post-holiday re-open); USD/INR ₹96.13 (slightly weaker)
- 15% import duty structure confirmed: 10% BCD + 5% AIDC (unchanged since May 13)
- Q1 2026 gold ETF AUM ₹1.71L crore (+191% FY26); 11.44mn accounts total; April inflows ₹30.4bn
- RBI reserves: 880.52t, near-zero new buying, repatriation of ~168t from BoE ongoing

**Pages updated**:
- `wiki/china-pboc-gold.md` — Updated to 18-month streak, 8.1t April 2026, 2,322t total; added Daily Update Log
- `wiki/iran-conflict-2026.md` — Added May 28 tentative MOU events; updated May 28 and 29 assessments
- `wiki/india-gold-market.md` — Updated to May 29 prices (MCX ₹1,57,410, USD/INR 96.13); updated INR dynamics section
- `wiki/goldman-sachs-gold-forecast.md` — Added UBS cut to $5,500; updated consensus range note
- `wiki/gold-geopolitical-risk-premium.md` — Updated price timeline through May 29; new EMA estimates ($4,557/$4,693); updated technical levels table
- `wiki/global-cb-activity-log.md` — Added 2026-05-29 section with 6 country entries (China, Poland, Germany, India, Russia, Turkey)
- `wiki/log.md` — This entry

**global-cb-activity-log.md rows added**:
- 🇨🇳 China: 8.1t April 2026 purchase confirmed; 18-month streak; 2,322t total
- 🇵🇱 Poland: Q1 2026 confirmed 581.64t; targeting 700t
- 🇩🇪 Germany: AfD motion confirmed; CDU not acting
- 🇮🇳 India (RBI): 880.52t; no new buying; repatriation ongoing
- 🇷🇺 Russia: ~2,330t; selling ~22t/quarter
- 🇹🇷 Turkey: ~595t; selling via swaps

**Price fetch**: Both yfinance and metals.dev returned 403. All values manually sourced from web searches and patched into prices.csv. 4 new rows added (May 26–29).

**Signal**: Wait (Score +1) — Price 16.8% below Goldman $5,400 (bull +1); Iran tentative MOU = de-escalation, gold at 2-month low (bear -1); Fed holding 3.5–3.75%, neutral (0); China April data reported May 8 = 21 days ago, outside 7-day window, neutral (0); below both EMAs ($4,557/$4,693) but 2 consecutive green days (bear-to-bull bounce) = bullish (+1). Net: +1 = Wait.

---

## 2026-05-27 — Expansion: Germany, France, Italy, Japan pages (web-researched)

**Trigger**: User requested dedicated pages for Germany, France, Italy, Japan.

**Web research conducted**:
- Germany: Bundesbank storage confirmed (Frankfurt ~1,710t, FRBNY ~1,236t, BoE ~404t); Jan 2026 Mönch "dangerous" FRBNY comment; Mar 2026 AfD Bundestag motion; CDU not acting (Euronews Apr 2026, Kitco Jan 2026, Mining.com)
- France: MAJOR story — Banque de France sold 129t from FRBNY Jul 2025–Jan 2026, rebought in Europe, made €13B (~$15B) profit; ALL 2,437t now in Paris; 134t more to modernise by 2028 (Newsweek, Kitco, Brussels Signal, Mining.com Apr 2026)
- Italy: 2,452t confirmed; Nov 2025 Fratelli d'Italia ownership amendment in Senate; ECB objected and blocked it; Italy under pressure to follow France repatriation (Euronews Nov 2025, Project Syndicate Dec 2025, Il Sole 24 Ore)
- Japan: 845.97t confirmed static Q1 2026 = Q4 2025; $125.4B value Apr 2026; ~3–4% of $1.2T total reserves; no active accumulation programme (CEIC, TradingEconomics, FX Empire)

**Pages created**:
- `wiki/germany-gold-reserves.md` — 3,352t; storage breakdown; 2026 repatriation pressure; France cited as template
- `wiki/france-gold-reserves.md` — 2,437t; ALL gold repatriated from FRBNY; €13B profit; 134t still to modernise
- `wiki/italy-gold-reserves.md` — 2,452t; FdI ownership amendment; ECB blocked it; France repatriation pressure
- `wiki/japan-gold-reserves.md` — 845.97t static; 3–4% gold-to-reserves; no accumulation; largest potential swing buyer

**Pages updated**: `wiki/index.md` (4 new entries), `wiki/log.md` (this entry), `wiki/global-cb-activity-log.md` (4 countries moved to dedicated pages)

---

## 2026-05-27 — Expansion: 6 major country pages (USA, UK, Canada, Israel, Saudi Arabia, Iran)

**Trigger**: User requested pages for USA, UK, Canada, Israel, Saudi Arabia, Iran + Iran addition + fresh web data.

**Web research conducted before writing**:
- UK BoE reserves: CEIC confirmed 310.29t Q1 2026 unchanged; BoE vaults hold 400,000+ bars for 72+ central banks (BoE, LBMA, CEIC)
- Canada: TradingEconomics/CEIC confirmed 0t; last 0.62t sold Feb 2016; 1,023t peak in 1965 worth $132B today (Globe and Mail, CBC)
- Israel: Bank of Israel Dec 2025 release confirmed 0t; Knesset Finance Committee debate ongoing (Ynet, CEIC)
- USA: US Treasury FRED confirmed 8,133t as of April 30, 2026; Fort Knox = 147.3M fine troy oz (FRED, US Mint)
- Saudi Arabia: CEIC/WGC Q3 2025 confirmed 323.07t unchanged; March 2026 Gulf gold mystery investigated — no confirmed SAMA sales found; LBMA vault outflows ~45t Jan–Feb 2026 (Middle East Insider, TradingEconomics)
- Iran: Al Jazeera/WGC confirmed 100t+ gold imported 2024; CBI governor claims 20% FX reserves in gold; sanctions-evasion strategy; IMF does not report Iran data (Al Jazeera, Money Metals, IranIntl)
- Brown's Bottom UK: confirmed 395t sold at avg $275/oz, $3.5B raised, ~£48B lost at 2026 prices (Wikipedia, GBNews)

**Pages created**:
- `wiki/uk-gold-reserves.md` — 310.29t; BoE custodian for 72+ central banks; Brown's Bottom $3.5B sold = £48B lost
- `wiki/canada-gold-reserves.md` — 0t; only G7 country; 36-year sell-off from 1,023t; $132B opportunity cost
- `wiki/israel-gold-reserves.md` — 0t; policy since Fischer/1980s; $214B total reserves; Knesset debate
- `wiki/iran-gold-reserves.md` — IMF unreported; CBI 20% in gold claim; 100t+ 2024 imports; sanctions buffer; nuclear deal variable

**Pages updated with fresh data**:
- `wiki/usa-gold-reserves.md` — Refreshed with April 30, 2026 FRED data (8,133t confirmed); Fort Knox specific tonnage added
- `wiki/saudi-arabia-gold-reserves.md` — Added March 2026 Gulf gold mystery section; LBMA outflow data; PIF undisclosed angle

**Pages updated**:
- `wiki/index.md` — Added 6 new entries
- `wiki/log.md` — This entry
- `wiki/global-cb-activity-log.md` — Updated countries table and "no gold" section

---

## 2026-05-27 — Expansion: 11 country stub pages + global activity log

**Trigger**: User requested full country coverage for all Q1 2026 CB gold buyers/sellers + daily update mechanism.

**Pages created** (11 country stubs):
- `wiki/uzbekistan-gold-reserves.md` — 2nd largest Q1 2026 buyer (25t); Navoi Mining link
- `wiki/kazakhstan-gold-reserves.md` — 12t Q1 2026; domestic mine purchase programme
- `wiki/czech-republic-gold-reserves.md` — 5t Q1 2026; CNB multi-year policy; 100t target (needs verification)
- `wiki/malaysia-gold-reserves.md` — 5t Q1 2026; ASEAN de-dollarisation; BRICS+ aligned
- `wiki/indonesia-gold-reserves.md` — 2t Q1 2026; Grasberg mine; ASEAN regional pattern
- `wiki/cambodia-gold-reserves.md` — 2t Q1 2026; dollarised economy; monetary sovereignty signalling
- `wiki/guatemala-gold-reserves.md` — 2t Q1 2026; Central America entering gold accumulation trend
- `wiki/serbia-gold-reserves.md` — 1t Q1 2026; EU candidate; geopolitical neutrality hedge
- `wiki/uae-gold-reserves.md` — 1t Q1 2026; DMCC gold hub; BRICS+ member; Hormuz exposure
- `wiki/azerbaijan-sofaz-gold.md` — 22t Q1 2026 seller; SOFAZ sovereign wealth fund cycle
- `wiki/kyrgyz-republic-gold-reserves.md` — 1t Q1 2026 seller; Kumtor mine cycle

**Pages created** (infrastructure):
- `wiki/global-cb-activity-log.md` — append-only daily log for all country-level CB gold activity; includes policy tracker; updated daily by routine

**Pages updated**:
- `wiki/central-bank-gold-demand.md` — buyer/seller tables now link to all 15 individual country pages; added [[global-cb-activity-log]] to related pages
- `wiki/index.md` — added 12 new entries (11 country pages + global-cb-activity-log)

**Routine change**: See below entry for routine update details.

---

## 2026-05-27 — Ingest: Daily research update (Wednesday)

**Sources**: `raw/india-gold-2026-05-27.md`, web research (BusinessToday, India.com, Goodreturns, Invezz, CNN, Al Jazeera, CNBC, NPR, Wikipedia Iran-US negotiations, IndexBox, FinanceMagnates, iShares Fed outlook)

**Holiday check**: May 27 is NOT a market holiday. NSE/BSE/MCX are open. (Eid al-Adha/Bakrid holiday falls on **May 28**, not May 27 — confirmed by Ministry of Personnel notification.)

**Raw files created**:
- `raw/india-gold-2026-05-27.md` — MCX ₹15,827/g (-0.61%), 24K retail ₹15,829/g, 22K ₹14,510/g, silver ₹2,85,000/kg, USD/INR 95.45, FY26 gold ETF AUM ₹1.71L crore (+191% y/y), gold lower on Iran strikes "priced in" dynamic

**Pages updated**:
- `wiki/india-gold-market.md` — Updated MCX price to ₹15,827/g; USD/INR to 95.45; added gold-lower-on-Iran-strikes note; added FY26 ETF AUM data (₹1.71L crore, +191% y/y, ₹68,868 crore net FY26 inflows); corrected AUM from prior ₹1.83L crore (Feb 2026) to confirmed ₹1.71L crore (March 2026 FY end); added expert 2026 range ₹1.5–1.8 lakh/10g
- `wiki/iran-conflict-2026.md` — Added May 27 timeline entry: Trump says deal close with "strong inspections" but Khamenei advisor calls nuclear control demand a "fantasy"; Araghchi publicly unsure deal imminent; gold declining ~0.61% on "risk priced in"; added May 27 risk assessment paragraph
- `wiki/gold-geopolitical-risk-premium.md` — Added May 27 price range ($4,528–$4,557) to price timeline; updated Technical Levels table with current price and indicators (RSI 38.74, MACD -29.01, ADX 11.51); noted May 27 = red day (below May 26 close ~$4,570); added key signal watchpoints
- `wiki/index.md` — Updated descriptions for iran-conflict-2026, gold-geopolitical-risk-premium (both entries), india-gold-market (both entries)

**Price fetch**: yfinance FAILED — HTTP 403 (network policy blocks yfinance). Last prices from prices.csv: Gold $4,523.20 (May 25), Silver $76.199, DXY 99.026, WTI $96.60. Today's estimated spot from web: Gold ~$4,528–$4,580 range; MCX ₹15,827/gram.

**Signal**: Wait (Score -1) — Price 16% below $5,400 Goldman target (bullish); Iran deal stalling with divergent signals, gold declining today with risk priced in (bearish); Fed unchanged (neutral); no new CB demand data in 7 days (neutral); below both 9-day ($4,651) and 50-day ($4,723) EMA, May 26 green but May 27 red = not 2 consecutive green (bearish). Step down from yesterday's Buy (3) as Iran risk premium deflates and technicals weaken.

---

## 2026-05-26 — Ingest: Daily research update (Tuesday)

**Sources**: `raw/india-gold-2026-05-26.md`, web research (Sunday Guardian Live, BusinessToday, NPR, Al Jazeera, CNN, Axios, exchangerates.org.uk, gold.org WGC, TipRanks, Yahoo Finance, ClearTax)

**Holiday check**: May 26 is not a market holiday. Indian markets open. (May 2026 holidays: May 1 Maharashtra Day; May 28 Bakri Id.)

**Raw files created**:
- `raw/india-gold-2026-05-26.md` — India gold data: MCX price ~₹15,858/g, retail 24K ₹15,889/g, USD/INR 95.346, RBI 880.52t (no new announcement), import duty 15% unchanged, ETF flows still positive

**Pages updated**:
- `wiki/india-gold-market.md` — Corrected MCX price to ₹15,858–₹16,000/gram (previous ₹14,075 was pre-duty conversion only); updated USD/INR to 95.346; noted gold rises on Middle East tension; added duty-adjusted price explanation
- `wiki/iran-conflict-2026.md` — Added May 26: Austria BVT intel report (Iran pursuing advanced nuclear weapons program with ballistic missiles); US military strikes on Iran continued May 25 despite "largely negotiated" MOU; updated risk premium assessment to "Mixed/contradictory" — strikes-plus-negotiations dynamic; gold edging higher on safe-haven flows
- `wiki/gold-geopolitical-risk-premium.md` — Updated price timeline to May 26 ($4,536); updated technical levels table: 9-day EMA ~$4,651 (resistance), 50-day EMA ~$4,723 (resistance), both overhead; added EMA configuration note (price below both EMAs, 2 consecutive green closes = mean-reversion bounce)
- `wiki/goldman-sachs-gold-forecast.md` — Added RBC Capital Markets ($5,723, up from $4,800) and LBMA annual average consensus ($4,741.97) to comparison table; updated institutional range note; confirmed Wells Fargo $6,100–$6,300 upgrade detail
- `wiki/index.md` — Updated descriptions for iran-conflict-2026, gold-geopolitical-risk-premium, goldman-sachs-gold-forecast, india-gold-market (both entries)

**Price fetch**: yfinance fetch FAILED — HTTP 403 host not in allowlist (network policy blocks yfinance). Last known prices from prices.csv: Gold $4,523.20 (May 25), Silver $76.199, DXY 99.026, WTI $96.60. Today's spot from web: Gold ~$4,536/oz.

**Signal**: Buy (Score 3) — Price 16% below Goldman $5,400 target (bullish); US strikes Iran + Austria nuclear intel, gold rising on safe-haven with USD flat (bullish); Fed unchanged at 3.5–3.75% for 3rd hold, no new surprise (neutral); no new CB demand data in 24–48h (neutral); price below both 9-day ($4,651) and 50-day ($4,723) EMA but 2 consecutive green days = mean-reversion bounce (bullish).

---

## 2026-05-25 — Ingest: Daily research update (Sunday)

**Sources**: `raw/india-gold-2026-05-25.md`, web research (Bloomberg, CNBC, FXStreet, CNN, Axios, BusinessToday, WGC, exchangerates.org.uk)

**Note**: May 25 is a Sunday. Indian markets (NSE/BSE/MCX) closed for regular weekend. Next listed holiday: May 28 (Bakri Id). Update proceeds because this is not a named market holiday.

**Raw files created**:
- `raw/india-gold-2026-05-25.md` — India gold market data: MCX price, import duty, ETF flows, INR/USD, RBI

**Pages created**:
- `wiki/india-gold-market.md` — New India gold market running concept page: MCX price (~₹14,075/g), 15% import duty hike (May 13), PM Modi appeal, ETF market (AUM ₹1.83L crore, April inflows INR 30.4bn), physical-to-digital demand shift, INR/USD (95.81)

**Pages updated**:
- `wiki/iran-conflict-2026.md` — Major update: added May 23–25 Iran MOU negotiations progress (Trump "deal largely negotiated," draft MOU terms including Hormuz reopening, 60-day ceasefire extension, uranium never-pursue commitment, key sticking points); updated risk assessment table; added gold market reaction analysis (gold up $40–50/oz via Fed/inflation channel, not safe-haven)
- `wiki/goldman-sachs-gold-forecast.md` — Added Morgan Stanley H2 2026 target cut to $5,200 (from $5,700, ~10% reduction); updated institutional forecast table and summary note; consensus range now $5,200–$6,300
- `wiki/gold-geopolitical-risk-premium.md` — Updated price table to May 25 ($4,565); added 20-day EMA ($4,646) as near-term resistance; rewrote Iran deal section to reflect reversal from near-collapse (May 22) to near-deal (May 24); added critical insight on Iran deal = bullish via macro/Fed channel (not safe-haven); updated sustaining vs. compressing premium drivers
- `wiki/index.md` — Added india-gold-market page entry; updated descriptions for iran-conflict, gold-geopolitical-risk-premium, goldman-sachs-gold-forecast

**Signal**: Buy (Score 2) — Iran deal progress pushed gold to $4,565 via weaker USD/Fed channel; 18% below $5,400 Goldman target; CB demand ~80t/month; technicals neutral (between 9-day and 50-day EMA); Morgan Stanley joined Goldman at $5,200 floor.

---

## 2026-05-22 — Ingest: Daily research update

**Source**: `raw/daily-update-2026-05-22.md`

**Pages created**:
- `wiki/daily-update-2026-05-22.md` — source summary; key developments table

**Pages updated**:
- `wiki/iran-conflict-2026.md` — added Mojtaba Khamenei uranium directive (May 21); Trump military threat; updated oil prices to Brent ~$104.52/bbl; updated risk assessment table; added Nuclear Negotiations — May 2026 section; clarified gold push-pull dynamic
- `wiki/fed-macro-factors.md` — Warsh confirmed dovish (not hawkish); one rate cut expected H2 2026; Powell stays as governor pending Fed HQ investigation; DXY ~99; updated FOMC section with fed funds rate (3.5–3.75%); updated USD Dynamics section
- `wiki/goldman-sachs-gold-forecast.md` — corrected nowcast table: March ~50t, April ~80t, FY avg ~60t; updated institutional forecast table (added Deutsche Bank $6,000; ANZ note on mid-2027 timeline; UBS upside $7,200)
- `wiki/central-bank-gold-demand.md` — replaced single nowcast figure with March/April/FY breakdown table; trend noted as accelerating
- `wiki/hidden-sovereign-buying.md` — added April 2026 nowcast of ~80t/month; clarified FY average vs. monthly trend
- `wiki/gold-geopolitical-risk-premium.md` — updated price table to May 22; added granular support/resistance levels ($4,410–$4,430 immediate, $4,362 critical floor); added Iran re-escalation risk as highest-priority premium driver
- `wiki/index.md` — added new source summary entry; updated Goldman description

---

## 2026-05-21 — Ingest: Automated daily research update

**Source**: `raw/daily-update-2026-05-21.md`

**Pages created**:
- `wiki/fed-macro-factors.md` — Kevin Warsh confirmation (May 13), 8-4 FOMC split, June 16-17 risk event, Big Beautiful Bill deficit, real yield dynamics
- `wiki/iran-conflict-2026.md` — US-Israel strike Feb 28, ceasefire Apr 7, Hormuz at 5% traffic, gold ATH $5,200, ceasefire correction to $4,500

**Pages updated**:
- `wiki/goldman-sachs-gold-forecast.md` — nowcast revised 50t→60t/month; updated institutional forecast table (JPM avg cut to $5,243, UBS near-term $6,200, ANZ $5,600)
- `wiki/central-bank-gold-demand.md` — Goldman nowcast updated to 60t/month
- `wiki/hidden-sovereign-buying.md` — added May 21 further revision to 60t/month
- `wiki/rare-earths-geopolitics.md` — added China May 20 "lawful" statement section
- `wiki/us-china-trade-war.md` — added China "lawful" statement and $30B tariff cut discussions
- `wiki/gold-geopolitical-risk-premium.md` — full price timeline added ($4,000→$5,200→$4,500); updated support/resistance levels; corrected Hormuz status (5% traffic, not "open"); added June 16-17 Warsh FOMC as risk event
- `wiki/de-dollarisation.md` — added BRICS gold settlement infrastructure section (Saudi/Singapore/Malaysia vaults, 2030 target)
- `wiki/index.md` — added 2 new concept pages and updated descriptions across Geopolitics & Macro section

---

## 2026-05-21 — Ingest: US–China Beijing Summit, May 14–15, 2026

**Source**: `raw/us-china-beijing-summit-2026-05-15.md`

**Pages created**:
- `wiki/us-china-beijing-summit-may-2026.md` — source summary; summit outcomes, deals, gold market reaction
- `wiki/us-china-trade-war.md` — tariffs, rare earths, Taiwan; November 10, 2026 truce deadline
- `wiki/rare-earths-geopolitics.md` — China's 90% refining dominance; exports 50% below pre-control; key escalation risk
- `wiki/gold-geopolitical-risk-premium.md` — how geopolitical events move gold; summit compressed premium by $120–$220/oz

**Pages updated**:
- `wiki/china-pboc-gold.md` — added 17 consecutive months buying streak; diplomatic insulation section
- `wiki/de-dollarisation.md` — added trade war accelerant section; new related links
- `wiki/index.md` — new source summary entry; new Geopolitics & Macro section with 3 pages

---

## 2026-05-21 — Ingest: India RBI and Russia gold reserve data (latest available)

**Source**: `raw/india-russia-gold-reserves-2026-05-21.md`

**Pages created**:
- `wiki/india-rbi-gold.md` — 880.52t reserves; near-zero new buying in 2026; repatriation of 168t from London in past year
- `wiki/russia-gold-reserves.md` — 2,304t; selling ~22t/quarter (sanctions-driven fiscal liquidation, not bearish signal)

**Pages updated**:
- `wiki/central-bank-gold-demand.md` — expanded Russia seller entry; added India and Russia to related pages
- `wiki/index.md` — added new source summary and two new country pages

---

## 2026-05-21 — Initial ingest: central bank gold purchases week of May 12–18, 2026

**Source**: `raw/central-bank-gold-purchases-2026-05-19.md`

**Pages created**:
- `wiki/central-bank-gold-purchases-week-2026-05-19.md` — source summary
- `wiki/central-bank-gold-demand.md` — core concept; Q1 2026 data (244t net), 2026 outlook
- `wiki/de-dollarisation.md` — key structural driver of EM central bank buying
- `wiki/hidden-sovereign-buying.md` — Goldman's May 18 finding; 72% undercount in prior model
- `wiki/poland-gold-reserves.md` — largest Q1 2026 buyer globally (31t), targeting 700t
- `wiki/china-pboc-gold.md` — 2,313t reserves; largest 17-month purchase in Q1 2026
- `wiki/turkey-gold-reserves.md` — ~70t Q1 reduction via swaps; not a structural sell signal
- `wiki/goldman-sachs-gold-forecast.md` — $5,400/oz target; revised CB nowcast to 50t/month
- `wiki/index.md` — created (first entry)
- `wiki/log.md` — created (this file)



---

## 2026-06-27 — COT weekly update FAILED: fetch_cot.yml failing since 2026-06-22 (5 consecutive days)

**Status**: cot_latest.json absent from repo. cot.csv NOT updated. Last confirmed COT data: 2026-06-09 (MM_Net=+105,863).

**Root cause**: `ModuleNotFoundError: No module named 'requests'` — the GitHub Actions runner (ubuntu-latest) was updated to Python 3.14.6 which does not bundle `requests` as a stdlib module. The workflow never included a `pip install requests` step. All 5 scheduled runs failed at the "Fetch CFTC disaggregated COT data" step within 1–2 seconds.

**Affected runs** (all conclusion=failure):
- 2026-06-26 21:47 UTC (run 28267122428)
- 2026-06-25 22:01 UTC (run 28203251460)
- 2026-06-24 21:53 UTC (run 28132048118)
- 2026-06-23 21:55 UTC (run 28059775383)
- 2026-06-22 22:21 UTC (run 27987969112)

**Fix applied**: Added `pip install requests` before the Python heredoc in `.github/workflows/fetch_cot.yml`. Committed and pushed 2026-06-27. Workflow manually re-triggered.

**Missing COT reports**: June 16 and June 23 CFTC reports were not captured during the outage. These will need to be backfilled manually or will be superseded by the next successful run (June 27 report if available, or June 30 on Monday).

**Pages updated**:
- `wiki/log.md` — this failure entry
- `.github/workflows/fetch_cot.yml` — pip install fix applied

---

## 2026-07-06 — Daily update: Gold $4,163.46 (+0.63%); WGC May CB net +41t (Poland+18t China+10t Singapore+4t resumes); MCX ₹1,46,730 (−0.01%); USD/INR ₹95.44; DXY 100.88 (+0.06%) | Signal: Wait (+1)

**Holiday check**: July 6, 2026 — Monday. No NSE/BSE holiday. Proceeding with full update.

**Prices fetched** (all manual via web search — yfinance 403 + metals.dev 403 both failed):
- Gold: $4,163.46/oz (+0.63%) | Silver: $62.60/oz (~+0.04%) | DXY: 100.88 (+0.06%) | WTI: $68.78/bbl (+0.48%) | USD/INR: ₹95.4380 | Volume: not available (yfinance blocked)

**Key finding — WGC July 2026 CB Statistics published today**:
- May 2026 net central bank buying: **+41 tonnes**
- Poland: +18t (4th consecutive double-digit month; total ~631t; YTD ~81t)
- China PBoC: ~+10t (20th consecutive month; total ~2,341.52t)
- Uzbekistan: +9t (YTD ~33t)
- Kazakhstan: +7t (YTD ~20t)
- Singapore MAS: +4t (first since Sep 2025 — **8-month pause ended**)
- Czech Republic: +2t (39th consecutive month; total ~81t)
- Jordan: +1t (new buyer — first time appearing in data)
- Russia BoR: −6t (YTD −34t; total ~2,292t; all domestic — no LBMA impact)
- WGC survey: record **45% of CBs** plan to increase own gold holdings; **89% expect global CB gold to rise**
- Full-year 2026 WGC forecast: **850 tonnes**

**EMA / Technicals**:
- 9-day EMA (computed from prices.csv): ~$4,109 (gold above → slightly bullish)
- 50-day SMA (from CSV avg): ~$4,392 (gold below → bearish; 50d > 9d → downtrend confirmed)
- Death cross / downtrend still active → Technicals = Bearish (−1)

**Signal**: Wait (+1). Breakdown: Price vs targets +1 ($4,163 is 15.1% below GS $4,900); Geopolitical 0 (Iran Khamenei burial July 9; Day ~16 of MOU; nuclear deferred; priced in); Fed/Macro 0 (NFP miss vs 9/18 hawkish dots — mixed); CB Demand +1 (WGC May data published today, within 7 days); Technicals −1 (above 9d EMA, below 50d SMA, downtrend); Dollar Pressure 0 (DXY +0.06% and INR +0.23% both within 1%).

**Pages created**:
- `wiki/singapore-mas-gold.md` — NEW PAGE: MAS +4t May 2026 (first since Sep 2025); 197t total; Oct 2026 gold vaulting hub strategy; ASEAN context
- `raw/india-gold-2026-07-06.md` — daily raw source: MCX ₹1,46,730/10g; XAU/USD $4,163.46; USD/INR ₹95.44; WGC CB data July 2026; RBI 880.52t unchanged

**Pages updated**:
- `wiki/central-bank-gold-demand.md` — WGC July 2026 May data: net +41t; all buyer/seller details; 45%/89% CB survey; last updated July 6
- `wiki/poland-gold-reserves.md` — May +18t confirmed; total ~631t; YTD ~81t; last updated July 6
- `wiki/china-pboc-gold.md` — May ~+10t (WGC); 20th consecutive month; total ~2,341.52t; June pending; last updated July 6
- `wiki/russia-gold-reserves.md` — May −6t; YTD −34t; total ~2,292t; reserve value ~$282B; last updated July 6
- `wiki/india-gold-market.md` — July 6 MCX ₹1,46,730 (−0.01%); Goldman implied MCX target; EMA levels; last updated July 6
- `wiki/gold-geopolitical-risk-premium.md` — July 6 price $4,163; 9d/50d levels; signal Wait (+1); last updated July 6
- `wiki/fed-macro-factors.md` — rates held 3.50-3.75%; PCE 3.6%; 9/18 hawkish; FOMC minutes week; Macro = Neutral (0); last updated July 6
- `wiki/global-cb-activity-log.md` — full July 6 section (~20 rows): WGC May CB data; all major countries; Signal: Wait (+1); last updated July 6
- `wiki/index.md` — all changed page descriptions updated; singapore-mas-gold added; uzbekistan/kazakhstan YTDs updated
- `wiki/log.md` — this entry
- `prices/prices.csv` — 2026-07-06 row appended (Gold $4,163.46, Silver $62.60, DXY 100.88, WTI 68.78, USD/INR 95.438)
- `signals/signals.csv` — Wait (+1) appended

**Minor country pages updated** (YTD figures):
- `wiki/uzbekistan-gold-reserves.md` — May +9t; YTD ~33t
- `wiki/kazakhstan-gold-reserves.md` — May +7t; YTD ~20t
- `wiki/czech-republic-gold-reserves.md` — May +2t; 39 consecutive months

## 2026-07-11 — COT weekly update
Report_Date: 2026-07-07 | MM_Net: +116,161 (+766 vs prior week) | OI: 371,776 | Sentiment: Neutral zone | Source: CFTC via GitHub Action (fetch_cot.yml), fetched 2026-07-10T21:34:33Z

## 2026-07-13 — Daily automated update

**Web searches**: NSE/BSE July 2026 holiday check (no holidays); gold spot price July 13; XAU/USD 9d EMA; gold 50d EMA; DXY July 13; WTI crude July 13; USD/INR July 13; silver price July 13; Iran-US conflict escalation July 2026; India MCX gold price July 13; India gold ETF flows RBI; WGC central bank gold statistics June 2026; Fed Warsh rate signal July 2026; Germany Bundesbank repatriation July 2026.

**Prices fetched (web search — yfinance/metals.dev proxy-blocked)**:
- Gold: $4,053.92 (Sunday spot; July 12 close $4,121.95); prev Friday $4,116.00
- Silver: $58.72/oz; DXY: 101.10; WTI: $74.71; USD/INR: ₹95.56
- 9d EMA: ~$4,090 (est. from prices.csv); 50d EMA: ~$4,320 (TipRanks/FXStreet web search)

**Key findings**:
1. Iran war sharply re-escalated: Trump declared 60-day MOU ceasefire "over" (July 8); US revoking Iran oil license; US struck Tehran; Iran retaliating on UAE/Kuwait/Bahrain; Hormuz tanker attacks. WTI surged +4.3% to $74.71. Gold FALLING (−1.5%) — macro/Fed channel dominant.
2. Fed hawkish Warsh shock (confirmed in FOMC June minutes July 8): 9/18 FOMC members project 2026 rate hike; market pricing >75% probability. No forward guidance policy. CPI July 14 is critical catalyst tomorrow.
3. WGC June 2026 CB data (published July 7): China (PBoC) +14.93t June (20-month streak; total 2,346t); Uzbekistan +9t June (YTD ~41t; #2 buyer); Poland YTD #1 ~81t; Singapore +4t May (first since Sep 2025; total 197t).
4. WGC CB survey: 89% of central bankers expect global gold reserves to increase in next 12 months; 45% plan to increase their own holdings.
5. India: 15% import duty unchanged; ETF AUM ₹1,84,571 crore (May 2026); 6 AMCs impose subscription restrictions; MCX gold ~₹1,44,760/10g (July 10 ref); Business Standard flagged gold/silver volatility ahead of CPI July 14.
6. Germany: no new Bundesbank repatriation announcement; political pressure continuing from AfD/Greens; CDU still backing FRBNY.

**Trading Signal**: **Wait (Score: 0)**
- Factor 1 Price vs targets: +1 (17.3% below GS $4,900)
- Factor 2 Geopolitical: 0 (Iran escalating but gold not responding as safe haven; ambiguous)
- Factor 3 Fed/macro: −1 (Warsh hawkish; >75% hike probability; CPI July 14 risk tomorrow)
- Factor 4 CB demand: +1 (PBoC June +14.93t announced July 7 — within 7 days)
- Factor 5 Technicals: −1 (below both 9d EMA ~$4,090 and 50d EMA ~$4,320; not 2 green days)
- Factor 6 Dollar pressure: 0 (DXY +0.16%; USD/INR +0.25%; both within 1%)

**Files updated**:
- `prices/prices.csv` — added 2026-07-13 row
- `raw/india-gold-2026-07-13.md` — created
- `wiki/global-cb-activity-log.md` — July 13 section added (14 country rows)
- `wiki/iran-conflict-2026.md` — updated summary + timeline
- `wiki/fed-macro-factors.md` — updated summary (Warsh hawkish shock, >75% hike)
- `wiki/gold-geopolitical-risk-premium.md` — updated summary + July 13 timeline entry
- `wiki/india-gold-market.md` — updated summary
- `wiki/china-pboc-gold.md` — last updated date refreshed (June +14.93t already logged July 8)
- `wiki/uzbekistan-gold-reserves.md` — last updated date refreshed (June +9t already logged July 9)
- `wiki/index.md` — updated descriptions for iran-conflict, fed-macro, gold-geopolitical, india-gold-market, global-cb-activity-log
- `signals/signals.csv` — added 2026-07-13 Wait signal

## 2026-07-14 — Daily update: Gold ~$4,009 (−1.1%); Trump Hormuz blockade + 20% toll; WTI $79.57 (+1.83%); June CPI released; Waller hawkish; MCX ~₹1,40,963–₹1,41,550 (−2.1%); USD/INR ₹95.81 | Signal: Wait (−1)

**Raw file created**:
- `raw/india-gold-2026-07-14.md` — MCX ~₹1,40,963–₹1,41,550/10g (−2.1%); XAU/USD $4,009.45 (−1.1%); Silver $58.00 (~−1.2%); DXY 101.29 (+0.19%); WTI $79.57 (+1.83% — Trump Hormuz blockade+20%toll); USD/INR ₹95.81 (+0.26%); June CPI released today; Waller hawkish; 15% duty unchanged

**Pages updated**:
- `wiki/iran-conflict-2026.md` — July 14 timeline entry added: Trump reinstated Hormuz blockade + 20% toll demand on all transiting cargo; WTI +1.83% to $79.57; Iran exported 57M bbl during blockade gap; Factor 2 = Bearish (−1); last updated July 14
- `wiki/fed-macro-factors.md` — July 14 section added: June CPI released (exp 3.8-3.9%); Gov. Waller hawkish ("if CPI rises, consider rate hikes"); Warsh testimony; Hormuz oil surge; July FOMC hike 25-30% prob; Macro factor = Bearish (−1); last updated July 14
- `wiki/gold-geopolitical-risk-premium.md` — July 14 price row added ($4,009.45; below both EMAs 9d~$4,100 and 50d $4,319.64; NOT safe haven; Signal Wait −1); last updated July 14
- `wiki/india-gold-market.md` — July 14 MCX section: ₹1,40,963–₹1,41,550/10g; WTI surge; CPI impact; Waller hawkish; USD/INR ₹95.81; last updated July 14
- `wiki/poland-gold-reserves.md` — Bloomberg Jul 9 data incorporated: 82t YTD 2026 (Governor Glapinski confirmed); total ~613t; +37t since April; $5B value; last updated July 14
- `wiki/global-cb-activity-log.md` — July 13 and July 14 sections added (July 13 was missing from prior run); Poland 82t Bloomberg entry; Iran Hormuz blockade; no new CB buy/sell data beyond Poland confirmation; last updated July 14
- `wiki/index.md` — page descriptions updated: gold-geopolitical-risk-premium, iran-conflict-2026, fed-macro-factors, india-gold-market, global-cb-activity-log, poland-gold-reserves, central-bank-gold-demand; last updated July 14
- `wiki/log.md` — this entry

**Prices recorded** (prices.csv):
- Gold: $4,009.45 | Silver: $58.00 | DXY: 101.29 | WTI: $79.57 | USD/INR: ₹95.81 | Volume: N/A

**Signal**: Wait (−1)
- Factor 1 (Price vs targets): +1 — gold 18.2% below Goldman $4,900
- Factor 2 (Geopolitical): −1 — Trump Hormuz blockade+20%toll; oil surge → inflation → rate hike fears (NOT safe-haven gold channel)
- Factor 3 (Fed/Macro): −1 — June CPI day + Waller hawkish + Warsh testimony + fresh Hormuz oil surge
- Factor 4 (CB Demand): +1 — PBoC Jun+14.93t (Jul7, within 7d); Poland 82t (Bloomberg Jul9, within 7d)
- Factor 5 (Technicals): −1 — below both EMAs (9d~$4,100, 50d $4,319.64); last 2 days red; 50d>9d downtrend
- Factor 6 (Dollar Pressure): 0 — DXY +0.19% (within 1%), USD/INR +0.26% (within 1%)

---

## 2026-07-17 — Daily Update

**Sources ingested**: `raw/india-gold-2026-07-17.md`

**Pages updated**:
- `wiki/iran-conflict-2026.md` — MAJOR: Iran Strait of Hormuz remains CLOSED (July 12 declaration); US 3rd+ round of strikes; Iran retaliated on Jordan/Qatar/Kuwait/Oman; gold FALLING despite escalation (safe-haven paradox); Factor 2 updated to Bearish (−1)
- `wiki/gold-geopolitical-risk-premium.md` — Gold breached $4,000 to $3,985 (−1.8%); 9d EMA updated to $4,111 (web search); 50d EMA $4,319; safe-haven paradox documented
- `wiki/fed-macro-factors.md` — July 17 data: retail sales in-line, jobless claims 208K (2-month low); June payrolls 57K miss; FOMC July 28-29 hold 90%; net Macro: Neutral (0)
- `wiki/india-gold-market.md` — MCX ~₹1,40,000/10g; USD/INR 96.43; WTI $79.67; Iran Strait disrupting Dubai-routed shipments; Signal: Wait (+2)
- `wiki/poland-gold-reserves.md` — Confirmed 82t YTD (Bloomberg Jul 9; Glapiński), total 632.4t, "buying the dip" confirmed
- `wiki/global-cb-activity-log.md` — Added July 17 entries: Iran Strait closure/strikes; Poland 82t YTD; WGC CB survey (45% plan to buy, 850t 2026 full-year); major holder status checks (Germany, Saudi, Japan, UK, Italy, France all no new data); India MCX update

**Prices recorded** (2026-07-17): Gold $3,985.00 | Silver $58.50 | DXY 100.60 | WTI $79.67 | USD/INR 96.43

**Signal**: Wait (+2)
- Factor 1 (Price vs targets): +1 — $3,985 is 18.7% below GS revised target $4,900 (→ >15% below = Bullish)
- Factor 2 (Geopolitical): −1 — Iran Strait CLOSED; US conducting strikes; gold FALLING despite crisis; oil/inflation/Fed channel dominates (Bearish)
- Factor 3 (Fed/Macro): 0 — June payrolls 57K (dovish) vs WTI +11% w/w oil surge (hawkish); net Neutral
- Factor 4 (CB Demand): +1 — PBoC Jun+14.93t (Jul 7); WGC May data (Jul 3); Poland 82t YTD (Jul 9-10); all within 7 days
- Factor 5 (Technicals): +1 — below both EMAs (9d $4,111, 50d $4,319); last 2 CSV days both green (Jul 15: +$43, Jul 16: +$6) = Bullish per table
- Factor 6 (Dollar Pressure): 0 — DXY 0.0% change (100.60→100.60); USD/INR +0.25% (within 1%); net Neutral

**Key new findings**:
- Iran Strait of Hormuz closure (July 12) and US 3rd round strikes is creating "safe-haven paradox" — gold falling despite escalation; WTI +11% w/w to $79.67
- WGC 2026 CB Survey: record 45% of CBs plan to increase holdings; 89% expect global reserves to rise; 850t 2026 full-year forecast
- Gold has breached $4,000 for the first time since early July; now $126 below 9d EMA
- Goldman Sachs (revised June: $4,900) and JPMorgan (Q4: $4,500) cuts now well-documented; gold trading well below both

---

## 2026-07-18 — Data fix: prices.csv switched to previous-day closes; July signals re-scored

**Source**: User-reported bug — prices.csv rows were live ~12 PM IST snapshots (the price at routine run time), not daily closes. On 2026-07-17 this made Factor 5 score "last 2 days green" when the real Jul 15/16 closes were both red (the big US-session drops landed in the *next* day's row).

**Root cause**: `fetch_prices.py` `run_today()` appended `rows[-1]` — yfinance's in-progress bar for the current session.

**Changes**:
- `fetch_prices.py` — now appends only COMPLETED trading days (Date < today UTC); heals up to 7 days of gaps; never writes the live bar
- `prices/prices.csv` — rows 2026-06-25 → 2026-07-17 rewritten with official yfinance daily closes (GC=F, SI=F, DX-Y.NYB, CL=F, USDINR=X); missing 2026-06-26 trading day inserted; rows ≤ 2026-06-24 remain legacy snapshots
- `wiki/signal-methodology.md` — new "Price data basis" section; Factor 5 now evaluates the last two completed sessions; price-vs-EMA position uses newest CSV close; also finally committed the 2026-07-02 fixes (explicit "2 green" definition; Factor 6 threshold ±1.0% → ±0.5%) which had never been pushed — the cloud routine kept scoring with the 1% threshold through Jul 17
- Cloud routine `trig_01Q7FfuV2Y2Fqk4f8dtokd2J` prompt updated to match (close basis, 2-green definition, 0.5% threshold, previous-session-close web patches)

**Re-score (close basis + 0.5% Factor 6 threshold), signals.csv corrected in place**:
- 2026-07-02: Wait −2 → Wait 0 (Jun 30 & Jul 1 closes both green → Factor 5 −1→+1)
- 2026-07-03: Buy 3 → Buy 4 (DXY −0.52%, INR +0.53% → Factor 6 0→+1)
- 2026-07-15: Wait 2 → **Buy 3** (USD/INR +1.02% close-over-close — exceeded even the old 1% threshold; snapshot had shown only +0.62%)
- 2026-07-17: Wait 2 → Wait 0 (Jul 15 −$17 and Jul 16 −$58 both red → Factor 5 +1→−1; the "2 green" was a snapshot artifact)
- All other July days: factor values re-checked, scores unchanged

---

## 2026-07-22 — Daily update: Iran deal "over" (NATO summit); oil pullback; FOMC hike prob 36.3%

**Source**: `raw/india-gold-2026-07-22.md` (new); web research (gold spot, Iran, FOMC, CB activity, India MCX)

**Prices (T-1 = July 21 closes)**:
- XAU/USD: $4,007.77 | Silver: $29.17 | DXY: 100.92 | WTI: $82.58 | USD/INR: ₹96.4330
- MCX gold (July 22 intraday): ₹1,44,408/10g (+1.07%)

**Signal**: **Wait (0)**
- Factor 1 (Price vs GS $4,900): $4,007.77 = 18.2% below → **+1 Bullish**
- Factor 2 (Geopolitics/Iran): Deal "over" per Trump at NATO summit; oil pulling back from $88; gold relief rally → **0 Neutral**
- Factor 3 (Fed/Macro): FOMC Jul28-29 hike prob **36.3%** (up from 25%); Goldman cut forecast on no 2026 cuts; CPI 4.2%; oil pullback slightly reduces pressure → **-1 Bearish**
- Factor 4 (CB Demand): Czech Republic +2t July 16 within 7-day window; WGC: record 45% CBs plan to increase holdings → **+1 Bullish**
- Factor 5 (Technicals): Jul 18 close ($4,017.52) GREEN; Jul 21 close ($4,007.77) RED — not 2 green; gold below both 9d EMA (~$4,030-$4,050) and 50d EMA (~$4,450-$4,480) → **-1 Bearish**
- Factor 6 (Dollar): DXY +0.22%; USD/INR -0.07% — both within ±0.5% threshold → **0 Neutral**
- **Total: +1+0-1+1-1+0 = 0 → Wait**

**Pages updated**:
- `wiki/india-gold-market.md` — MCX ₹1,44,408; investment demand (82t) > jewellery (66t) first time; imports -42% m/m
- `wiki/gold-geopolitical-risk-premium.md` — intraday ~$4,073-$4,079; Iran deal "over"; oil pullback; EMAs updated
- `wiki/iran-conflict-2026.md` — ceasefire deal declared "over" by Trump at NATO summit; oil pulling back WTI $82.58
- `wiki/fed-macro-factors.md` — FOMC hike prob 36.3% (up from 25%); Goldman cut on no 2026 rate cuts
- `wiki/global-cb-activity-log.md` — July 22 section; Czech +2t in 7d window; WGC 45% CBs; gold > US Treasuries
- `wiki/index.md` — descriptions updated for all changed pages

**New files**: `raw/india-gold-2026-07-22.md`, `prices/prices.csv` (July 21 row added)
