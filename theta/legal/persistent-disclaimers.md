# Theta — Persistent Disclaimer Strings

**Status: DRAFT 0.1 — 2026-05-20, pending counsel review.** Catalog
of the standard disclaimer strings shown across Theta. Closes the
persistent-disclaimer portion of `COMPLIANCE.md RF-08`.

These strings are designed to be:
- Short enough to fit a single footer line on mobile.
- Strong enough to satisfy §206(4) anti-fraud framing.
- Re-used verbatim so the wording stays consistent.

Display rule: a disclaimer is shown **wherever** the relevant
content appears. Buried-in-Settings disclaimers are not sufficient;
the disclaimer must accompany the content.

---

## D-1. Persistent footer — any screen showing a specific ticker
**Where:** any screen displaying a specific security, options
contract, scanner result, paper-trade ticket, or chart.
**Text (one line):**
> Educational. Not investment advice. Options involve substantial
> risk of loss.

## D-2. Persistent footer — paper-trade screen
**Where:** any paper-trade portfolio, P&L view, or simulator screen.
**Text:**
> Simulated trading. Results do not reflect real-money execution,
> slippage, or your behavioral response to live capital.

## D-3. Persistent footer — scanner screen
**Where:** any screen showing scanner output.
**Text:**
> Results match the filter YOU defined, as of [delayed timestamp].
> Educational; not a recommendation.

## D-4. Persistent footer — coach chat screen
**Where:** any LLM coach conversation interface.
**Text:**
> Educational chat with a language-model coach. May contain errors.
> The coach does not recommend specific trades.

## D-5. First-time options-lesson disclaimer (ODD link)
**Where:** opening of every options lesson (L2 onward) and any
options-strategy content in the SaaS tier.
**Text (modal, dismissable per session):**
> Options trading involves substantial risk. Before trading options
> for real, read the OCC Options Disclosure Document:
> https://www.theocc.com/about/publications/character-risks.jsp
> Your broker will require you to be approved for options trading.

## D-6. Backtest result disclaimer
**Where:** every backtest output view, every shared/exported
backtest summary.
**Text (full):**
> Hypothetical performance. Backtested results are calculated with
> the benefit of hindsight, do not involve financial risk, and
> cannot account for many factors that affect actual trading. No
> representation is made that any account will achieve similar
> results.

## D-7. Strategy builder — undefined-risk warning
**Where:** when the user configures a strategy with theoretically
unlimited loss (e.g., naked short call) above the safety threshold.
**Text (interrupting modal):**
> This configuration has theoretically unlimited risk of loss. Many
> traders never use undefined-risk strategies; Theta's curriculum
> favors defined-risk structures. If you understand the risk and
> want to proceed, confirm below.

## D-8. Exported / shared P&L disclaimer
**Where:** any export of paper-trade or backtest P&L (PDF, image,
CSV header).
**Text (header + footer of export):**
> Theta — Educational paper-trade results. Simulated; not
> real-money execution. Past simulated results do not predict
> future results.

## D-9. Coach output — every response
**Where:** appended (subtly) to every LLM coach response, or shown
permanently in the chat-interface footer.
**Text:**
> Educational. Not investment advice.

## D-10. Marketing / public-facing content
**Where:** any marketing surface where Theta references trading,
strategies, options, or the scanner.
**Text:**
> Theta is an educational SaaS tool, not a broker-dealer or
> investment adviser. Options trading involves substantial risk of
> loss.

## D-11. Journal / adherence view (after Schwab OAuth aggregation)
**Where:** any view that shows trades pulled from a connected
brokerage.
**Text:**
> Imported from your broker for journaling purposes only. Theta
> does not place orders, hold funds, or trade on your behalf.

## D-12. Voice-output coach
**Where:** any audio interface where the coach speaks responses.
**Text (spoken at session start; brief, not legalese):**
> A quick reminder — I teach strategy. I don't tell you what to
> trade. Let's get into it.

---

## Production / accessibility requirements
- Footer text must meet WCAG 2.1 AA contrast (≥4.5:1) at the
  selected font size.
- Footer must persist on screen (not auto-hide on scroll) where the
  disclaimed content is visible.
- Modal disclaimers must be dismissable by explicit user action,
  not by tapping outside.
- Disclaimer text is treated as content (not a "loading state") —
  must be present even when the underlying data feed errors.

## Versioning
Current version: **DRAFT 0.1 — 2026-05-20.** Bump on any material
change. Sync version with `risk-disclosure.md`.
