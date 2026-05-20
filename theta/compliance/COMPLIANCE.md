# Theta — Compliance Investigation (LIVING)

Parallel to `DESIGN.md`. This is the regulatory map for an actual
securities-law attorney to confirm and refine. Nothing here is legal
advice; this is a working investigation by the design partner playing
the role of someone who knows banking, brokerage, options, small
business, and international-app regulation. Every row gets a citation
where possible and a status: **OPEN / NEEDS COUNSEL / CLOSED**.

## 0. Locked answers (2026-05-20, Gee)
Captured in `decisions/2026-05-20_initial-bootstrap-scope.md` plus
`decisions/2026-05-20_compliance-arch.md` (the major architecture
lock that came out of the strategy-teacher + tool-of-the-user
investigation).
- **Geography day-one:** US ONLY, geofenced. Closes RF-07.
- **Coaches:** LLM-driven, interactive, **strategy teachers — not
  pick generators.** Contract: data + mechanics + strategy-fit
  check + behavioral inquiry. Never a verdict. Numerical work in
  deterministic tools; LLM narrates only. Pedagogy architecture in
  `theta/ai/PEDAGOGY.md`.
- **Legal budget:** Bootstrap. Compliance is engineering + content,
  not retainer, until trigger events fire (see initial bootstrap
  decision file).
- **Characterization (RESOLVED 2026-05-20):** Theta is a strategy
  **tool + strategy education** product, sold as SaaS. The LLM
  teaches strategies (education); the scanner runs the user's own
  strategy (tool of the user); the paper-trade simulator lets the
  user test their strategy; the journal + adherence scorer tracks
  their discipline (analytics). Does NOT require investment adviser
  or broker-dealer registration under settled SaaS-tool precedent —
  Finviz, TradingView, OptionStrat, Options Profit Calculator,
  Edgewonk, Tradervue, tastylive education arm, OptionAlpha pre-RIA
  era. See §1 (resolved) and §17 (the middle-position playbook).
- **Data tier:** 15-minute delayed, throughout Theta, forever. Real-
  time lives at the user's broker, not inside Theta. Pedagogically
  fits the 45+ DTE strategy focus where the lag is functionally
  invisible. Marketing line: *"Theta uses 15-minute data because we
  don't trade the second — we trade the strategy."*

> **Bright line.** Theta sells a *product* about *securities* to *users*
> who *trade real money*. That sentence is the regulatory perimeter.
> The faster we lock characterization (§1), geography (§5.9), and the
> scanner's personalization boundary (§2.1), the cheaper everything else
> gets. Backloading these = a redesign during US counsel review and a
> second redesign during UK/EU counsel review.

---

## 0.1. ALERT — Trademark finding (2026-05-20)
DIY trademark pass surfaced two converging concerns with the bare
"Theta" name in the options-trading space:
1. **Descriptiveness (Trademark Act §2(e)(1)).** "Theta" is the
   standard industry term for the option Greek measuring time
   decay. USPTO is likely to reject a bare THETA word mark for
   options-related goods/services as merely descriptive.
2. **Existing competitor: Theta Trading Co.** (Burlington, ON,
   founded 2019, "Stock Options Academy," 1,300+ students). Holds
   at minimum common-law trademark rights in our direct field.

**RESOLUTION DIRECTION (Gee, 2026-05-20):** **Rebrand the primary
product name.** "Theta" is preserved as an internal sub-theme
(the actual Greek measuring time decay, the L5 lesson, the
stylized Θ as a potential design-mark element). The four coaches,
Stoic framing, palette, typography, curriculum, and compliance
architecture all unchanged.

**Round 2 clearance (2026-05-20):** STOA and KAIROS ruled OUT
(both heavily taken in fintech / trading-app space; STOA also
clashes with an existing Stoic-philosophy meditation app; KAIROS
clashes with multiple AI trading apps including a Feb-2026
a16z-funded retail prediction-markets product). **GNOMON is the
surviving viable candidate** — finance presence exists (Gnomon
Alpha CTA institutional fund; Gnomon Capital PE) but at a
different audience tier from retail options education; the
well-known Gnomon School is in a different industry
(VFX/animation). Counsel clearance opinion is the next step.
Full Round 2 analysis: `compliance/trademark-tess-pass-2026-05-20.md`.
Full decision sequencing: `compliance/decisions/2026-05-20_rebrand-decision.md`.

---

## 1. Characterization (RESOLVED 2026-05-20)
**Resolution:** Theta is a **strategy SaaS tool + strategy education
product** — option (E) hybrid, the *narrowest* defensible read:
**education + strategy builder + scanner-as-tool-of-the-user +
paper-trade simulator + journal/analytics + Schwab deep-link**.
None of these components, individually or in combination, requires
investment-adviser or broker-dealer registration under settled
commercial precedent. The teaching is education (not advice); the
scanner runs the *user's* logic (not Theta's); the paper-trade
environment doesn't touch real money; the journal is analytics on
the user's own data; the deep-link is a hyperlink, not order
routing. Locked in `DESIGN.md §2.5` and the architecture decision
file `decisions/2026-05-20_compliance-arch.md`.

