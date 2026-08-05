# India Gold News - 2026-08-05

**Date**: 2026-08-05
**Sources**:
- https://www.businesstoday.in/personal-finance/investment/story/gold-silver-prices-today-august-5-check-latest-rates-in-delhi-mumbai-kolkata-other-cities-547247-2026-08-05
- https://www.goodreturns.in/gold-rates/
- https://www.cnbc.com/2026/05/13/india-hikes-bullion-import-duties-to-arrest-rupee-slide.html
- https://www.gold.org/goldhub/gold-focus/2026/05/india-gold-market-update-import-tightening
- https://hellobanker.in/rbi-gold-reserves-rise-to-880-52-metric-tonnes-government-informs-parliament/
- https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-india-focus-q2-2026
- https://www.bookmyforex.com/currency-converter/usd-to-inr/forecast/
- https://news24online.com/india/this-small-district-has-indias-largest-gold-refinery-produces-over-300-tonnes-of-gold-a-year-located-in/865868/

---

## MCX Gold Price

MCX gold futures were up ~0.60% at approximately ₹1.45 lakh per 10 grams intraday on August 5, 2026 (source: businesstoday.in). This is a live/intraday quote, not an official close — kept out of `prices/prices.csv` per the close-basis rule. Directionally consistent with COMEX gold's move (Aug4 close $4,077.48, +0.97% vs Aug3) plus a modestly weaker rupee.

## RBI / Reserves

No new RBI gold data since the last confirmed figure. RBI held 880.52 metric tonnes as of June 26, 2026 (source: hellobanker.in, citing government parliamentary disclosure) — unchanged from prior wiki entries. Gold's share of India's FX reserves continues to be cited around 13.9%, up from 9% in September 2024, driven by both repatriation (274t repatriated since March 2023) and price appreciation (source: hellobanker.in). No new repatriation or purchase announcement in the last 24-48h.

## Import & Trade

No new policy change. The 15% total effective import duty (10% Basic Customs Duty + 5% Agriculture Infrastructure & Development Cess), in place since the May 2026 hike aimed at defending the rupee, remains unchanged (source: cnbc.com, gold.org/goldhub). WGC continues to project jewellery and bar/coin demand will decline 50-60 tonnes (~10% y/y) in 2026 because of this duty hike.

## Retail & Jewellery Demand

Early signs of a pickup in jewellery demand since late June, attributed to lower/more stable gold prices; retailers reported building inventory ahead of the festive season, which begins in late August 2026 (source: gold.org/goldhub, WGC India Focus Q2 2026 update). No fresh data point specific to August 5.

## ETF & Investment Flows

No new monthly figure since the last confirmed reading. Indian gold ETFs saw a rebound in June 2026 with net inflows of ₹34.4bn (~$356mn, the highest since February), and early-July inflows continued at an estimated ₹12.1bn (~$127mn) for July 1-10 (source: gold.org/goldhub, WGC India Focus Q2 2026). Q2 2026 ETF demand overall moderated to 4t, down >80% from Q1's record 20t, though India remained one of the few markets with positive net demand.

## INR Impact

USD/INR previous-day close (Aug 4, 2026): approximately ₹95.33-95.39 (best-effort reconstruction; see prices.csv note below). One source (bookmyforex.com derived) showed the rate touching a low of 94.8872 intraday on August 5 — a modest rupee strengthening move if accurate, though this is a live/intraday reading, not a close, and was not written to prices.csv. Net effect on MCX gold: broadly rupee-neutral to slightly rupee-supportive over the last 2 sessions.

## Policy & Regulation

No new government gold policy announcement in the last 24-48h. The May 2026 import duty hike (see above) remains the most recent policy action; PM Modi's public request for Indians to pause gold buying for a year (made around the same time) also remains the most recent policy-adjacent statement, no new developments today.

## Other India Gold News

India's largest gold refinery remains the Mewat (Nuh), Haryana facility (~300+ tonnes/year capacity); no operational or capacity news from the last 24-48h. Deccan Gold Mines Ltd (India-listed) reported progress at its Altyn Tor project in Kyrgyzstan (pre-commissioning trials) — an overseas exploration asset, not domestic production, and not a new development specific to today's window; noted for completeness only.

## Data-quality note (network access)

**yfinance, the metals.dev fallback, and direct FRED (`fredgraph.csv`) access were all blocked by the sandbox's outbound egress policy this run** (confirmed via `$HTTPS_PROXY/__agentproxy/status` → `recentRelayFailures`: repeated "gateway answered 403 to CONNECT (policy denial or upstream failure)" for `fc.yahoo.com`, `query1.finance.yahoo.com`, `api.metals.dev`, and `fred.stlouisfed.org`). **`WebFetch` also returned HTTP 403 on every external site attempted today**, including normally-permissive ones (Wikipedia), indicating the tool itself was non-functional this session, not just individual sites blocking bots. All price and yield data this run was reconstructed from `WebSearch` snippets only — see `wiki/log.md` for the full reconciliation notes and confidence caveats on each figure. This is the same failure pattern logged on 2026-08-04 — a persistent, not transient, condition in this environment.
