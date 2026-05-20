# Decision — Initial compliance scope (2026-05-20, Gee)

Locked threshold answers that branch the rest of the investigation
in `theta/compliance/COMPLIANCE.md`.

## Answers
1. **Characterization** — UNRESOLVED. Defer to counsel. (COMPLIANCE.md §1.)
2. **Geography day-one** — **US only, geofenced.** (COMPLIANCE.md §5.9.)
3. **Coaches** — **LLM-driven, interactive.** (COMPLIANCE.md §2.6, §10.)
4. **Legal budget** — **Bootstrap, minimum viable, accept higher risk.**

## What this combination implies
- **Geography lock closes ~90% of international complexity.** UK FCA
  s.21, MiFID II, ASIC, CIRO, MAS, SFC, JFSA all off day-one critical
  path. Re-open per-country when adding it. App Store + Play Store
  country restrictions + server-side scan geofence + ToS US-only
  clause are all free.
- **LLM + bootstrap is the high-tension pair.** An LLM will not stay
  inside an impersonal-publisher scope by default. The moment it
  answers "should I sell my DT" or references the user's holdings, the
  *Lowe v. SEC* publisher's exemption is gone and we are *de facto*
  in characterization (C) without registering. Under bootstrap
  budget, the safety has to be **designed in**, not lawyered in.
- **Unresolved characterization + bootstrap = the design has to be
  conservative enough to survive any of (A), (B), or the most
  defensible read of (C).** Treat scope as (B) until told otherwise.

## Risk owned by Gee, not transferred to counsel
By choosing bootstrap, Gee is personally absorbing the risk a
$25–80k counsel engagement would normally transfer. That is a real,
legitimate small-business choice. It is documented here so the
trade-off is eyes-open and traceable.

## Bootstrap-safe LLM scope (proposed, awaiting Gee confirm)
- The LLM is allowed to:
  - Teach options concepts, Stoic concepts, lesson content.
  - Respond to questions about the *lesson* the user is in.
  - Explain what's on the scanner card in generic terms.
  - Stay in-character as the coach (Lyra/Nestor/Chiron/Atlas voice).
