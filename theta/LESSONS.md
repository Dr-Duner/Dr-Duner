# Theta — Lesson Bible (2–19)

Every lesson is the **locked production template** (see
`storyboard-production-template.png` + `storyboard-frame-layout.png`).
Font = IBM Plex Mono; palette black/green; ~40s, 9:16, chibi, App-Store
quality. The wrapper is FIXED for all 19; only the teaching middle and
the scanner card change per lesson.

FIXED WRAPPER — **REWRITTEN 2026-05-20 (Gee)** — supersedes the earlier
S4/S5 reframes. Every lesson is now an **app-execution demo wrapped
by the coach**: maximum UI, two initial sell points (scanner; ease of
execution), paper-trade-only at launch. The lessons that *generate*
the strategy parameters the scanner uses live elsewhere in the arc
and are OUT OF SCOPE for this wrapper — the wrapper shows the trade
flow, not the strategy derivation. (See DESIGN.md "Lesson = app demo
= promo" lock 2026-05-20.)

1. **COLD OPEN — coach in ancient life** (per coach; ~0–4s). Full-
   color Aegean; coach unaware. Establishes the human you're about
   to bond with.
2. **THE NOTIFICATION** (~4–7s). Cut tighter — the modern phone on
   the marble ledge. Lock-screen Θ push notification arrives.
   On-screen: the lesson's Stoic line + a "matches your strategy"
   tag. *This is how users get notified.*
3. **THE SCANNER — terminal home screen** (~7–13s). Coach picks up
   the phone, unlocks → the real app terminal home (DESIGN §3b-1).
   The `[COACH] scan — DD Mon` block surfaces trades that match the
   user's strategy. **SELL POINT #1.** (Per-lesson `SCAN:` line below
   defines which trades surface for that lesson.)
4. **THE ENTRY — paper-trade entry screen** (~13–22s). Coach taps a
   pipeline row / `[ PAPER TRADE ]` → paper-trade entry screen.
   Coach picks underlying, sets stop, sets take-profit. Taps only.
   No math, no chain, no greeks. Dichotomy is BAKED INTO the screen:
   editable fields = signal-green = what you control; read-only/
   greyed = what you don't. **SELL POINT #2 begins.**
5. **THE REVIEW — paper-trade review screen** (~22–28s). All entered
   numbers shown back — underlying, entry, exit, size — with a
   non-removable `PAPER TRADE` badge. Honest framing on-screen.
6. **THE SEND + Θ LOGO** (~28–34s). Coach taps send → `PAPER TRADE
   SENT` animation; Θ logo lands in green candlesticks. **SELL
   POINT #2 paid off — that easy.**
7. **COACH LAND + Θ CTA** (~34–40s). Coach back in ancient frame
   (telescope/drill/etc.); one line that names the lesson's truth;
   Θ end card — "Θ / don't predict it. trade it. now."
   (locked 2026-05-18).

DEPENDENCY: S3 / S4 / S5 / S6 all == real shipping app UI (DESIGN
§3b-1 terminal home + paper-trade entry/review/sent screens). The
in-video screen and the real app must be the same screen, or the
demo lies. Paper-trade screens must be designed in lockstep with the
videos.

Per-lesson swap surface:
- **S1 cold open** — coach-specific scene (Lyra telescope / Nestor
  drill / Chiron TBD / Atlas TBD).
- **S2 notification** — the lesson's Stoic line in the push body.
- **S3 SCAN line** — which trades surface for this lesson's strategy
  (defined per-lesson below in `SCAN:`).
