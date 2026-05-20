# Decision — Compliance Architecture lock (2026-05-20, Gee)

This is the major architecture lock that emerged from the compliance
investigation chats on 2026-05-20. Backpointers:
- `theta/DESIGN.md §2.5` — locked design section.
- `theta/compliance/COMPLIANCE.md §0 / §1 / §13 / §17` — updated.
- `theta/ai/PEDAGOGY.md` — the teaching architecture this protects.

## Characterization resolved
Theta is a **strategy tool + strategy education** product, sold as
**SaaS**. Specifically:
- **LLM coach** — teaches strategies (education, not advice).
- **Scanner** — runs the user's *own* strategy (tool of the user,
  not adviser).
- **Paper-trade simulator** — lets the user test their strategy
  against delayed-but-real market data.
- **Trade journal + adherence scorer** — analytics on the user's
  own behavior; eventually populated via Schwab read-only OAuth.
- **Schwab deep-link** — execution lives at the user's broker,
  never inside Theta.

This combination requires neither investment adviser registration
nor broker-dealer registration under settled commercial precedent
(Finviz, TradingView, OptionStrat, Edgewonk, Tradervue, tastylive's
education arm, OptionAlpha's pre-RIA education business, etc.).

## L20 corrected meaning
**L20 unlocks the SaaS tier** — the user has built their own
strategy and earns the right to run it through the scanner. It does
NOT unlock real-time data, and it does NOT switch the primary
action from paper-trade to brokerage. The user keeps access to the
scanner of their own strategy inside the SaaS subscription forever.

Supersedes the earlier `DESIGN.md §3b-1` "after L20 open-brokerage
becomes the primary action" framing.

## Locked architectural decisions
### A. Two-tier product
- Tier 1: Education on-ramp (lessons + paper-trade on templated
  setups). Lower-priced or free.
- Tier 2: Theta SaaS (the ongoing business) — strategy builder,
  scanner running user's strategy, paper-trade, backtesting,
  versioning, journal, adherence, behavioral analytics, coach,
  deep-link.

### B. The LLM contract
- Provides: data + mechanics + strategy-fit check + behavioral
  inquiry.
- Never: verdicts, picks, predictions, math computation.
- Numerical work via deterministic tools; LLM narrates.
- Memory: stateful for strategy rules; stateless for holdings.

### C. Scanner contract ("tool of the user")
- Runs only the user's own strategy.
- Deterministic, explainable, no editorial overlay.
- No "top picks" / "Theta Score" / "best setups."
- Safety constraints (warn on undefined risk) are tool features,
  not advice.

### D. Data tier
- **15-minute delayed, throughout Theta, forever.**
- Real-time lives at the user's broker, not inside Theta.
- Marketing line: "Theta uses 15-minute data because we don't
  trade the second — we trade the strategy." A feature, not a
  limitation. Especially valid because the curriculum targets 45+
  DTE strategies where the 15-min lag is functionally invisible.

### E. Paper-trade simulator
- Realistic fills (buys at ask / sells at bid or worse, never
  mid-quote).
- Realistic frictions (commissions, fees, assignment, slippage).
- Mandatory hypothetical-performance disclaimer.

### F. Brokerage relationship
- Deep-link only. No order placement.
- Read-only OAuth aggregation for journal/adherence (post-bootstrap,
  with Reg S-P safeguards). CSV import day one.
- **No broker referral fees.** Avoids Cash Solicitation Rule /
  finder-fee complications.

### G. Hard red lines (still)
- No order execution.
- No fund holding.
- No personalized recommendations from the LLM coach.
- No specific-ticker calls in coach videos / marketing.
- No editorial overlay on the scanner.
- No pre-canned strategies with one-click selection.
- No track-record or return claims about Theta or its users.
- **No strategy marketplace (peer-to-peer publishing).**
- **No copy-trading.**
- **No cash-prize leaderboards for paper-trade P&L.** Adherence-
  score leaderboards are acceptable — they reward discipline, not
  returns.
- No marketing of "AI" until every claim is defensible.
- No availability outside the US on day one.

### H. Pedagogy as moat
The strategy-teacher LLM is the *real* defensible product as AI
commoditizes. Detailed architecture in `theta/ai/PEDAGOGY.md`:
- Curriculum graph (not flat prompts).
- Deterministic math (narrated).
- RAG from curated content library.
- Voice/character enforced.
- Mastery model + spaced repetition.
- Self-improvement loop (the data flywheel).
- Model-agnostic so the engine is swappable.

## Red flags resolved by this lock
From `COMPLIANCE.md §13`:
- **RF-01** (personalized advice via scanner holdings block) —
  RESOLVED. Scanner runs only the user's own strategy; aggregated
  brokerage data feeds journal only, never the scanner or LLM.
- **RF-02** (options strategies recommended without ODD) — RESOLVED
  BY DESIGN. Strategies are *taught* (education), not recommended.
  ODD link in every options lesson as belt-and-suspenders.
- **RF-03** (Schwab token + OPEN BROKERAGE button) — RESOLVED BY
  DESIGN. Deep-link only; no order placement; read-only OAuth
  with Reg S-P safeguards; no referral fees.
- **RF-04** (gamification) — RESOLVED BY DESIGN. Reframed as
  competency gate + behavioral coaching. Discipline leaderboards
  only.
- **RF-06** (Capital Mind upstream dependency) — RESOLVED BY DESIGN.
  Scanner runs user's strategy, not Capital Mind picks. Theta only
  needs clean delayed-data feeds (IEX / Polygon / Tradier / Schwab
  developer API).
- **RF-07** (cross-border exposure) — RESOLVED. US-only geofence.
- **RF-10** (coach-goes-live + L20 unlock framing) — RESOLVED BY
  DESIGN. L20 unlocks SaaS tier, not "live tips." Coach teaches
  forever.

## Red flags still open
- **RF-05** — AI coaches framing. Addressed via PEDAGOGY.md
  architecture + "don't market as AI" rule. Still requires care in
  marketing.
- **RF-08** — Risk-disclosure track in storyboards. Open; needs
  drafting (Risk Disclosure modal copy, persistent footer, ODD
  links in lessons).
- **RF-09** — Subscription auto-renewal compliance. Open; mostly
  handled by Apple/Google billing flows + ToS work.
- **RF-11** — 18+ age gate. Open; implementation work.
- **RF-12** — "Theta" trademark search in IC 036 / IC 041. Open;
  DIY USPTO TESS pass + follow-up clearance opinion before public
  launch.

## Trigger events to revisit
- 5,000 paying US users → engage US securities counsel for a clean
  opinion letter on the locked architecture.
- Any plan to add a country (UK / CA / EU / AU) → engage local
  counsel before any marketing reaches that country.
- Any plan to take payments outside Apple/Google → ROSCA + state
  ARL review.
- Any marketing line implying returns, performance, or track
  record → marketing-rule review before publication.
- Any new feature that touches order placement, fund holding, or
  third-party-strategy publication → architecture review against
  the red lines above.