- The LLM is **NOT** allowed to:
  - Read or reference the user's portfolio / holdings.
  - Recommend buying or selling a specific security.
  - Confirm or critique a *specific* trade the user mentions ("Was
    my AAPL call a good idea?" → refuse + redirect to the lesson).
  - Predict price direction on any specific ticker.
  - Make any forward-looking performance claim.
  - Discuss tax treatment beyond a "consult a tax advisor" line.
  - Speak about anything outside the lesson curriculum.
- Implementation:
  - System prompt enforcing the refusal taxonomy above.
  - Pre-prompt classifier (fast, cheap) that screens user input for
    personalized-advice intent and short-circuits before LLM call.
  - Server-side log of every prompt + completion (recordkeeping
    posture even though not required absent registration).
  - Adversarial test suite ("should I buy X", "what's your price
    target", "is my portfolio diversified") — refuse cleanly.
  - Use Anthropic Enterprise or OpenAI ZDR endpoints so prompts +
    completions are not retained or used for training.

## Cheap / free controls to ship day-one (the bootstrap playbook)
Each of these would otherwise be a counsel ask; under bootstrap they
are engineering + content work the team does itself.

1. **App store availability — US only.** App Store Connect + Play
   Console country toggles. Free. Closes RF-07 mechanically.
2. **Server-side geofence on `/scanner` and `/coach` endpoints.**
   IP + payment-country check. Reject with a "coming soon to your
   region" page. Free.
3. **ToS US-only clause + governing law (Delaware or founder's
   state) + arbitration.** Templates exist; one $1–2k attorney
   review pass recommended.
4. **Hard 18+ age gate at signup.** Date-of-birth field, refuse if
   under 18. Eliminates COPPA and aligns with options-eligibility.
5. **First-launch Risk Disclosure modal** — full-screen, must-scroll,
   tap-to-accept. Covers: education-not-advice; options risk;
   past-performance disclaimer; LLM-output disclaimer.
6. **Persistent footer disclaimer** on every screen showing tickers
   or trade ideas: "Educational content. Not investment advice.
   Options involve substantial risk of loss." Cheap to design.
7. **Link to OCC's Options Disclosure Document** ("Characteristics
   and Risks of Standardized Options") inside every options lesson
   and on first scanner view. Free; OCC hosts the document.
8. **Schwab integration: read-only, deep-link only.** No order
   pre-fill via API. The `OPEN BROKERAGE` button opens Schwab's
   own app/web to the ticker page; Theta never touches an order
   ticket. Engineering decision; documents to RF-03.
9. **Schwab token handling: encrypted at rest (AWS KMS / GCP KMS /
   HashiCorp Vault), rotated, access-logged.** Reg S-P safeguards
   posture without retainer.
10. **Scanner: same content for every US user.** Drop the
    `holdings (n)` block from the home screen until characterization
    is resolved. Or move it to a separate "My Holdings" tab that the
    user populates manually and that is *visually and logically
    decoupled* from any signal. Closes RF-01 mechanically.
11. **No testimonials. No performance claims. No "X% in Y days."
    No "earn while you learn." No influencer pay-for-post day one.**
    Eliminates 80% of marketing-rule and FTC endorsement risk for free.
12. **No "AI" word in marketing** until we are ready to handle
    AI-washing exposure. Call them "coaches," "characters,"
    "instructors" — never "AI-powered" unless every claim is provable.
13. **Subscription compliance** — Apple/Google handle most of ROSCA
    via their stores. If we ever add a web checkout, use Stripe's
    auto-renewal copy + clear-and-conspicuous disclosure + in-app
    cancel.
14. **Privacy policy + cookie banner via Termly/iubenda** (~$10–30/mo)
    customized for trading + LLM data. Single attorney review pass.
15. **LLM data hygiene** — no portfolio data sent to model providers;
    use no-retain enterprise endpoints; redact PII before logging.
16. **USPTO TESS search on "Theta" in IC 036 + IC 041** — DIY first
    pass free at https://tmsearch.uspto.gov; followed by a $500–$1.5k
    clearance opinion from a TM attorney before public launch.
17. **Conversation logs retained 5 years.** Aligns with Advisers Act
    Rule 204-2 even though we're not registered — survives a future
    "you should have registered" enforcement letter much better.
18. **VPN clause in ToS** — explicit that VPN access from outside the
    US is prohibited and account may be terminated. Closes the loop
    on geofence circumvention.
19. **Document every design choice that LIMITS scope as a compliance
    control.** ("We do not show user holdings on the home screen for
    compliance reasons" — written into DESIGN.md.) This is the
    paper trail an enforcement letter would ask for.
20. **Trigger event to revisit:** at 5,000 paying US users, or first
    sign of UK/EU traffic, or any plan to take payments outside
    Apple/Google, or any marketing that names a specific ticker —
    upgrade to counsel engagement immediately.

## What we will NOT do under bootstrap (red lines)
- No live trade execution via Theta. Schwab deep-link only.
- No order pre-fill via Schwab API.
- No personalized recommendations from the LLM.
- No specific-ticker price targets from any coach video or post.
- No marketing claim of returns, performance, win-rate of users, or
  "track record" of the scanner.
- No paid testimonial / influencer marketing without FTC-compliant
  disclosure + attorney pass.
- No availability outside the US on day one.
- No marketing of "AI" until we can defend every AI claim.
- No "Capital Mind" data redistributed until we have a written
  license confirming our right to do so.

## Open items still owed to counsel (for the day we do hire one)
1. Lowe v. SEC opinion letter once scope is final.
2. Schwab Developer Portal ToS review.
3. Reg S-P safeguards policy sign-off.
4. ToS + Privacy + Risk Disclosure final pass.
5. USPTO clearance + filing intent-to-use on "Theta" in IC 036/041.
6. Capital Mind redistribution license.
7. LLM refusal-taxonomy review for §206 anti-fraud exposure.

## Next steps in this investigation
- Confirm proposed LLM scope (above) with Gee.
- Walk RF-01 through RF-12 in `COMPLIANCE.md §13` row-by-row, mark
  each "design-fix possible under bootstrap" vs "needs counsel."
- Draft Risk Disclosure modal copy (free; lives in repo).
- Sketch the LLM system prompt + refusal taxonomy.
- Pull a sample Capital Mind output to assess re-publishing scope.
- DIY USPTO TESS pass on "Theta" in IC 036 + IC 041.
