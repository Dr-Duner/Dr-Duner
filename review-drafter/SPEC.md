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

**Value prop:** *"HIPAA-safe review responses for dental practices,
written in your voice, ready to approve in 30 seconds."*

Compliance is the product, not a feature. It is also the moat: it lets us
charge more than a $20 generic SaaS and sell to compliance-nervous office
managers.

Target buyer: dental office manager / practice owner. Pain: 4–5 hrs/week,
plus fear of replying wrong. Volume: a busy practice gets 5–30
reviews/week across Google + Yelp.

---

## 2. MVP scope (decided)

- **Ingestion: manual paste / CSV.** No API approvals, ships in days,
  proves value before we invest in Google integration. Owner pastes
  review text (or uploads a CSV export from Google/Yelp/their PMS).
- **Delivery: single-page review queue (recommended).** Rationale: with
  manual ingestion the staffer pasting reviews *is* the approver — a
  daily email digest only makes sense once ingestion is automated
  (phase 2). v1 flow on one screen:
  1. Paste reviews or upload CSV.
  2. Each review gets 2 draft replies (one warm/short, one fuller).
  3. Inline edit → **Copy** button → "Mark posted."
  4. Optional: export approved replies back to CSV.
- **Drafting: Claude API.** Tone learned from 5–10 of the practice's own
  past replies (or a short brand-voice questionnaire if none exist).

Out of scope for v1: auto-posting replies, Google/Yelp API, multi-user
accounts, billing, analytics dashboard.

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
 review queue UI  (paste box | edit | Copy | Mark posted | export CSV)
```

- Single small web app (server + one page). No DB needed for v1 —
  in-memory/session + CSV export is enough; add SQLite only when we add
  accounts.
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

- **Phase 1 (MVP, now):** manual paste/CSV → queue → copy. Validate with
  1–2 real dental offices. Goal: they say "I'd pay for this."
- **Phase 2:** Google Business Profile API (OAuth, auto-pull new
  reviews), daily email digest delivery, "posted" tracking. Yelp =
  best-effort/manual (Fusion API returns only 3 truncated reviews;
  scraping violates ToS — do not).
- **Phase 3:** multi-practice accounts, billing, analytics (response
  rate, rating trend), optional auto-post with approval.
- **Phase 4:** adjacent niches reusing the compliance engine (medical,
  dermatology, vet, legal).

---

## 9. Open questions / risks

- Google API approval timeline (phase 2) — start that application early.
- BAA / PHI contractual path before paid launch (see §6).
- Do target practices *have* past replies to learn tone from, or is the
  brand-voice form the common path? (Affects onboarding UX.)
- Yelp coverage gap — set expectation up front that v1 is Google-centric.
- Liability framing: we draft, human approves & posts. Keep the human in
  the loop; never auto-post in v1. Document this.

---

## 10. Next step

On approval of this spec, build Phase 1: parser + drafter (with HIPAA
system prompt, prompt caching, post-check) + single-page queue, plus a
small fixture set of realistic dental reviews (positive, negative,
PHI-laden) to test the guardrails.
