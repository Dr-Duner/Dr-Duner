# Theta — Subscription Terms

**Status: DRAFT 0.1 — 2026-05-20, pending counsel review.** Covers
ROSCA (15 USC §8403), California Auto-Renewal Law (Bus. & Prof.
Code §17602), and the FTC Click-to-Cancel Rule (16 CFR Part 425).
Closes `COMPLIANCE.md RF-09`.

This captures the language and UX requirements that Theta's
purchase, billing, renewal, and cancel flows must follow. Final
production copy will be reviewed by counsel before launch.

---

## Where subscriptions are billed
**Day one:** Apple App Store In-App Purchase + Google Play Billing.
Apple/Google handle most ROSCA + state-law compliance via their
billing flows; Theta inherits their compliant flow. However,
Theta-controlled surfaces (the in-app paywall, the post-purchase
confirmation screen, the cancel flow) must comply independently.

If/when we add web checkout: Stripe or similar with explicit
compliance review.

---

## Required disclosures at the point of purchase
Before the user confirms purchase, the following must be clearly
and conspicuously shown (CA ARL §17602(a)(1)–(2) + FTC negative-
option rules):

1. **Plan name** (e.g., "Theta SaaS — Monthly").
2. **Price per billing cycle** in USD, including any introductory
   pricing AND the standard price after the introductory period
   ends.
3. **Billing cycle** ("Billed every month / year").
4. **Auto-renewal clearly stated:**
   > Your subscription **automatically renews** at the standard
   > price each [cycle] until you cancel.
5. **How to cancel:** "Cancel anytime in Settings or in your
   App Store / Google Play account."
6. **Free-trial conversion (if any):** "After [N]-day free trial,
   you will be charged $X each [cycle] unless you cancel before
   the trial ends."

These six items must appear together on the same screen as the
"Subscribe" button, at a font size readable on mobile. No fine
print only.

---

## Affirmative consent
The user must take an affirmative action (tap "Subscribe" or
equivalent) AFTER the six items above are visible. Pre-checked
boxes do not count as affirmative consent. The button text must
make clear that the action is purchasing a subscription — not
"Continue" or "OK" alone.

---

## Post-purchase confirmation
Immediately after purchase:
1. In-app confirmation screen restating: plan, price, next billing
   date, how to cancel.
2. Confirmation email (Apple/Google receipt, plus Theta-side email
   if we have the address) restating the same.

---

## Cancel flow (FTC Click-to-Cancel + CA ARL)
The cancel mechanism must be **as easy** as the signup mechanism.

Requirements:
1. **In-app cancel link in Settings.** Tap to cancel, no friction.
2. **No "save offers" or retention obstacles** that interpose more
   than one screen between the cancel tap and the cancellation
   confirmation. A single optional pause/discount offer is
   permissible; chained retention screens are not.
3. **Cancellation effective at end of current billing cycle.** User
   retains access until the cycle ends.
4. **Confirmation of cancellation:** in-app screen + confirmation
   email.
5. **No re-engagement spam** after cancel — one "we're sorry to see
   you go" email is acceptable; ongoing re-engagement requires
   separate consent.

Apple / Google flows handle in-store cancellation directly. Theta's
in-app cancel link routes to the appropriate store's subscription
management when on iOS / Android.

---

## Renewal reminders (CA ARL 2024 amendment)
- For subscriptions of 6+ months billed annually: send a reminder
  email 15–45 days before each renewal restating the price, billing
  cycle, and cancel mechanism.
- For long-running subscriptions of 12+ months: send a reminder
  every year (CA ARL §17602(c)).

---

## Plan changes by Theta
- Material price increases require: 30-day advance notice + a clear
  opportunity to cancel before the increase takes effect.
- New material terms require: 30-day notice + opportunity to cancel.

---

## Refunds
Apple App Store and Google Play govern refunds for in-app
purchases. Theta will not represent refund availability beyond
what the store rules provide.

---

## Termination by Theta
Theta may terminate or suspend an account for: violations of these
Terms; violations of the Acceptable Use clause in the main ToS;
suspected VPN-based access from outside the US (see Risk Disclosure
§8); or as required by law. Material termination includes a
pro-rated refund of the unused portion of the billing cycle.

---

## Tax handling
US sales tax + VAT (where applicable) is handled by Apple App
Store / Google Play. If Theta ever adds direct web billing, a VAT /
sales-tax solution (e.g., Stripe Tax, Quaderno, Paddle) is required
before launch in any taxing jurisdiction.

---

## Governing law + dispute resolution
- Governing law: Delaware (assuming Delaware incorporation) or the
  state of Theta's principal place of business. Confirm with
  counsel before launch.
- Dispute resolution: arbitration on an individual basis (no class
  arbitration), AAA Consumer Rules, with a small-claims-court
  carve-out. Counsel must review the arbitration clause for
  enforceability under current case law (Discover Bank, Concepcion,
  Lamps Plus, etc.).

---

## In-app UX spec
- **Settings → Subscription** is one tap from the home screen.
- The Subscription page shows: current plan, price, next billing
  date, **Cancel subscription** button (large, contrasting,
  unambiguous label — not "Manage" alone).
- Tapping **Cancel subscription** routes to the App Store / Play
  Store subscription management for that platform (Apple and Google
  require this).
- After return from the store flow, Theta polls subscription status
  and updates the UI to reflect the cancellation.
- The same path is available on a web account-management page if
  any web checkout exists.

---

## Engineering acceptance criteria
- [ ] All six required disclosures present on the paywall screen.
- [ ] Subscribe button text explicitly says "Subscribe" (not
      "Continue").
- [ ] Post-purchase confirmation screen + email implemented.
- [ ] In-app cancel link in Settings, one tap from home.
- [ ] Annual reminder email (15–45d pre-renewal) for annual plans.
- [ ] Renewal reminder for 12+ month long subs (CA ARL).
- [ ] Material change notice flow (30-day advance) defined.
- [ ] No retention chain >1 screen between cancel tap and confirm.

---

## Versioning
Current version: **DRAFT 0.1 — 2026-05-20.** Bump on every material
change. Existing subscribers must be notified of material changes
per the rules above.
