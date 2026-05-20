---
name: hipaa-review-compliance
description: Use whenever drafting, reviewing, or approving a public reply to a patient/customer review for a dental (or any healthcare) practice. Enforces HIPAA-safe language and rewrites non-compliant drafts. This is the product's compliance moat — invoke before any reply is shown or sent.
---

# HIPAA Review Compliance

The non-negotiable gate. Every reply passes this before a human sees it.
This is product compliance design, not legal advice — practices' own
counsel signs off before launch.

## Hard rules — a compliant reply MUST NOT
1. Confirm or imply the reviewer is/was a patient ("thanks for choosing
   us", "glad you came in", "your visit", "see you next time").
2. Name/confirm/describe any treatment, procedure, diagnosis,
   appointment, or visit — **even if the reviewer disclosed it first.**
   The practice cannot ratify PHI by repeating it.
3. Tie the reviewer's name to care received.
4. Dispute facts of a visit publicly, or reveal whether they were seen.
5. Add any non-public clinical/personal detail.

## Compliant pattern
- **Positive:** warm, general thanks for kind words; reinforce values
  (caring team, comfortable environment) WITHOUT echoing treatment;
  no "your [procedure]".
- **Negative:** empathize generally, do not confirm patient status, do
  not argue facts, move offline: invite to call the office at
  {office_phone} so the team "can help" / "make things right." Never
  state whether they were a patient.
- **Neutral/mixed:** thank, acknowledge the experience generally,
  invite private contact for specifics.

## Deterministic post-check (run on every draft)
Scan the draft text. FAIL if it contains, in a patient-confirming
sense, any of:
- visit/appointment words: "your appointment", "your visit", "when you
  came in", "see you", "next visit", "your last", "schedule"
- treatment words: cleaning, filling, crown, root canal, extraction,
  implant, whitening, braces, Invisalign, denture, X-ray, exam,
  surgery, anesthesia, sedation, hygienist (as care received), "your
  treatment", "your procedure", "we treated/fixed/extracted/placed"
- patient-confirming phrasing: "thank you for choosing/trusting us
  with", "glad we could [verb] you", "as our patient", "your dentist"
On FAIL: do NOT show the draft. Regenerate with the violating phrase
fed back as a constraint. Max 2 retries, then fall back to the safe
template below.

## Safe fallback templates
- Positive: "Thank you so much for the kind words — it means a lot to
  our whole team. We're always here if you need anything. — {sign_off}"
- Negative: "We're sorry to hear this and we take feedback seriously.
  Please reach out to us directly at {office_phone} so we can help.
  — {sign_off}"

## Output contract
Return: the reply text + a one-line "Why this is safe" note for the
approver (e.g. "Generic thanks; no patient status or treatment
referenced"). Expand the term lists above as new edge cases appear —
this file is the source of truth.