The options A–D below remain as historical reference and as guard-
rails: any future feature must check itself against them to make
sure it doesn't drift into (C) RIA or (D) BD territory.

Original framing (kept for reference):

- (A) **Pure education** — courses + paper-trade simulator, NO live
  signals on real tickers, NO portfolio read. Lowest regulatory burden.
  Closest analog: Investopedia Academy, Khan Academy. STATUS: not what
  the current `DESIGN.md §3b-1` describes.
- (B) **Education + impersonal newsletter scanner** — same daily scan
  to every user, NO portfolio read, NO personalization. Candidate for
  the *Lowe v. SEC* (472 U.S. 181, 1985) publisher's exemption from
  Advisers Act registration. Requires: bona fide, regular circulation,
  impersonal, not "tailored to client's individual needs." STATUS:
  achievable if we redesign the home screen to drop the user's
  `holdings (n)` block.
- (C) **Registered Investment Adviser** — personalized recommendations,
  scans reference the user's portfolio, possibly the user's risk
  profile. Requires SEC registration (>$100M AUM) or state RIA
  registration (under, with internet-adviser exemption to consider —
  17 CFR 275.203A-2(e)). Form ADV Parts 1, 2A (brochure), 2B (brochure
  supplement), and ongoing recordkeeping (Rule 204-2). Marketing Rule
  (Rule 206(4)-1) applies in full. STATUS: where the current design
  is *de facto* heading.
- (D) **Broker-Dealer** — if Theta *places* orders on behalf of users.
  FINRA membership, Form BD, Reg BI, FINRA 2360 (options), net capital
  rules (Rule 15c3-1), CIP/AML (Bank Secrecy Act). STATUS: avoid this
  perimeter at all cost on day one. Stay a deep-link to Schwab.
- (E) **Hybrid** — most fintech apps are. The hybrid most consistent
  with current design = "B for the publication + paper-trade simulator
  for the learning loop + deep-link to Schwab for execution."

**RECOMMENDED:** scope day one to **(B) + paper-trade simulator + Schwab
deep-link (NOT order placement)**. Drop the user-holdings block from
the home screen, or move it into a section the *user enters manually*
and explicitly does not interact with the scan output. Revisit (C)
after first 10k paying users.

---

## 2. United States — Federal Securities Layer

### 2.1 Investment Advisers Act of 1940
- **Definition** §202(a)(11): any person who, for compensation, engages
  in the business of advising others as to the value of securities or as
  to the advisability of investing in, purchasing, or selling securities.
  All three prongs (compensation, business of, advice) currently met.
- **Publisher's exemption — *Lowe v. SEC*, 472 U.S. 181 (1985)** — narrow
  test: (i) bona fide; (ii) of regular and general circulation; (iii)
  impersonal/not tailored. Tailoring to a user's portfolio breaks (iii).
  Free trials and individualized in-app coaching responses break (iii).
- **Registration thresholds** — generally state RIA <$100M AUM, SEC
  RIA ≥$100M. **Theta won't have AUM** if it doesn't take custody, so
  the "internet adviser" exemption (Rule 203A-2(e)) is the realistic
  SEC path if we ever register, requiring an interactive website
  delivering services to all/substantially-all clients through the
  internet.
- **No-advice carve-outs (impractical here):** Solely-incidental for
  lawyers, accountants, engineers, teachers (§202(a)(11)(B)). A school
  teaching about securities is *not* automatically exempt — must show
  the advice is incidental to the teaching, not the business model.
  Once we sell a *scanner*, that's the business model.
- **Anti-fraud applies regardless of registration** — §206 prohibits
  fraud, misleading statements, and certain principal/agency
  transactions whether or not registered. Hypothetical performance,
  cherry-picked backtests, anecdotal "wins" are §206(4) Marketing Rule
  problems even outside registration.
- **STATUS: OPEN** — pivots on §1 characterization.

### 2.2 Securities Exchange Act of 1934 — Broker-Dealer (§3(a)(4))
- "Broker" = any person engaged in the business of effecting
  transactions in securities for the account of others.
- "Effecting" includes: solicitation, participating in negotiations,
  routing orders, handling customer funds/securities, receiving
  transaction-based compensation.
- **Safe-harbor design:** the user opens Schwab's own app via deep-link
  with no order-pre-fill from Theta. We never touch the order ticket.
  Pre-fill is a gray zone; placing via API is not.
