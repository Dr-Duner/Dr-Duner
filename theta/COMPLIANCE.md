# THETA — Compliance Posture & Marketing Copy Rules

Status: working draft (2026-05-20). NOT legal advice — this captures the
structural posture and the open questions for a securities attorney.
Update every time the product touches anything execution-related.

> **TL;DR.** At launch Theta is **education + a self-configured scanner
> + paper-trade execution**. There is no real-money order routing in v1.
> That posture keeps Theta clear of broker-dealer / investment-adviser
> registration triggers. Every line of marketing and product copy must
> stay inside that posture.

---

## 1. The structural posture (the three-piece defense)

The legally defensible shape of Theta is three boxes that never collapse
into "we recommend trades":

1. **Education** — the 20 coach-led lessons. Teaches strategies and
   discipline. Pure information; no personalized recommendation.
2. **Tool** — the scanner. Filters live (or delayed) options data
   against parameters **the user built from the lessons**. The output is
   "options that match the criteria *you* set," not "options Theta
   thinks you should buy."
3. **Self-directed execution** — at launch, paper trade only. User
   picks every parameter, user taps send. Theta never decides for them.

This separation is what makes the product *not* a registered
investment adviser, *not* a broker-dealer, and *not* a signals service.
If any one of these boxes leaks into another, the posture collapses.

## 2. Paper-trade-only launch — what that buys us

Decision (LOCKED 2026-05-20, Gee): launch with paper trades only. The
"send" beat in every lesson video and in the app is a **simulated**
order, not a real broker order. On-screen framing must make this
unambiguous (`PAPER TRADE` badge on the review and sent screens).

What it gives us at launch:
- **No broker-dealer registration trigger** — we never route real
  customer orders.
- **No investment-adviser registration trigger** — we never accept
  compensation for personalized recommendations on specific securities.
- **No PFOF, no custody, no clearing** — no money flow at all.
- The compliance surface area at launch is roughly: subscription
  contracts + standard education/entertainment disclaimers + terms
  of service + privacy.

What it does NOT buy us:
- FTC scrutiny of marketing claims still applies (no "we find you
  profitable trades", no implied returns, no testimonials without
  disclosure).
- State-level disclosure rules around "investment education" still apply
  in some jurisdictions.
- Real-money execution (Phase 2) is a separate, much bigger
  compliance build — start that conversation early, not late.

## 3. Marketing copy rules (do / don't)

### Always
- "Trades that match **the strategy you built**."
- "Practice trading on Theta — **paper trades only**, no real money."
- "Learn the strategy. Build it in. Run it yourself."
- "**Education and tools**, not advice."
- Attribute results to *the user's process*, not Theta's picks.

### Never
- "We find you profitable trades."
- "Our picks." / "Our trade ideas." / "Theta recommends…"
- "Guaranteed returns" / "Beat the market" / any specific return number.
- Personalized phrases like "buy NVDA calls today" in any push, banner,
  email, or screen.
- Testimonials with specific dollar gains, unless under proper FTC
  endorsement guides (with typical-results disclosure).
- Anything that implies Theta is choosing the security for the user.

### Gray zone (needs attorney review before use)
- "Backtested" performance claims for the scanner — even of user-built
  strategies. Backtested numbers carry their own disclosure requirements.
- Showing real-time options chains in marketing materials — OPRA
  redistribution rules apply.
- Influencer partnerships — FTC endorsement disclosure required.

## 4. On-screen framing rules (in the app and in the videos)

- Every paper-trade review screen and every "sent" screen carries a
  visible **`PAPER TRADE`** label. Non-removable until real-money
  execution exists (and even then, paper mode must remain visually
  distinct).
- The scanner block's header reads "**matches your strategy**" — never
  "our picks" or "recommended."
- Every lesson includes a brief on-screen disclosure beat or persistent
  footer: "Education. Paper trading. Not investment advice."
- The Θ end card stays brand-only ("don't predict it. trade it. now.")
  — no return claims, no testimonials, no implied performance.

## 5. Phase 2 (real-money execution) — what changes

When Theta adds real-money order routing, the compliance posture shifts
materially. Likely paths in rough order of cost:
- **Introducing broker arrangement** with a partner BD (cheapest:
  the partner does the regulated work, Theta is a marketing/UI front).
- **Broker-dealer registration** (FINRA member firm) — full build,
  multi-month, six-to-seven-figure cost.
- **API hand-off to user's own broker** — user's broker is the BD;
  Theta sends order parameters via deep link or broker API. Lowest
  regulatory burden, weakest UX.

All three require:
- Suitability framework (FINRA Rule 2360 for options — account
  approval levels, options agreement).
- Reg BI compliance review of any "recommendation-adjacent" surface.
- Anti-money-laundering / KYC if Theta touches funds at any point.

Start the attorney conversation about Phase 2 **before** committing
engineering, not after.

## 6. Open questions for the securities attorney

1. Does the scanner ("trades matching *your* strategy") fall within
   the "publisher exclusion" (Lowe v. SEC) framing if it's purely
   user-configured and non-personalized?
2. At what point does a per-lesson "build your strategy" exercise that
   outputs concrete numeric parameters cross the line from education
   to personalized advice?
3. Are there state-level "investment advice" registrations that bite
   even on paper-only education products?
4. What's the cleanest disclaimer language for the lesson videos and
   the app footer?
5. Influencer / affiliate marketing — what FTC and FINRA rules apply
   to a non-BD education product partnering with finance influencers?
6. If Phase 2 uses an introducing-broker model, which partner BDs are
   most willing to take an options-first education brand on?
7. PFOF disclosure rules under Reg NMS if Phase 2 routes through a
   broker — what does Theta have to surface to users?

## 7. Change log

- 2026-05-20 — created. Triggered by Kevin's plausibility-check ask:
  the strategic posture (paper-trade-only at launch; education + tool
  + self-directed) was locked the same day.
