# Theta — Pedagogy & AI Architecture (LIVING)

Parallel to `DESIGN.md` and `compliance/COMPLIANCE.md`. This is the
how-we-teach spec. It is the **defensible IP layer of Theta** — the
part that survives and compounds as model capability commoditizes.

> **Load-bearing principle (LOCKED 2026-05-20, Gee).** The LLM is a
> substrate, not the product. The pedagogy, character, curriculum
> graph, content library, mastery model, and data flywheel are the
> product. We design model-agnostic from day one: when GPT-5 or
> Claude 5 ships, we drop it in and Theta gets better, not different.

---

## 1. The defensibility thesis
- 2026: dozens of "AI tutor for X" wrappers exist; most are thin
  prompts on top of an API.
- 2027–2028: a 12-month moat at the model layer evaporates. Generic
  chatbots become competent at explaining iron condors.
- 2029+: the products that survive are the ones whose moat is *above*
  the model layer — proprietary curriculum, character, content
  library, mastery models, and a data flywheel from real student
  interactions.
- **Theta's bet:** build the pedagogy moat now, while everyone else
  is still on the model wrapper. Each month of paid users compounds
  the flywheel. By the time models are commoditized, the content +
  mastery model + character + community are uncatchable.

---

## 2. The teaching contract (what the LLM is and is not allowed to do)
Strict scope, set in lockstep with `DESIGN.md §2.5 B` and
`compliance/COMPLIANCE.md §0`:

**The LLM does:**
- Teach the *why* and *how* of options strategies and concepts.
- Analyze user-brought trade ideas using: data + mechanics +
  strategy-fit check + behavioral inquiry.
- Coach retrospectively on the user's own paper-trade and journaled
  real-trade history.
- Stay in coach character (Lyra / Nestor / Chiron / Atlas).

**The LLM does NOT:**
- Give verdicts on whether a specific trade is good or bad.
- Pick trades for the user.
- Compute P&L, Greeks, or option prices — those go through
  deterministic tools and the LLM narrates the result.
- See the user's brokerage holdings. Aggregated data feeds the
  journal / adherence scorer only.
- Predict price direction or claim performance.

This is the same contract the compliance investigation defined; it
is restated here because the teaching architecture must enforce it
mechanically, not just by polite system-prompt instruction.

---

## 3. The six architectural decisions that separate competent from excellent