- **STATUS: OPEN — design constraint** — confirm no order pre-fill via
  Schwab API; if pre-fill is necessary, get counsel sign-off.

### 2.3 Options-Specific
- **Options Disclosure Document (ODD)** — SEC Rule 9b-1 + OCC; the
  document "Characteristics and Risks of Standardized Options" must be
  delivered before a customer is approved for options trading. Theta
  doesn't approve users, but if we *recommend* options strategies, the
  ODD obligation falls onto whoever is recommending. Best practice:
  ship the ODD link inside the app and every options lesson.
- **FINRA Rule 2360** — options account approval, recordkeeping,
  position limits, supervision. Hits us only if we cross BD line.
- **FINRA Rule 2210 (b)(2)(B)** — options communications need
  pre-approval by a Registered Options Principal. Hits if BD.
- **Reg BI (Rule 15l-1)** — best-interest standard on recommendations
  for retail customers. Hits if BD; analog under Advisers Act §206
  (fiduciary) if RIA.
- **Strategy-level red flags inside `LESSONS.md`:**
  - L14 "Vertical spreads" — defined-risk multi-leg. Recommending a
    specific spread on a specific ticker = options recommendation.
  - L15 "0DTE / gamma / pin risk" — even teaching the trade-off is OK;
    handing a user a 0DTE setup is *exactly* what FINRA Notice 22-08
    flagged on complex products and 23-12 on 0DTE.
  - L16 "Selling premium / be the house" — naked short options have
    margin and risk requirements; misrepresenting risk = §206(4) /
    Rule 10b-5 territory.
  - L12 "Rolling underwater positions" — defending losers is the
    behavior pattern FINRA and SEC enforcement cite most in retail
    options blow-ups. Lesson is fine *if* framed as defined defense;
    "ROLL / CLOSE / ADD" on a live position card crosses the line.
- **STATUS: OPEN — design constraint** — every options lesson must
  carry an ODD link + "this is education, not a recommendation" frame.

### 2.4 SEC Marketing Rule (Rule 206(4)-1) — only if RIA, but the FTC
analogs apply regardless:
- **Testimonials/endorsements** — written disclosure of material
  conflicts, compensation, and whether the giver is a client.
- **Hypothetical performance** — only to audiences with the means to
  assess. "If you'd taken every Lyra signal, you'd be up X%" is
  hypothetical performance and must follow the rule.
- **Past performance** — must be net of fees, time-weighted, in
  specific formats. If we *ever* show a track record, every digit is
  regulated.
- **STATUS: OPEN.**

### 2.5 Digital Engagement Practices (gamification)
- SEC RFI Aug 27 2021 (Release No. 34-92766) on DEPs in retail
  investing. Not a rule yet, but signals enforcement risk.
- **Massachusetts A.G. vs. Robinhood** — gamification cited as
  unsuitable inducement; settled March 2024 ($7.5M + remediation).
- **NY Senate Bill S8588** (proposed) — restricts gamification in
  retail brokerage UIs.
- **Theta-specific exposures:**
  - "XP / streaks / trust meter" — DEP signals.
  - "Coach intercepts a revenge trade" — actually a *positive* design;
    document this as an anti-DEP control.
  - "Scanner unlock at L20" — the prize-gate framing is the highest-
    risk line. Reframe as "competency gate" + appropriateness check
    (UK FCA already requires this for High-Risk Investments under
    PS22/10).
- **STATUS: OPEN — design constraint** — re-spec the gamification as
  competency gates, not slot-machine reward loops; capture the
  intercepts (revenge trade L6, naked-option blocker L14, 0DTE
  blocker L15) as the defense in any future enforcement letter.

### 2.6 AI / Predictive Data Analytics
- **SEC proposed Rule 211(h)(2)-4 / 15l-2** (July 2023, "Reg PDA") —
  would require addressing/eliminating conflicts where a
  predictive-analytics or AI system places the firm's interest ahead
  of the investor's. Not finalized; trajectory matters.
- **"AI washing"** — SEC Enforcement actions against Delphia (USA)
  and Global Predictions (March 2024) for falsely claiming AI use.
  Don't market "AI coaches" if they're scripted; don't market them
  as "scripted personalities" if they're LLM outputs. Be exact.
- **NY DFS, NIST AI RMF, EU AI Act** — see §10.
- **STATUS: OPEN** — needs decision on AI vs. scripted (DESIGN.md §3b).

### 2.7 State Blue Sky + State RIA
- State RIA registration applies under $100M AUM. With no AUM, the
  internet-adviser exemption is the relevant federal-pre-emption
  route, but it pre-empts state *registration*, not state *notice
  filing* or state anti-fraud. Each state still has anti-fraud.
