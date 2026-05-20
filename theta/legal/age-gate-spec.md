# Theta — 18+ Age Gate Specification

**Status: implementation spec — 2026-05-20.** Closes
`COMPLIANCE.md RF-11`.

---

## Why 18+
Three converging reasons set the floor at 18:
1. **Options-account eligibility.** Schwab (and every major US
   broker) requires account holders to be 18+ to open an options-
   approved brokerage account. A user under 18 cannot use the
   downstream brokerage workflow.
2. **COPPA compliance.** A hard 18+ gate categorically avoids the
   Children's Online Privacy Protection Act (under-13) regime. The
   intermediate teen tier (13–17) is also avoided.
3. **Stoic discipline alignment.** Theta teaches discipline applied
   to substantial financial risk. The product is intentionally
   designed for adults making adult decisions about their own
   capital.

---

## Signup flow
1. **Date-of-birth field** is the first field on the account-
   creation screen, before email/password.
2. Field uses a native date picker (mobile) or three-dropdown
   (year / month / day) with reasonable bounds (year 1900 –
   current year).
3. On submit, Theta computes the user's age in whole years from
   DOB to today's date.

---

## Branching logic
- **Age ≥ 18:** continue to email/password collection.
- **Age 13–17:** show refusal screen **R-1**. No data is written
  to backend; the DOB itself is **not stored**, only used in-memory
  for the check.
- **Age < 13:** show refusal screen **R-2**. No data is written;
  the session ends.
- **DOB in the future, or > 130 years old:** show error **E-1**;
  allow retry. (Validation, not refusal.)
- **DOB missing on submit:** show inline validation error; cannot
  proceed.

---

## Refusal screen R-1 (13–17)
> **Theta is for adults.**
>
> Theta teaches options trading strategies, and options trading
> requires you to be at least 18 to open a brokerage account in
> the United States. We do not offer accounts to people under 18.
>
> When you turn 18, you're welcome back.
>
> [ Close ]

No data is collected. No email is captured. No retry path on the
same device for 24 hours (see Device fingerprinting below).

---

## Refusal screen R-2 (under 13)
> **Theta is for adults.**
>
> We do not collect any information from people under 13. Please
> close this app.
>
> [ Close ]

Same data-handling rules as R-1: nothing collected. Explicit
mention of "do not collect any information" satisfies the COPPA
notice requirement on the no-collection path.

---

## Error screen E-1 (invalid DOB)
> Please check the date of birth you entered.

Allow retry up to 3 attempts in 24 hours per device (see Device
fingerprinting below).

---

## Device fingerprinting / rate-limiting
To prevent trivial circumvention by re-entering a different DOB:
- Each refusal (R-1 or R-2) sets a device-level cool-down (24
  hours) before the signup flow can be retried.
- This is a soft control — VPN + device reset defeats it — but is
  sufficient to address the COPPA "we made reasonable efforts not
  to collect" standard.
- Implementation: client-side cool-down with a server-side backup
  keyed on device fingerprint + IP.

This is the balance: too aggressive a fingerprint hurts users with
legitimate retries; too loose a fingerprint invites re-entry. The
24-hour soft control is the standard pattern used by alcohol-vendor
age gates and similar regulated-product sites.

---

## Re-verification
- Once an account is created (18+ at the time), Theta does not ask
  the user's age again.
- If a user later claims to be under 18 (through customer service,
  social media, etc.), Theta's policy is to terminate the account
  and delete the user's data under the COPPA "actual knowledge"
  trigger.

---

## Settings / parental notice
The Privacy Policy (when drafted) includes a section confirming
Theta does not knowingly collect information from anyone under 18,
with contact instructions for parents to request deletion of any
data of a minor that may have been collected despite the gate.

---

## What Theta is NOT doing under bootstrap
- No knowledge-based age verification (KBV). Overkill; expensive;
  introduces PII risk we don't need.
- No government-ID upload. Strong friction; not justified by risk.
- No phone-number-based age check. Adds vendor complexity.

The DOB-field-with-cool-down approach is the standard for
regulated-product apps and is what's used by alcohol delivery,
firearms retail, cannabis (where legal), and most options-related
education products.

---

## Engineering acceptance criteria
- [ ] DOB field is the first input on signup, before any PII
      collection.
- [ ] DOB is NOT stored if age < 18.
- [ ] Refusal screens contain no opportunity for retry on the same
      device for 24 hours.
- [ ] Refusal screens collect no email and no PII.
- [ ] Server-side check confirms client-computed age (do not trust
      client alone).
- [ ] Privacy Policy section drafted with COPPA / under-18
      language.
- [ ] Customer-service playbook for "I'm under 18 / my child used
      this" → terminate + delete data.

---

## Future considerations (parked)
- If Theta ever expands beyond the US, jurisdiction-specific
  appropriateness assessments apply (UK FCA PS22/10 requires more
  than just age — see `COMPLIANCE.md §5.1`). N/A under US-only.

---

## Versioning
Current version: **0.1 — 2026-05-20.**