### 3.1 Curriculum graph, not flat prompts
Every concept (delta, theta, gamma, vega, IV rank, vertical spread,
iron condor, the wheel, calendars, diagonals, etc.) becomes a node
in a knowledge graph. Each node carries:
- **Prerequisites** (you can't teach gamma before delta).
- **Related concepts** (theta ↔ vega; vertical spread ↔ iron condor).
- **Common misconceptions** with the exact correction.
- **Embodied metaphors** (theta = daily tax; gamma = steering).
- **Worked examples**, three+ per concept at increasing complexity.
- **Failure modes** — when this concept gets traders blown up.
- **Mastery assessment** — the application question that proves the
  user got it.

The LLM does not recite a fixed lesson. It navigates the graph
adaptively based on what the user has and hasn't grasped. The graph
is proprietary IP. Build it once; refine it forever.

### 3.2 Deterministic math, narrated
The LLM never computes numbers. A typed tool layer handles:
- Black-Scholes / binomial option pricing.
- Greeks (delta, gamma, theta, vega, rho).
- P&L curves for any strategy structure.
- Breakeven, max profit, max loss.
- Implied vs. realized volatility statistics.
- Probability-of-touch, probability-of-profit.
- Position sizing math from the user's account size + risk rule.

The LLM reads tool output and explains it in coach voice. Math
correctness becomes a function of code, not of the model. This
removes the one class of hallucination that would (a) break user
trust catastrophically and (b) create §206(4) anti-fraud exposure.

### 3.3 Retrieval-augmented from a curated content library
The LLM cites from a library we build and own:
- Worked examples for every strategy.
- Anonymized historical scenarios + how each played out.
- Greek explanations at three depth levels (intuitive, applied,
  mathematical).
- Stoic source texts (public-domain translations) + connection notes.
- Misconception catalog with corrections.
- Tax treatment (educational, not advisory) per instrument class.
- Strategy failure case studies.

Architecture: vector store + structured metadata. When the user
asks about iron condors, the LLM retrieves the relevant nodes,
worked examples, and misconceptions, then composes the response in
coach voice. The library is the content moat. Grows monthly.

### 3.4 Voice and character as enforced contract
Each coach has:
- A canonical voice profile: sentence length, rhythm, lexicon,
  default emotional temperature, preferred metaphor families.
- A system-prompt segment that enforces the voice.
- An evaluations suite that catches voice drift over time.

Voice is brand. Users return to Lyra because Lyra speaks a specific
way no other product replicates. As models commoditize, voice is
the most durable moat. The framing matters: the product is not
"options education powered by AI" — it is *Lyra teaches you
options*.

### 3.5 Mastery model + spaced repetition
Track per-concept-per-user mastery on a five-step scale:
1. Not started
2. Exposed (saw the concept)
3. Applied once (used it correctly in a worked example)
4. Applied multiple times across contexts
5. Explained back (Feynman test passed)

Concepts at step 2–3 come back in new contexts at Anki-style
intervals (1d, 3d, 7d, 21d, 60d). The user does not see this as a
quiz layer — they experience it as the coach naturally bringing up
gamma again two weeks later in a different setting.

Almost no AI tutor in 2026 does this well. It is both a meaningful
differentiator AND it produces dramatically better learning outcomes.

### 3.6 Self-improvement loop (the data flywheel)
- Weekly: sample 1–5% of conversations.
- First pass: LLM-as-judge scoring against a golden-example rubric.
- Second pass: human review on the flagged failures.
- Failures become updates to: the system prompt, the content library,
  the misconception catalog, the curriculum graph.
- The product gets measurably better month over month.

This is the part a competitor cannot copy by reading marketing
pages. It compounds. It is the closest thing AI products have to a
classical network effect.

---

## 4. The democratization toolkit
The product mission is to make options strategy genuinely understood
by people without finance degrees. Six teaching rules govern every
piece of content the LLM produces:

1. **Strip jargon, keep rigor.** "Theta" becomes "the daily tax the
   option pays for being alive." The math stays; the jargon goes.
2. **Embodied metaphors that survive months.** Gamma = steering
   responsiveness. Vega = the fear gauge. Delta = roughly the
   probability of finishing in the money. The metaphor is the handle
   the user grabs to retrieve the concept later.
3. **Concrete before abstract.** Every concept opens with a story or
   scenario, not a definition. "If you saw a house that might be
   worth more in six months, would you pay $1,000 today to lock in
   the right to buy it later? That's a call option."
4. **Failure-first.** Teach how a strategy loses before how it wins.
   The trader who knows the failure modes manages against them.
5. **The user owns the artifact.** The strategy they build is theirs,
   written line by line. The journal is theirs. The discipline is
   theirs. They learn because the work is personal.
6. **No shame.** When the user doesn't get it, reformulate — different
   metaphor, different scenario, different angle. The LLM never gives
   up on a user. (Most students give up on finance because the
   *teacher* gave up first.)

Plus three principles from learning science:
- **Active recall** over passive reading.
- **Worked examples** with deliberate fading (full example → partial
  → blank).
- **Interleaving** rather than blocked practice (mix strategy types
  rather than drilling one strategy in isolation).

---

## 5. What the LLM does well + what it can't (yet)

**Real advantages over a human tutor — these are the democratization
equation:**
- **Patience.** Explains the same thing ten different ways without ego.
- **Availability.** 3 AM and 3 PM are the same.
- **Memory.** Never forgets where you were or what worked for you.
- **Calibration.** Adjusts depth and pace per user automatically.
- **Stigma-free.** Users ask the LLM what they'd be embarrassed to
  ask a human — and that's where real learning happens.
- **Cost.** ~$0.01 per session vs. $200/hr for a comparably skilled
  human tutor. Same teaching, one-thousandth the price.
- **Voice consistency.** Stays in coach character across years.

**Real limits (be honest in product about these):**
- **Bullshit detection.** The user claims to understand; doesn't.
  Mastery assessment must catch this; the model alone can't. Open
  problem.
- **Long-term motivation.** Humans need community, accountability,
  rituals. This is why a discipline-community surface eventually
  matters (NOT a strategy marketplace — ruled out for legal reasons
  in COMPLIANCE.md).
- **True innovation.** LLMs interpolate, don't extrapolate. They
  teach the existing canon brilliantly; they don't invent novel
  strategies. This is fine — most traders need the canon, not
  novelty.
- **Compounding empathy across years.** Models do not yet build
  trust the way a long-term mentor does. Character + consistency
  + the data flywheel is the best current substitute.

---

## 6. Model-agnostic principles
Designed so the LLM layer is swappable when better models ship:
- System prompts are portable text; tested against Claude, GPT,
  Gemini before release.
- The content library lives in a vector store + metadata DB
  independent of any model.
- The mastery model lives in our own database.
- The voice profiles are encoded in text, not model weights.
- The deterministic math layer is independent of the model.
- When a new model ships: A/B against the incumbent on the evals
  suite; swap if consistently better. Product gets better; no
  rewrite.

Avoid: fine-tuning that locks us to one provider; model-specific
prompt hacks; reliance on quirks that may not survive a model update.

---

## 7. The data flywheel (compounding moat)
Every conversation produces:
- An evidence point about which explanations work for which user
  type.
- A potential addition to the misconception catalog (when a user
  says something wrong that wasn't caught).
- A potential addition to the worked-example library (when a coach
  invents a particularly good metaphor).
- A potential adjustment to the curriculum graph (when concept A
  consistently requires concept C before concept B).
- An update to the mastery model (when a concept proves harder or
  easier than expected to land).

After 18 months of paying users, the curriculum graph + content
library + misconception catalog become uncatchable by a launch-time
competitor. This is the durable moat.

Privacy/compliance constraint: conversations are stored encrypted;
sampling for improvement is logged; PII is redacted before any
training/eval pipeline; aggregated insights are decoupled from
individual user identifiers. Aligns with Reg S-P safeguards posture
in `compliance/COMPLIANCE.md §3.1 / §4`.

---

## 8. Hardest design problems (open)
- **Voice integration with Lyra's locked deeper warm female register
  (DESIGN.md §3c-1).** TTS quality vs. cost vs. latency tradeoff.
  Options: ElevenLabs (best quality, ~$0.30/min), OpenAI TTS
  (cheaper, less expressive), Anthropic voice (when available).
- **Multimodal explanation: text vs. payoff diagram vs. interactive
  slider.** Which concepts go which way? Some Greeks land via
  slider (drag DTE, watch theta change); others land via story.
- **Behavioral coaching evals.** How do we score "did the coach
  catch the user's revenge-trade impulse well?" Hard to evaluate;
  high leverage.
- **Mastery model bootstrapping.** Day-one users have no history;
  the model has to start somewhere. Diagnostic flow on first session.
- **Bullshit detection.** Already noted; the hardest open problem.
  Approach: forced application + Feynman-test prompts.
- **Coach handoff.** User picks Lyra; later wants to hear Atlas's
  take. How does the system swap coach voice while preserving
  mastery state and journal continuity?
- **When the user is wrong about a strategy concept inside a trade
  question.** Coach must correct without becoming an adviser on the
  trade. Delicate.

---

## 9. Next steps (proposed)
1. Sketch the curriculum graph for L1–L19 — every concept tagged with
   prerequisites, misconceptions, metaphors, mastery checks. Free
   (mermaid).
2. Draft Lyra's voice profile + system-prompt segment. Iterate
   against 20–30 worked-example prompts; check for drift.
3. Define the deterministic-math tool surface (function signatures,
   no implementation yet) — what the LLM is allowed to call.
4. Choose RAG infra (pgvector or Pinecone) and initial schema for
   the content library.
5. Define the mastery model schema and the first five concept
   assessments.
6. Pick an evals harness (Promptfoo, Inspect, or roll our own) and
   write the first 10 golden examples.
7. Write the first five Lyra worked examples end-to-end at production
   quality — these become the seed golden examples for the
   self-improvement loop.

---

## 10. Status legend
Same as `DESIGN.md`: **LOCKED** means decided and load-bearing.
Other items are working drafts open to refinement.
