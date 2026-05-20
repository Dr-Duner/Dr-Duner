# Theta — Risk Disclosure

**Status: DRAFT 0.1 — 2026-05-20, pending counsel review.** The
working draft of the Risk Disclosure shown to every user before
they create an account. Final production copy requires US securities
counsel sign-off. Closes the modal portion of `COMPLIANCE.md RF-08`.

---

## The plain-English version (the part users read first)

Before you use Theta, understand four things:

1. **Theta is education, not investment advice.** We teach options
   strategies — how they work, when they win, when they fail. We do
   not tell you which trades to make. The decisions are yours.

2. **Options trading involves substantial risk of loss.** You can
   lose the entire amount you put in, and in some strategies more
   than that. Options are not suitable for everyone, and you should
   not trade options with money you cannot afford to lose.

3. **Theta is not your broker or your investment adviser.** We are
   not registered as a broker-dealer or as an investment adviser.
   We are a SaaS tool for traders. When you are ready to trade for
   real, you do that through your own broker (e.g., Schwab), not
   through Theta.

4. **Past results — yours, ours, or anyone else's — do not predict
   future results.** Paper-trade outcomes inside Theta are simulated
   and do not reflect the slippage, commissions, assignment, or
   timing of real-money trading. Backtested results are
   hypothetical.

If you understand all four points, tap **I understand** to continue.
If you don't, please read the longer disclosure below.

---

## The longer disclosure

### 1. Education, not advice
Theta provides educational content, strategy-building tools, a
scanner that runs the strategy *you* define, a paper-trade
simulator, and a journal/analytics layer. The on-screen coach
("Lyra," "Nestor," "Chiron," or "Atlas") is an educational chat
interface — it explains strategies, mechanics, and the math behind
them, and reflects your stated strategy rules back to you. It does
not recommend specific trades, does not give buy/sell advice on
specific securities, and does not predict price direction.

Information shown in Theta — including data on specific securities,
strategy mechanics, examples, and the output of the scanner — is
for educational purposes and is **not** a recommendation to buy,
sell, or hold any security, or to enter any specific transaction.

### 2. Options-trading risk
Options trading involves substantial risk and is not appropriate
for all investors. The risks include, without limitation:
- Loss of the entire premium paid (for option buyers).
- Loss of substantially more than the premium received, up to
  theoretically unlimited loss in some strategies (for sellers of
  uncovered positions).
- Adverse changes in implied volatility affecting position value
  regardless of underlying price movement.
- Time decay (theta) eroding the value of long option positions.
- Assignment risk on short options, including early assignment.
- Pin risk and gamma risk near expiration.
- Liquidity risk in thinly traded options.
- Gap risk over earnings, news, and overnight sessions.

Before you trade options for real, you must read the Options
Clearing Corporation's disclosure document, **"Characteristics and
Risks of Standardized Options"** (the **ODD**), at:
https://www.theocc.com/about/publications/character-risks.jsp

Your broker will also require you to be approved for options
trading at an appropriate level before you can place options
trades.

### 3. Theta is not a broker-dealer
Theta is not registered as a broker-dealer with the U.S. Securities
and Exchange Commission, FINRA, or any state securities regulator.
Theta does not:
- Effect securities transactions;
- Place, route, or hold orders;
- Hold customer funds or securities;
- Receive transaction-based compensation tied to specific trades.

When you are ready to execute trades for real money, you do so
through your own brokerage account (e.g., Schwab). Theta may
provide a hyperlink to your broker for your convenience; that link
opens your broker's own application — Theta never touches the
order.

### 4. Theta is not an investment adviser
Theta is not registered as an investment adviser with the SEC or
any state securities regulator. Theta does not provide personalized
investment advice. The strategy you build in Theta is yours — you
define every parameter, and the scanner mechanically executes the
filter you wrote. The coach educates you on options strategies and
reflects your own rules back to you; the coach does not recommend
specific trades.

### 5. Paper trading is a simulation
Theta's paper-trade simulator uses 15-minute-delayed market data
and approximates real-world execution (realistic fill prices,
commissions, fees, assignment, slippage). Paper trading is a
simulation and does not represent actual trading. Real-money
execution may differ materially due to: actual market liquidity,
slippage, partial fills, broker-specific execution quality, your
account-level fees and commissions, tax consequences, and your own
emotional and behavioral responses to live capital at risk.

**No representation is made that any account will or is likely to
achieve results similar to those shown in the paper-trade
simulator.**

### 6. Past and hypothetical performance
Past performance — whether your own, another user's, the result of
a strategy you defined, or any strategy referenced in Theta — does
not guarantee or predict future results.

Backtested ("hypothetical") performance results have inherent
limitations. They are calculated with the benefit of hindsight, do
not involve financial risk, and cannot completely account for the
impact of financial risk in actual trading. For example, the
ability to withstand losses or to adhere to a particular trading
program in spite of losses are material points that can adversely
affect actual trading results. Numerous other factors related to
the markets or to the implementation of any specific program
cannot be fully accounted for in the preparation of hypothetical
results, and all of which can adversely affect actual trading.

### 7. Coach output limitations
The on-screen coach generates responses using large language model
technology. These responses are produced statistically and may
contain errors, omissions, or inaccuracies, even where presented
confidently. You should not rely on any coach response as a
substitute for independent verification of facts, mathematics, or
strategy mechanics. Where a number is shown, it was computed by a
deterministic tool. Where an opinion appears to be given on a
specific trade, treat it as an educational illustration, not as a
recommendation.

### 8. US availability only
Theta is currently offered only to users in the United States. By
using Theta, you represent that you are accessing the service from
within the United States. Accessing Theta via a virtual private
network or other means of obscuring your location for the purpose
of using the service from outside the United States is a violation
of these terms and may result in account termination.

### 9. Suitability
Options are not suitable for all investors. Before opening an
options account at your broker, your broker will assess your
financial situation, investment experience, and risk tolerance to
determine the appropriate options-trading level for you. Theta's
educational content is not a substitute for that suitability
assessment, and Theta makes no determination of suitability for
any specific user.

### 10. No fiduciary relationship
Use of Theta does not create a fiduciary, advisory, agency, or
similar relationship between you and Theta. Theta does not owe you
a duty to act in your best interests with respect to any specific
investment decision.

### 11. Limitation of liability
To the maximum extent permitted by applicable law, Theta is not
liable for any losses you incur in connection with trading
decisions you make based on information, tools, simulations, or
coach output provided by Theta, whether such losses arise from
real-money trading, paper trading, errors or inaccuracies in
content, or otherwise. Some jurisdictions do not allow the
exclusion of certain warranties or limitation of liability for
certain damages; in those jurisdictions, this section applies to
the maximum extent permitted.

### 12. Acknowledgment
By tapping **I understand and accept**, you confirm that you:
- Are at least 18 years of age and a U.S. resident.
- Have read this Risk Disclosure in full.
- Understand that Theta is an educational and analytical tool, not
  a broker-dealer or investment adviser.
- Understand that options trading involves substantial risk of
  loss.
- Understand that past performance and paper-trade results do not
  predict future results.

---

## Display + UX requirements
- Shown on first launch after install, before any other screen.
- Shown again on any user account that has not seen the current
  version (version-stamped).
- Must be scrolled to the end before the **I understand and
  accept** button activates.
- Accept action is logged with timestamp + disclosure version.
- A persistent link to this document is available in Settings.

## Versioning
Current version: **DRAFT 0.1 — 2026-05-20.** Bump version on every
material change. Existing users must re-accept on material change.
