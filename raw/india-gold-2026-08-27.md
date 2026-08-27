# India Gold News - 2026-08-27

**Date**: 2026-08-27
**Sources**: https://www.businesstoday.in/personal-finance/story/gold-silver-prices-today-august-27-check-latest-rates-in-delhi-mumbai-kolkata-other-cities-551644-2026-08-27, https://www.goodreturns.in/gold-rates/, https://sundayguardianlive.com/business/gold-price-today-in-india-august-26-mcx-gold-hits-163-lakh-remains-steady-check-latest-city-wise-gold-rates-across-delhi-mumbai-pune-bangalore-chennai-more-270418/, https://www.businesstoday.in/personal-finance/story/gold-etfs-attract-rs1179-crore-in-first-half-of-august-even-as-prices-rebound-what-is-driving-investor-demand-550764-2026-08-22, https://www.gold.org/goldhub/gold-focus/2026/08/india-gold-market-update-recovery-taking-shape, poonawallafincorp.com gold import tax 2026, ddnews.gov.in RBI 855t gold reserves

---

## MCX Gold Price

MCX gold futures were up ~0.56% at roughly ₹1.60 lakh/10g on August 27, tracking COMEX's pullback from Tuesday's 3-month+ high. Retail 24K gold ≈ ₹16,298/gram, 22K ≈ ₹14,940/gram, 18K ≈ ₹12,224/gram (source: goodreturns.in, businesstoday.in). This follows Aug26's steady MCX read of ~₹1.63 lakh/10g. Note the day-over-day figures across sources are not perfectly reconciled (₹1.60L vs ₹1.63L) — both are retained as reported since MCX and retail-city quotes track slightly different baskets/timing.

## RBI / Reserves

No new RBI announcement found today. RBI gold holdings remain on record at 880.52t (unchanged Q2 2026). One recycled older DD News item references RBI reserves at "855 metric tonnes" — this is a stale/outdated figure inconsistent with the 880.52t figure already established in [[india-rbi-gold]] and is disregarded as noise, not a correction.

## Import & Trade

No new data on import volumes today. The 15% gold/silver import duty (10% BCD + 5% AIDC, effective May 13, 2026) remains unchanged; WGC continues to project 50-60t of demand destruction (~10% y/y) from the hike.

## Retail & Jewellery Demand

WGC's "Recovery taking shape" update (carried from Aug 19, still the latest dedicated India piece) continues to describe jewellery demand strengthening into the festive season as consumers treat recent price pullbacks as buying opportunities, though elevated absolute price levels remain a constraint on volumes.

## ETF & Investment Flows

No fresher print than the already-recorded ₹1,179 crore net inflow into Indian gold ETFs for the first half of August; total AUM ₹1,733bn (~$18.1bn), 12.53 million folios. No new data found for the second half of August.

## INR Impact

USD/INR closed around ₹95.55 (Aug26, web-search estimate — see note below), broadly flat-to-slightly-firmer versus Aug25's ₹95.7310 close. A live mid-market read around 18:11 UTC Aug27 showed ~₹95.37, suggesting continued modest rupee strength into today's session. This modest INR firming is a small drag on domestic gold prices, layered on top of the COMEX pullback.

## Policy & Regulation

No new gold-specific government policy announcement found today.

## Other India Gold News

**Data-sourcing note**: `fetch_prices.py` (yfinance + metals.dev fallback) and a direct `curl` to `fred.stlouisfed.org` were all blocked with 403s by the network egress proxy today — confirmed as an organization policy denial via `$HTTPS_PROXY/__agentproxy/status` (`recentRelayFailures` showed `connect_rejected` for `query2.finance.yahoo.com`, `api.metals.dev`, and `fred.stlouisfed.org`), not a transient error. This is consistent with every daily run since the block began around 2026-07-31. All of today's Gold/Silver/DXY/WTI/USD_INR previous-day-close figures and the DFII10 real-yield reading were sourced via WebSearch and manually appended to `prices/prices.csv` / `prices/real_yields.csv`. Precision on USD/INR in particular is lower than usual today — no single source gave a clean "Wednesday Aug 26 close" print; ₹95.55 is a best-effort estimate bracketed between the confirmed Aug25 close (₹95.7310-95.7438) and a live Aug27 mid-market read (~₹95.37).
