# Review Response Drafter — Build Spec (v0)

HIPAA-safe review-response drafting for **dental practices**.
Status: spec / pre-build. Branch: `claude/review-response-drafter-rmd0U`.

---

## 1. Positioning

Not "a review tool." The wedge is the one thing generic tools (incl. the
one in the source tweet) get wrong for dentistry:

> A dental practice **cannot legally confirm someone is a patient** in a
> public reply. Generic AI responders routinely write "Thanks for
> trusting us with your cleaning, Jane!" — that is a HIPAA violation
> (improper disclosure of PHI / treatment relationship).

**Value prop:** *"We answer every Google review for your dental practice
— HIPAA-safe, in your voice. You do nothing."*

This is a **fully managed service**, not self-serve software. The
practice does not log in, approve, or post. We ingest their reviews,
draft replies, pass them through the HIPAA gate, and **the operator
(us, running this business) posts them** to the practice's Google
listing. The client's 4–5 hrs/week → zero.

Compliance is the product, not a feature. It is also the moat: it lets us
charge more than a $20 generic SaaS and sell to compliance-nervous office
managers.

Target buyer: dental office manager / practice owner. Pain: 4–5 hrs/week,
plus fear of replying wrong. Volume: a busy practice gets 5–30
reviews/week. **Scope: Google reviews only** (see §2 — Yelp has no
reply API and is not part of the promise).

---

## 2. Scope (decided)

Fully managed, **operator-in-the-loop**, **Google-only**:

- **The client does nothing.** No client login, no client approval, no
  client posting. The practice grants one-time Google access at
  onboarding; after that it's hands-off for them.
- **Operator-in-the-loop:** the operator (us) reviews the gated drafts
  in an internal **operator console** and posts them. The human safety
  net is at *our* cost, not the client's effort. Never the client.
- **Posting to Google requires the Google Business Profile API + the
  practice's OAuth grant.** No compliant shortcut (scripting Google's UI
  violates ToS and flags the listing — fatal for a reputation product).
  This makes the Google API integration **core, not optional**.
- **Yelp is out.** Yelp has no public API to post review replies, by any
  compliant means. The promise is Google-only; do not imply Yelp.
- **Phase 1 (built):** offline drafting + HIPAA gate + the operator
  console, fed by manual paste/CSV. This is the testing/ops harness and
  proves the engine. It is NOT the client-facing product.
- **Phase 2 (required for the promise):** Google Business Profile API —
  auto-pull new reviews + **operator-gated post-back** to Google. This
  is what makes "the client does nothing" true.
- **Drafting: Claude API.** Tone learned from 5–10 of the practice's own
  past replies (or a short brand-voice questionnaire if none exist).

Out of scope: client-facing UI, fully autonomous posting (gate-passes →
live with no human; revisit per-practice once trust is earned), Yelp,
multi-tenant accounts, billing UI, analytics dashboard.

---

## 3. HIPAA guardrails (the core of the product)

The drafting prompt and a post-generation check both enforce these. A
draft that fails the check is regenerated, never shown raw.

Hard rules — a compliant reply must NOT:
- Confirm or imply the person is/was a patient.
- Name, confirm, or describe any treatment, procedure, diagnosis,
  appointment, or visit (even if the *reviewer* mentioned it).
- Use the reviewer's name in a way that ties them to care received.
- Disclose any detail not already public and non-clinical.

Compliant reply pattern (what we steer toward):
- Thank generally, express care for experience, invite private contact to
  resolve specifics ("please call our office at ___ so we can help").
- Negative reviews: empathize, do **not** dispute facts publicly, move
  the conversation offline. Never reveal whether they were seen.
- Positive reviews: warm thanks, reinforce values, **no** treatment echo.

Implementation:
- System prompt encodes the rules + good/bad examples.
- Deterministic post-check: scans draft for treatment/procedure terms,
  patient-confirming phrasing ("your [procedure]", "when you came in",
  "your appointment", "glad we could treat/fix/extract…"). Fail → regen
  with the violation fed back.
- Every draft ships with a one-line "why this is safe" note for the
  approver's confidence.

