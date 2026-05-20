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

**Value prop:** *"We write and post every Google review reply for your
dental practice — HIPAA-safe, in your voice. You just give a quick
thumbs-up."*

This is a **fully managed service**, not self-serve software. We do
100% of the labor — ingest reviews, draft replies, run the HIPAA gate,
and post to the practice's Google listing. The practice's only touch is
a fast **approve before posting** (a few seconds per review, on the
channel they pick). That approval is deliberate: it is the practice
consenting to what appears in their name, which is what makes the
HIPAA/liability posture clean — while their workload still goes from
4–5 hrs/week to seconds.

Compliance is the product, not a feature. It is also the moat: it lets us
charge more than a $20 generic SaaS and sell to compliance-nervous office
managers.

Target buyer: dental office manager / practice owner. Pain: 4–5 hrs/week,
plus fear of replying wrong. Volume: a busy practice gets 5–30
reviews/week. **Scope: Google reviews only** (see §2 — Yelp has no
reply API and is not part of the promise).

---

## 2. Scope (decided)

Fully managed, **client-approves-then-we-post**, **Google-only**:

- **We do all the work; the client only approves.** We ingest, draft,
  HIPAA-gate, send for approval, and post. The client never logs into
  an app, never writes, never posts. Their effort = a quick yes/no.
- **Approval before posting (the liability anchor):** nothing reaches
  the live listing without the practice's approval. Channel is
  **per-practice configurable — all three supported**: (a) email
  digest with one-click Approve/Edit/Reject, (b) a magic-link approval
  page, (c) SMS reply-to-approve. The practice picks at onboarding.
- **Approval granularity:** positive replies (4–5★) are bulk-approvable
  (one-click "approve all", or auto-approve after a quiet window if the
  practice opts in). Negative (1–2★) and mixed (3★) **always require
  explicit per-reply approval** — eyes on the risky ones.
- **Internal operator console** (built, Phase 1) is where we QA/gate
  and trigger posting after client approval. Not client-facing.
- **Posting to Google requires the Google Business Profile API + the
  practice's OAuth grant.** No compliant shortcut (scripting Google's UI
  violates ToS and flags the listing — fatal for a reputation product).
  This makes the Google API integration **core, not optional**.
- **Yelp is out.** Yelp has no public API to post review replies, by any
  compliant means. The promise is Google-only; do not imply Yelp.
- **Phase 1 (built):** drafting + HIPAA gate + operator console, fed by
  manual paste/CSV. Testing/ops harness; proves the engine. NOT the
  client product.
- **Phase 2 (required for the promise):** Google Business Profile API
  (auto-ingest + post-back) + the client approval delivery in the three
  channels. This is what makes the managed promise real.
- **Drafting: Claude API.** Tone learned from 5–10 of the practice's own
  past replies (or a short brand-voice questionnaire if none exist).

Out of scope: client-facing authoring app, fully autonomous posting
(no approval at all; revisit per-practice once trust is earned), Yelp,
multi-tenant billing UI, analytics dashboard.

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

Also captured at onboarding (one-time): the **approval channel**
(email / magic-link / SMS), the **approver contact** (email or mobile),
the optional **auto-approve-positives** preference, and the **Google
OAuth grant + written authorization** to post on their behalf.

Stored as a per-practice config (JSON) reused on every draft.

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
 OPERATOR CONSOLE (internal QA — never client-facing)
      │
      ▼
 ROUTE BY RATING
   4–5★ → bulk-approvable (or auto-approve if practice opted in)
   1–3★ → always explicit per-reply approval
      │
      ▼
 CLIENT APPROVAL  (per-practice channel: email | magic-link | SMS)
   approve / edit / reject
      │ approved
      ▼
 Phase 1: operator marks posted (manual paste/CSV harness)
 Phase 2: on approval → Google Business Profile API posts the reply
          to the practice's listing
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

- **Phase 0 (built; the pre-API revenue engine):** lead qualifier +
  free-sample generator (`/prospect`, `app/leads.py`) and the
  **concierge trial** — we draft + HIPAA-gate, the practice approves,
  and *they paste* the approved replies into their own Google dashboard
  (or delegate access to it). Not automation, no ToS issue, no API
  dependency. This earns money and proves retention while the Google
  API access application is in flight; those practices upgrade silently
  to the Phase 2 pipeline when access lands.
- **Phase 1 (built):** offline drafting + HIPAA gate + operator console,
  fed by manual paste/CSV. The engine + ops harness. Use it to validate
  draft quality with 1–2 real dental offices' past reviews.
- **Phase 2 (built offline; live pending credentials):** the full
  approval state machine is implemented and persisted per practice
  (pending → approved → posted / rejected), with: client approval
  delivery rendered for all three channels (email digest, magic-link
  page, SMS) + the working **magic-link approval page**; the
  bulk-positives / explicit-negatives routing; client edits re-run
  through the HIPAA gate before they can post; a final pre-post HIPAA
  backstop; and a **Google post-back seam** (`SimulatedGoogleClient`
  proves the pipeline end-to-end; `LiveGoogleClient` refuses rather
  than fake a post). What remains is purely credential-gated and is a
  known, small swap: (a) Google Business Profile API access + the
  per-practice OAuth grant (start the access application early — lead
  time); (b) real SMTP / Twilio Senders behind the existing one-method
  `Sender` protocol. No further architecture needed.
- **Phase 3:** multi-practice scale, billing, analytics (response rate,
  rating trend), optional **per-practice auto-approve** (skip the
  approval step entirely) once a practice has earned trust in the gate.
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
- **Liability framing:** the practice **approves every reply before it
  is posted** (explicitly for 1–3★; bulk/opt-in-auto for 4–5★), so what
  lands on their public listing is content they consented to — this is
  the core liability anchor. Layered safety: deterministic HIPAA gate
  (nothing non-compliant is ever shown) → operator QA → client approval
  → we post. The Google OAuth grant + written authorization at
  onboarding cover us posting on their behalf. Counsel sign-off on the
  gate + a data/PHI BAA path remain hard launch-blockers. Note: opting
  a practice into auto-approve-positives (Phase 3) trades a sliver of
  that consent anchor for convenience — make it explicit and opt-in.
- Google API approval + per-practice OAuth onboarding friction is now on
  the critical path, not deferrable.

---

## 10. Next step

Phase 1 (engine + operator console + HIPAA gate + per-practice config)
and Phase 2 (approval state machine + persistence + 3-channel rendering
+ working magic-link approval page + simulated Google post-back, all
tested end-to-end offline) are **built**. The managed promise ("we
write & post, you just approve") is now real except for two purely
credential-gated swaps with no remaining design work: the Google
Business Profile API access + per-practice OAuth grant (start that
access application now — it has lead time), and real SMTP/Twilio
Senders behind the existing protocol. Next step is operational, not
architectural: file the Google access application and validate draft
quality on a real practice's history. The only client-facing surfaces
are the lightweight approval channels and a weekly recap — no
authoring app. Counsel sign-off on the HIPAA gate + a PHI/BAA path
remain the hard launch-blockers before any live post.