- **S4 entry parameters** — which fields the coach fills (the
  lesson's strategy expressed as a concrete trade).
- **S7 coach line** — the per-lesson one line + the coach in their
  closing ancient frame.
S2 notification UI, S5 review screen, S6 send + Θ logo are **constant
across all 20 lessons × 4 coaches** — generate once, reuse.

## Coach model
Lessons are coach-agnostic templates. `[COACH]` = the partner Gee's
user chose; voice adapts:
- Lyra: precise non-round numbers, calm, asks more than tells.
- Nestor: short sentences, like punches.
- Chiron: warm, teaches by question, never rushed.
- Atlas: downside first, names the exit before the entry.
Supersedes the old "coach silent 2–19" line — the coach is PRESENT and
interactive throughout (builds trust, ties user to the coach).

## Arc
L1 Dichotomy of Control (done) → 2–19 below → first paper trade closes
→ coach's ONE line (the handshake) → L20 scanner unlock → coach live.

---

### L2 — Premeditatio Malorum · Define the loss first
- HOOK: a trade ticket with the loss field blank, blinking.
- STOIC: Seneca — rehearse the worst before it happens.
- CRAFT: defined-risk basics; max loss = premium paid (long option).
- INTERACTIVE: user must type their max-loss number to arm the ticket.
- SCAN: a long-option idea card with the max-loss field auto-filled (= premium).
- COACH LAND: [COACH] — "You don't fear what you've already priced."

### L3 — The View From Above · Thesis vs noise
- HOOK: a 1-minute chart thrashing; zoom out to 1-year calm.
- STOIC: Marcus — the view from above shrinks the panic.
- CRAFT: timeframes; signal vs noise; why intraday lies.
- INTERACTIVE: user toggles 1D ↔ 1Y and feels the difference.
- SCAN: an idea card framed on 1Y context; intraday noise greyed out.
- COACH LAND: [COACH] — "The noise was never the trade."

### L4 — The Chosen Response · What an option is
- HOOK: two doors — CALL, PUT.
- STOIC: Epictetus — not events, but our response to them.
- CRAFT: call vs put as a chosen, bounded response (not a hope).
- INTERACTIVE: a scenario; user picks call or put, sees the payoff.
- SCAN: one directional idea; the chosen contract highlighted with its payoff.
- COACH LAND: [COACH] — "A contract is a decision, not a wish."

### L5 — Theta · Time Is the Tax  ⟵ brand lesson
- HOOK: the symbol Θ forms; a clock ticking inside it.
- STOIC: Memento mori — time spends whether you act or not.
- CRAFT: extrinsic value decays; theta is the daily tax/ally.
- INTERACTIVE: drag a slider across days, watch the decay curve bend.
- SCAN: a theta-positive idea; days-to-expiry + daily decay flagged.
- COACH LAND: [COACH] names the symbol — "This is why we're called Theta."

### L6 — Amor Fati · No revenge trades
- HOOK: a red loss; a glowing "GET IT BACK" button.
- STOIC: Nietzsche-via-Stoic — love what happened; don't fight it.
- CRAFT: tilt and revenge trades destroy edge.
- INTERACTIVE: user reaches for the button; [COACH] intercepts it.
- SCAN: next idea unlocks only after a cool-down; no "get it back" path.
- COACH LAND: [COACH] — "The next trade doesn't owe you the last one."

### L7 — The Discipline of Assent · IV is priced fear
- HOOK: a calm chart vs a screaming one, same price.
- STOIC: don't assent to every impression.
- CRAFT: implied volatility = the crowd's panic, priced.
- INTERACTIVE: compare high-IV vs low-IV option cost, same strike.
- SCAN: idea card leads with IV rank/percentile as a priced-fear gauge.
- COACH LAND: [COACH] — "You're buying their fear. Know the price."

### L8 — Memento Mori for Positions · Exit at entry
- HOOK: a position with a tombstone date (expiry).
- STOIC: everything has an end; plan for it now.
- CRAFT: every option dies; define the exit before the entry.
- INTERACTIVE: user sets a take-profit AND stop before arming.
- SCAN: idea card with take-profit + stop pre-filled; expiry as a tombstone.
- COACH LAND: [COACH] — "Name the exit and the trade gets quiet."

### L9 — [PROVISIONAL] The Dichotomy in Size · Sizing is control
> Placeholder. The real Lesson 9 was built in Cowork and is the bar;
> replace this when Gee surfaces it. Provisional below so the arc holds.
- HOOK: two identical theses, one 50% bet, one 2%.
- STOIC: control the controllable — size is fully yours.
- CRAFT: 1–2% risk per trade; ruin math.
- INTERACTIVE: user sets risk %, sees the survival curve.
- SCAN: idea card with position size auto-set to 1–2% account risk.
- COACH LAND: [COACH] — "Size is the only thing the market can't take."

### L10 — The Inner Citadel · The trade journal
- HOOK: a leather journal that is also a trade log.
- STOIC: Marcus wrote to himself, for himself.
- CRAFT: logging thesis/size/exit/feeling = the edge compounding.
- INTERACTIVE: user writes their first one-line journal entry.
- SCAN: arming the idea requires a one-line thesis/feeling log entry.
- COACH LAND: [COACH] — "The log is where you meet yourself."

### L11 — Probability, Not Prophecy · Delta as odds
- HOOK: a fortune teller crossed out; a probability dial.
- STOIC: act on reasoned likelihood, not certainty.
- CRAFT: delta ≈ probability; thinking in bets.
- INTERACTIVE: user guesses the odds, then delta is revealed.
- SCAN: idea card leads with delta read as probability-of-profit.
- COACH LAND: [COACH] — "You don't predict. You weigh."

### L12 — The Obstacle Is the Way · Defend a losing trade
- HOOK: a trade underwater; three doors: ROLL / CLOSE / ADD.
- STOIC: the impediment to action advances action.
- CRAFT: rolling mechanics; defined defense vs hope.
- INTERACTIVE: user chooses; sees the new risk picture.
- SCAN: an underwater position card offering ROLL / CLOSE / ADD + new risk.
- COACH LAND: [COACH] — "A good defense is still a decision."

### L13 — Sympatheia · You are part of the market
- HOOK: one stock pulses; the whole sector pulses with it.
- STOIC: all things are interwoven.
- CRAFT: correlation, beta, why "diversified" can be one bet.
- INTERACTIVE: pick a hedge; see correlation collapse the risk.
- SCAN: idea flags correlated holdings; suggests a decorrelating hedge.
- COACH LAND: [COACH] — "Nothing you hold is alone."

### L14 — Temperance · Defined risk over naked risk
- HOOK: a tightrope with a net vs without.
- STOIC: temperance — bounded appetite.
- CRAFT: the vertical spread; cap the loss, fund it.
- INTERACTIVE: user builds a spread from a naked option.
- SCAN: idea offered as a defined-risk vertical, never naked.
- COACH LAND: [COACH] — "The net doesn't slow you. It frees you."

### L15 — The Last Hour · Expiration & gamma
- HOOK: a countdown; the P/L line whipping violently.
- STOIC: the final hour magnifies everything — act early.
- CRAFT: gamma risk, pin risk, why you exit before the bell.
- INTERACTIVE: slide toward 0DTE, feel the P/L go unstable.
- SCAN: idea blocks 0DTE; flags gamma/pin risk, forces a later expiry.
- COACH LAND: [COACH] — "Heroes die in the last hour. Leave early."

### L16 — Premium as Patience · Be the house
- HOOK: flip the desk — user moves from buyer to seller seat.
- STOIC: patience as a position; collect, don't chase.
- CRAFT: selling premium; theta now works FOR you (the Θ payoff).
- INTERACTIVE: buyer P/L vs seller P/L, same contract.
- SCAN: a premium-selling card; theta now shown working FOR the user.
- COACH LAND: [COACH] — "Now time pays you. That's the whole game."

### L17 — Ataraxia · Equanimity in a drawdown
- HOOK: a losing streak; the equity curve bleeding.
- STOIC: tranquility independent of outcome.
- CRAFT: variance vs skill; why process holds when results don't.
- INTERACTIVE: simulate 5 losers with a sound process; hold or fold.
- SCAN: idea card foregrounds the process checklist, not the P/L.
- COACH LAND: [COACH] — "The process didn't break. You didn't either."

### L18 — The Reserve · Cash is a position
- HOOK: a vault with the door open — empty looks scary, is power.
- STOIC: Seneca — wealth is having enough, and dry powder.
- CRAFT: cash as optionality; not always being in a trade.
- INTERACTIVE: user allocates % to cash vs deploy; see opportunity.
- SCAN: card includes a deploy-vs-hold-dry-powder allocation choice.
- COACH LAND: [COACH] — "An empty hand can still catch."

### L19 — The Handshake Approaches · The pre-trade checklist
- HOOK: every prior icon assembles into one checklist.
- STOIC: synthesis — discipline is a system, not a feeling.
- CRAFT: the full pre-trade check (thesis/size/risk/exit/IV/odds).
- INTERACTIVE: user runs the checklist on a real setup, end to end.
- SCAN: the full pre-trade checklist runs on a live setup — all green to arm.
- COACH LAND: [COACH] — "You're ready for a real one. I'll be watching."
  → leads into first paper trade → the ONE-line handshake → L20.

---

## Status
- All 19 re-cut onto the LOCKED production template (fixed wrapper +
  variable teaching middle + per-lesson SCAN card). L9 PROVISIONAL
  pending the Cowork reference.
- Vision rendered: `storyboard-production-template.png` (the video,
  shot-by-shot + quality bar), `storyboard-frame-layout.png` (9:16
  grid / coach-UI), `storyboard-L5-theta.png` (worked example).
- Next: render the remaining per-lesson middles L5-style on request,
  then train the 4 coaches as Soul characters and generate one hero
  lesson end-to-end as the quality bar.