- High-friction states for fintech: NY (DFS), TX (TSSB), MA (Sec'y),
  CA (DFPI). Expect investigative letters if the marketing is loud.

---

## 3. United States — Consumer / Commercial / Financial

### 3.1 GLBA + Reg S-P (17 CFR Part 248)
- Once Theta receives a Schwab access token, we're handling NPI
  (non-public personal information). Even read-only.
- Required: initial privacy notice, annual notice, opt-out for
  sharing with non-affiliated third parties, written safeguards
  policy (Reg S-P amendment Nov 2024 added incident-notification
  obligations: 30 days, with content requirements).
- **STATUS: NEEDS COUNSEL** — depends on whether Theta is a "financial
  institution" under GLBA; the answer is likely yes the moment we
  hold the Schwab token.

### 3.2 FTC ROSCA (Restore Online Shoppers' Confidence Act)
- 15 USC §8403: any "negative option" (auto-renewing subscription)
  needs (i) clear material terms, (ii) express informed consent
  before charge, (iii) simple cancel mechanism.
- FTC "Click-to-Cancel" Rule (16 CFR Part 425), effective rolling
  through 2025 — requires cancel as easy as sign-up.
- **STATUS: OPEN — design constraint** — subscription page + in-app
  cancel flow must comply day one.

### 3.3 California ARL (Bus. & Prof. Code §17602)
- Strictest US state auto-renewal law; clear-and-conspicuous offer,
  affirmative consent, ack email, simple in-state cancel method.
- New 2024 amendment: every-3-year reminder for long-running subs.
- **STATUS: OPEN — design constraint.**

### 3.4 FTC Endorsements & Testimonials (16 CFR Part 255)
- Material connections disclosed; "results not typical"; can't claim
  endorsement from a non-user.
- Influencer marketing: if Theta pays creators, each post must
  disclose. FTC has enforced (Lord & Taylor 2016, CSGOLotto 2017).
- **STATUS: OPEN.**

### 3.5 CCPA / CPRA, plus VA / CO / CT / UT / TX consumer-privacy laws
- Right to know / delete / correct / opt-out of sale or share /
  limit use of sensitive personal info.
- Brokerage/financial info is "sensitive personal information"
  under CPRA — heightened.
- Required: privacy policy, "Do Not Sell or Share" link, consumer
  request workflow, vendor DPAs.
- **STATUS: OPEN.**

### 3.6 COPPA + 18+ age gate
- Options can only be traded by adults; Schwab's options approval
  is 18+. Theta should age-gate at signup (18+).
- COPPA (under 13) is binary — best practice: hard 18+ gate, screen
  out under-18 entirely. Avoid the COPPA regime altogether.
- **STATUS: OPEN — design constraint.**

### 3.7 ADA / WCAG 2.1 AA
- DOJ March 2024 final rule under Title II clarifies WCAG 2.1 AA for
  state/local gov; private commercial apps still litigated under
  Title III with WCAG 2.1 AA as the de facto standard (Robles v.
  Domino's, 9th Cir. 2019). Pure-mono terminal UI has known a11y
  risks: color contrast (off-white #eef6f3 on #000000 is fine at
  ~17:1; cyan #4fd1e6 ~10:1 — both pass), but mono and dense
  scan blocks risk screen-reader semantics and dynamic-text scaling.
- **STATUS: OPEN — design constraint** — bake VoiceOver/TalkBack
  semantics into the terminal UI from day one.

### 3.8 Money transmission (not currently triggered)
- No fund custody, no payments processing → no MSB / state MT
  license. STATUS: CLOSED *for now*. Re-open if we ever take
  payments outside Apple/Google billing for managed money.

---

## 4. Brokerage Integration (Schwab)
- **Schwab Developer Portal ToS** — read in full before token flow;
  typical clauses: no reselling data, no order-routing without
  separate agreement, attribution, rate limits, security review.
- **Reg S-P amendments (Nov 2024)** — incident notice within 30 days
  to affected individuals; written incident-response plan.
- **OAuth handling** — Schwab tokens are bearer credentials; treat
  as PCI-grade. Vault (AWS Secrets Manager / GCP Secret Manager /
  HashiCorp Vault), rotate, log access.
- **"Effecting transactions" line** — deep-link only; do not pre-fill;
  do not hold pending tickets; do not represent to user that the
  order will be placed by Theta.
- **STATUS: NEEDS COUNSEL + ENGINEERING.**

---

## 5. International Markets

### 5.1 United Kingdom — FCA
- **FSMA 2000 s.21** — financial promotions must be made or approved
  by an authorized person; criminal offense otherwise (max 2 years
  + unlimited fine). Includes apps available in the UK.
- **FCA PS22/10** — High-Risk Investments rules. Options are
  "Restricted Mass Market Investments" → personalized risk warnings
  ("90% of retail investors lose money trading…" style),
  appropriateness assessment, 24-hour cooling-off period, ban on
  incentives to invest.
- **FCA PS23/6** — financial promotions of cryptoassets (not Theta
  unless we add crypto options).
- **FCA Consumer Duty (PS22/9)** — outcomes-based duty for retail
  products; documentation required.
- **Approver Gateway** — since Feb 2024, only firms specifically
  authorized to approve s.21 promotions can do so. Find one early.
- **STATUS: OPEN — pre-launch blocker for UK availability.**

### 5.2 European Union — MiFID II / PRIIPs / MAR
- **MiFID II** — providing investment advice or receiving/transmitting
  orders requires authorization in a member state (passporting).
- **PRIIPs Regulation 1286/2014** — Key Information Document (KID)
  required for "packaged retail and insurance-based investment
  products"; listed options are exempt as such, but structured
  products and CFDs are not. Confirm Theta never recommends
  structured products to EU retail.
- **MAR (596/2014) Article 20** — investment-research production +
  dissemination rules. "Recommending" instruments triggers Article
  20 + the Commission Delegated Regulation (EU) 2016/958: objective
  presentation + disclosure of conflicts, plus retention of evidence.
- **ESMA product intervention** — banned binary options for retail,
  capped CFD leverage; options sit close to this in regulator mind.
- **STATUS: OPEN — pre-launch blocker for EU availability.**

### 5.3 Canada — CIRO + provincial securities commissions
- **National Instrument 31-103** — registration of advisers, dealers,
  investment fund managers; categories include Portfolio Manager and
  Exempt Market Dealer.
- **CIRO** (formed Jan 2023, IIROC + MFDA merger) — SRO for
  investment dealers.
- **OSC, AMF (Quebec)** — particularly active enforcers.
- **STATUS: OPEN.**

### 5.4 Australia — ASIC
- **AFSL (Australian Financial Services Licence)** — required to
  provide financial product advice or deal in financial products to
  Australian retail clients. Options are a financial product.
- **Design and Distribution Obligations (Corporations Act Part 7.8A)**
  — Target Market Determination (TMD) for each product; ASIC
  product-intervention powers used on binary options.
- **STATUS: OPEN.**

### 5.5 Singapore (MAS) — Financial Advisers Act + Securities and
Futures Act. CMS licence may be required.
### 5.6 Hong Kong (SFC) — Type 4 (advising) and Type 1 (dealing)
licences.
### 5.7 Japan (FSA / JSDA) — registration as Type II FIBO; very high
bar for foreign apps.
### 5.8 UAE (SCA), Saudi (CMA), Brazil (CVM) — each has its own
perimeter for non-resident financial promotion.

### 5.9 Geofencing strategy (the single cheapest control)
- App Store / Play Store both support country-by-country availability.
- IP-block + payment-country-block as a backstop.
- VPN users: explicit ToS clause + geo-fence the *scanner content*
  on the server, not just the app binary.
- **RECOMMENDED day-one geography: US only**, with a waitlist for UK
  and Canada. Add jurisdictions after counsel + filings.
- **STATUS: OPEN — design constraint.**

---

## 6. Privacy — International
- **GDPR (EU/UK GDPR + DPA 2018)** — lawful basis (likely contract +
  legitimate interests + consent for marketing), DPIA for profiling,
  DPO if scale warrants, SCCs/IDTA for transfers, breach notice 72h.
- **PIPEDA** (Canada), **LGPD** (Brazil), **POPIA** (South Africa),
  **APPI** (Japan), **PDPA** (Singapore).
- **Cross-border transfer** — EU-US DPF certification (DOC + ITA),
  UK Extension to DPF, SCCs as backup.
- **STATUS: OPEN.**

---

## 7. App Store Policies
### 7.1 Apple App Store Review Guidelines
- **§1.1.6** — no false information / features.
- **§3.1.5(b)** — financial trading apps must be submitted by the
  legal entity that provides the services, and must include the
  necessary licensing/permissions for the regions of distribution.
- **§5.2.1** — apps offering financial services may be required to
  provide evidence of authorization.
- **§5.1** — privacy + data minimization.
- **STATUS: OPEN — submission blocker without licensing evidence.**

### 7.2 Google Play
- **Financial Services policy** — apps offering or facilitating
  personal loans, options/CFDs/forex/crypto have additional
  requirements (disclosures, country availability, sometimes
  documentation of authorization).
- **STATUS: OPEN.**

---

## 8. Marketing / Advertising
- **FINRA Rule 2210** — if BD; pre-use approval for retail comms;
  options communications need Registered Options Principal sign-off.
- **SEC Marketing Rule 206(4)-1** — if RIA; covers testimonials,
  endorsements, third-party ratings, performance.
- **FTC Endorsements Guide (16 CFR 255)** — even outside SEC, the
  FTC governs paid creator marketing.
- **NAD / BBB self-regulation** — competitor challenges (low priority
  early).
- **STATUS: OPEN.**

---

## 9. "Capital Mind" upstream feed (DESIGN.md §3b-1 names this)
- Open questions:
  - Capital Mind's own regulatory status (RIA? Newsletter? Foreign?).
  - License terms — are we permitted to re-display? White-label?
  - If they call buys and we re-publish, are we now distributing
    *their* advice (does our publisher's-exemption analysis stand)?
  - Is the data feed real-time market data? Real-time data often
    has exchange license requirements (CTA / UTP / OPRA).
- **STATUS: OPEN — needs upstream contract review.**

---

## 10. AI-Specific
- **SEC "AI washing"** — Delphia + Global Predictions, March 2024
  ($400k combined). Don't overstate AI; don't hide it either.
- **SEC Reg PDA (proposed, 2023)** — conflict-of-interest rules for
  predictive analytics in advisory.
- **EU AI Act (effective Aug 2024, phased through 2026)** —
  classification of AI systems; financial-advisory AI likely
  "high-risk" under Annex III; conformity assessment + post-market
  monitoring + transparency obligations.
- **NIST AI RMF 1.0** — voluntary US framework; expected baseline.
- **NY AI bias audit (Local Law 144)** — employment-only, not
  relevant unless we use AI for our own hiring.
- **STATUS: OPEN.**

---

## 11. Tax / Entity / Corporate
- **Entity** — Delaware C-Corp if any chance of raising; LLC if
  bootstrapped indefinitely. Resident-state qualifications.
- **Sales tax / VAT on digital subscriptions** — Apple/Google handle
  most via app store, but in-house web checkout requires Quaderno-
  style VAT / GST handling.
- **§1256 contracts (US)** — broad-based index options are §1256
  60/40 (long-term/short-term). Equity options are not. Lessons
  should not characterize tax treatment unless reviewed.
- **STATUS: OPEN.**

---

## 12. Intellectual Property
- **"Theta" trademark** — USPTO TESS search for IC 036 (financial)
  + IC 041 (education). The Greek letter is unregistrable, but the
  word THETA may have prior users in fintech.
- **Coach names — Lyra, Nestor, Chiron, Atlas** — mythological,
  public domain.
- **IBM Plex Mono** — Open Font License (SIL OFL 1.1) — clean.
- **Stoic content** — Marcus, Seneca, Epictetus public domain;
  modern translations are not. Use Long / Hard / Gregory Hays
  translations only with permission, or paraphrase.
- **"Capital Mind"** — third-party mark; using their name in app
  requires a trademark license or careful nominative-fair-use.
- **STATUS: OPEN.**

---

## 13. Highest-priority red flags from `DESIGN.md` / `LESSONS.md`

| ID | Section | Issue | Status (2026-05-20) |
|----|---------|-------|--------------------|
| RF-01 | `§3b-1` `holdings (n)` block + `pipeline buy signals` | User-portfolio-aware buy signals = personalized investment advice; breaks publisher's exemption. | **RESOLVED BY DESIGN.** Scanner runs only the user's own strategy (tool of the user); aggregated brokerage data feeds journal/adherence only, never the scanner or LLM. See DESIGN.md §2.5 C. |
| RF-02 | `LESSONS.md` L4 / L14 / L15 / L16 | Specific options strategies recommended in-product (vertical spreads, premium-selling, 0DTE) without ODD delivery. | **RESOLVED BY DESIGN.** Strategies are *taught* (education), not recommended; user builds their own. ODD link in every options lesson as belt-and-suspenders. DESIGN.md §2.5 B / I + PEDAGOGY.md. |
| RF-03 | `§3b-1` `schwab token` + `OPEN BROKERAGE` button | Brokerage credential + execution funneled; Reg S-P + Schwab ToS + §3(a)(4) gray zone. | **RESOLVED BY DESIGN.** Deep-link only; no order placement; read-only OAuth aggregation (post-bootstrap) with Reg S-P safeguards; no broker referral fees. DESIGN.md §2.5 F. |
| RF-04 | Gamification: XP / streaks / scanner-as-prize / coach intercepts | SEC DEP scrutiny, MA Robinhood precedent, NY proposed law. | **RESOLVED BY DESIGN.** Reframed as competency gate + behavioral coaching; adherence-score leaderboards only (no return-based). Intercepts (revenge-trade L6, naked blocker L14, 0DTE blocker L15) documented as defenses. DESIGN.md §2.5 G. |
| RF-05 | Four "AI coaches" framing | If AI, Reg PDA + EU AI Act exposure; if scripted, AI-washing if marketed as AI. | **DRAFTED 2026-05-20.** `compliance/marketing-rules.md` is the operative control: forbidden phrases + approved language + mandatory disclosure + pre-publication checklist. Lead with character (Lyra/Nestor/Chiron/Atlas), not technology. Apply checklist before publishing any public-facing copy. |
| RF-06 | "Capital Mind" upstream feed | Re-publishing third-party advice; upstream license + their reg status. | **RESOLVED BY DESIGN.** Scanner runs the user's own strategy, not Capital Mind picks. Theta needs only clean delayed-data feeds (IEX, Polygon delayed, Tradier, Schwab developer API). Capital Mind drops out of the architecture. |
| RF-07 | Cross-border by default (no geofence) | UK s.21 (criminal), MiFID II, ASIC AFSL, CIRO exposure on day one. | **RESOLVED.** US-only geofence via App Store / Play Store country restrictions + IP block + payment-country check + ToS clause. DESIGN.md §2.5 H. |
| RF-08 | No risk-disclosure track in storyboards | Options risk warning, "education not advice," "past performance," "results not typical" not yet in any frame or screen. | **DRAFTED 2026-05-20.** `legal/risk-disclosure.md` (full modal copy, scrollable + accept-required on first launch) + `legal/persistent-disclaimers.md` (12 catalogued footer/banner/disclaimer strings for every disclaimed surface, including ODD link). Counsel review pending before production use. |
| RF-09 | Subscription auto-renewal compliance | ROSCA + CA ARL + FTC Click-to-Cancel. | **DRAFTED 2026-05-20.** `legal/subscription-terms.md` — six required disclosures at point of purchase, affirmative consent, post-purchase confirmation, in-app cancel routing, renewal reminders, plan-change notice, governing-law placeholders. Apple/Google handle most flows; in-app cancel UX still needs implementation. |
| RF-10 | "Coach goes live" + paper-trade handshake + L20 unlock framing | Reinforces influencer/guru pattern under SEC influencer enforcement. | **RESOLVED BY DESIGN.** L20 unlocks the SaaS tier (user's own strategy in the scanner), not "live tips." Coach teaches forever; never picks. DESIGN.md §2.5 A (L20 corrected). |
| RF-11 | No 18+ age gate spec'd | COPPA + options-eligibility (18+) + Stoic discipline alignment. | **DRAFTED 2026-05-20.** `legal/age-gate-spec.md` — full implementation spec: DOB-first signup, branch logic, refusal screens R-1 (13–17) and R-2 (<13) with no PII collection, 24-hour device cool-down on refusal, engineering acceptance criteria. Implementation pending. |
| RF-12 | "Theta" trademark not searched | Possible prior-user blocking commercial use in financial services. | **PARTIAL RESOLUTION 2026-05-20.** DIY first-pass complete: see `compliance/trademark-tess-pass-2026-05-20.md`. **Material finding:** bare "Theta" has descriptiveness concerns (Trademark Act §2(e)(1) — theta = generic options term) AND existing direct competitor Theta Trading Co. (Stock Options Academy, ~1,300+ students). Recommendation: shift trademark strategy to (a) stylized Θ design mark + (b) distinctive compound word mark, or (c) rebrand if counsel clearance fails. Counsel clearance opinion ($500–$1.5k) required before public launch. |

---

## 14. Investigation plan — next 10 steps
1. Lock §1 characterization (Gee decision; default = B + paper-trade + deep-link).
2. Lock §5.9 geography day-one (default = US only with waitlist elsewhere).
3. Decide AI vs. scripted (§2.6 / §10) and write it into `DESIGN.md`.
4. Engage US securities counsel with options + retail-app experience.
   (Suggested firms: WilmerHale, K&L Gates fintech, Lowenstein Sandler
   options, ACA Group for ongoing compliance.)
5. USPTO TESS search on "Theta" in IC 036 + IC 041.
6. Get Capital Mind's regulatory status + redistribution license.
7. Draft Risk Disclosure, Terms of Service, Privacy Policy
   (US-first; UK + EU before adding those countries).
8. Re-audit `DESIGN.md §3b-1` against §2.1 of this doc — every
   home-screen field gets tagged "impersonal OK" or
   "personalization risk."
9. Re-audit `LESSONS.md` L2–L19 against §2.3 — every recommendation
   gets a "this is education, not a recommendation" frame.
10. Bake risk disclosure into the production-template storyboard
   (RF-08) before any video is rendered.

---

## 15. Status legend
- **OPEN** — issue identified, design decision pending.
- **NEEDS COUNSEL** — requires actual licensed attorney sign-off.
- **CLOSED** — resolved with cite + rationale.

Every entry above is **OPEN** or **NEEDS COUNSEL** by default. None
**CLOSED** yet.

---

## 16. Decisions log
Per `theta/memory/MEMORY.md` convention; one file per resolved
issue in `theta/compliance/decisions/` named
`<YYYY-MM-DD>_<short-slug>.md`. Major locks to date:
- `2026-05-20_initial-bootstrap-scope.md` — threshold answers + the
  20-item bootstrap playbook.
- `2026-05-20_compliance-arch.md` — the strategy-tool + strategy-
  education architecture; characterization resolved; eight red flags
  closed by design.

---

## 17. The middle-position playbook
*Where Theta lives between the user and their broker, legally.*

Execution sits at the broker (Schwab). Everything around execution
— the days and weeks of strategy design, decision-making, record-
keeping, and reflection — is the open ground where Theta operates.
Brokers are bad at all of it. That's the gap.

### Three zones around execution
- **Pre-trade.** Strategy design, scanning the user's strategy,
  idea analysis (data + mechanics + adherence + behavioral), paper-
  trade testing, behavioral pressure-test. Theta's home base.
- **Post-trade.** Trade journal, adherence scoring against the
  user's own rules, behavioral analytics, retrospective coaching.
  The biggest untapped value real estate; the long-term SaaS moat.
- **Companion.** Two apps open — Theta on the left showing the
  user's strategy and journal; Schwab on the right showing the
  order ticket. The user integrates in their head. No legal issue.

### Surfaces Theta can legitimately claim
Each has commercial precedent as unregistered SaaS:

| Surface | Description | Commercial precedent |
|---------|-------------|----------------------|
| Strategy builder | User constructs strategy from atomic components | Tastylive research, thinkorswim Scan |
| Scanner | Runs user's strategy on delayed data, returns matches | Finviz, TradingView, Trade Ideas, TC2000 |
| Paper-trade simulator | Delayed-data trades with realistic frictions | thinkorswim PaperMoney, Tastytrade Paper, Webull Paper |
| Backtesting | User's strategy across historical data, with hypothetical-performance disclaimers | TradingView Pine Script, Backtrader, Quantrocket |
| Strategy versioning | Track every iteration of the user's strategy | No mainstream analog — Theta-original |
| Risk calc / Greeks viz | Payoff diagrams, breakeven, position sizing | OptionStrat, Options Profit Calculator |
| Trade journal | Manual or CSV import → eventual OAuth read-only | Edgewonk, Tradervue, Trademetria, Chartlog |
| Adherence scoring | User's actual trades vs. user's stated rules | No mainstream analog — Theta-original |
| Behavioral analytics | Patterns in the user's own behavior over time | No mainstream analog at this depth — Theta-original |
| Economic calendar | Public events with strategy overlay | Earnings Whispers, Investing.com calendar |
| Tax-aware exports | Format for tax software, wash-sale flags (educational only) | TaxBit (crypto), TurboTax import tools |
| LLM coach | Strategy teacher + retrospective coach over all of the above | No analog — Theta-original |

### The Schwab read-only OAuth pattern (the killer middle play)
**Pattern:** user authorizes OAuth read-only access → Theta pulls
trade history → journal auto-populates → adherence scoring runs on
real trades → coach reviews real behavior. Theta never writes back.

**Precedent:** Mint, YNAB, Personal Capital (the aggregator
business, not their RIA arm), Empower, Copilot Money, Monarch.
Plaid intermediates this exact pattern for hundreds of fintechs.
None of these are broker-dealers. Read-only data aggregation is
regulatorily settled.

**Compliance overhead:**
- Schwab Developer Portal application + approval.
- Reg S-P / GLBA safeguards (privacy notice, encryption at rest,
  access logging, incident response — see §3.1 and §4 above).
- The cardinal rule: **aggregated data feeds the journal/adherence
  scorer ONLY.** The LLM coach and the scanner do not see it.
  Cross-pollinating ("we noticed you're long NVDA, here's an iron
  condor on NVDA") moves us from aggregator to adviser. Hard wall
  in the architecture.

**Bootstrap sequencing:**
1. Day one: CSV import. User exports Schwab activity, drops into
   Theta. No Schwab dependency. Edgewonk built $7M+ ARR on CSV-
   only.
2. Once we have product traction: apply for Schwab read-only OAuth,
   pass security review, ship integration. Paid-tier feature.

### Bright lines (re-stated in middle-position context)
- No order placement (broker line).
- No fund holding (broker + MSB line).
- No cross-pollination of aggregated brokerage data into the LLM
  coach or the scanner.
- No editorial overlay on scanner output.
- No pre-canned strategies users select one-click.
- No broker referral fees (Cash Solicitation Rule / finder fees).
- No strategy marketplace where users sell each other strategies.
- No copy-trading.
- No cash-prize leaderboards for paper-trade returns.

These are restated from DESIGN.md §2.5 G because they are *the*
constraints that keep Theta inside the middle-position SaaS box and
out of the BD / RIA boxes.