This section is the spec's source of truth; expand the term list as we
find edge cases. (Note: this is product compliance design, not legal
advice — recommend the practice's own counsel signs off before launch.)

---

## 4. Tone matching

Onboarding (one-time, per practice):
- Preferred: paste 5–10 past replies they liked → model infers voice
  (formality, warmth, sign-off, emoji use, length).
- Fallback (new practice, no replies): 6-question brand-voice form
  (formal↔casual, use first name?, signature line, emoji yes/no,
  typical length, 1–2 phrases they always/never use).

Stored as a per-practice `voice_profile` (JSON) reused on every draft.

---

## 5. Architecture (v1, deliberately small)

```
CSV / pasted text
      │
      ▼
 parser ──► normalized Review[]  (author, rating, text, platform, date)
      │
      ▼
 drafter (Claude API)
   - system: HIPAA rules + voice_profile + examples
   - prompt caching: cache the static HIPAA ruleset + examples block
     (large, identical every call) → big cost saving at volume
   - returns 2 candidate replies + safety note
      │
      ▼
 HIPAA post-check (deterministic) ──fail──► regen (max 2 retries)
      │ pass
      ▼
 OPERATOR CONSOLE (internal — never client-facing)
   edit | confirm | post
      │
      ▼
 Phase 1: operator marks posted (manual paste/CSV harness)
 Phase 2: operator clicks → Google Business Profile API posts the
          reply to the practice's listing
```

- The console is an **internal operator tool**, not a client product.
  Single small web app. No DB needed for the Phase 1 harness —
  in-memory + CSV export; add storage with the Phase 2 Google
  integration (OAuth tokens per practice, posted-state tracking).
- Stack suggestion: Python (FastAPI) or Node — pick whatever ships
  fastest; Claude API SDK either way. Decide at build time.
- Secrets: `ANTHROPIC_API_KEY` via env only. No PHI written to disk; CSV
  export is user-initiated and local.

---

## 6. Data & privacy

- Review text *may* contain PHI written by the reviewer themselves.
  Treat all input as sensitive: no logging of review bodies, no
  third-party analytics, TLS only, no persistence beyond the session in
  v1.
- Document a data-flow one-pager for prospective practices (what's sent
  to Anthropic, retention, no training on their data per API terms).
- Before any paid launch: BAA question. Confirm what's contractually
  needed when processing text that may include PHI; line up Anthropic
  data-handling terms / BAA path. Flag as a launch-blocker item, not an
  MVP-demo blocker.

---

## 7. Cost estimate (rough)

- Per draft pair: input ≈ ruleset+voice+review (~2–4k tokens, mostly
  cached) + output ~400 tokens. With prompt caching the static block is
  ~90% cheaper after first call.
- ~20 reviews/week ≈ ~80 drafting calls/mo per practice → well under
  ~$1–3/mo API cost per practice at current pricing. Pricing power is
  100x the cost; this is a margin-rich service.

---

## 8. Roadmap

- **Phase 1 (built):** offline drafting + HIPAA gate + operator console,
  fed by manual paste/CSV. The engine + ops harness. Use it to validate
  draft quality with 1–2 real dental offices' past reviews. NOT the
  client-facing product.
- **Phase 2 (required for the promise — the real product):** Google
  Business Profile API: OAuth grant at onboarding, auto-pull new
  reviews, and **operator-gated post-back to Google**. Persist OAuth
  tokens + posted state per practice. This is what makes "the client
  does nothing" true. Start the Google API access application early
  (it has lead time).
- **Phase 3:** multi-practice scale, billing, analytics (response rate,
  rating trend), optional **per-practice fully-autonomous** posting once
  a practice has earned trust in the gate.
- **Phase 4:** adjacent niches reusing the compliance engine (medical,
  dermatology, vet, legal).

---

## 9. Open questions / risks

- Google API approval timeline (phase 2) — start that application early.
- BAA / PHI contractual path before paid launch (see §6).
- Do target practices *have* past replies to learn tone from, or is the
  brand-voice form the common path? (Affects onboarding UX.)
- Yelp is excluded from the promise (no reply API) — sell Google-only;
  never imply Yelp coverage.
- **Liability framing:** we post on the practice's behalf to *their*
  public listing — they are publicly liable for what lands there. The
  deterministic HIPAA gate + operator review are the safety net. Posting
  is operator-owned and operator-gated (never client, never autonomous
  in v1/v2). The practice's Google OAuth grant authorizes us to post;
  capture that authorization in writing at onboarding. Counsel sign-off
  on the gate + a data/PHI BAA path remain hard launch-blockers.
- Google API approval + per-practice OAuth onboarding friction is now on
  the critical path, not deferrable.

---

## 10. Next step

Phase 1 (engine + operator console + HIPAA gate + fixtures) is **built**
— it proves the drafting/compliance engine and is the operator's daily
tool. The promise ("client does nothing") is not real until **Phase 2**:
Google Business Profile API for auto-ingest + operator-gated post-back.
That work starts with the Google API access application (lead time) and
the per-practice OAuth onboarding flow. Everything client-facing is
replaced by that managed pipeline; there is intentionally no
client-facing app.
