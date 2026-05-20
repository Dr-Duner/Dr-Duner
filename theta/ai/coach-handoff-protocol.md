# Coach Handoff Protocol (DRAFT 0.1)

**Status: DRAFT 2026-05-20.** Specification for what happens when
a user switches between coaches (Lyra → Atlas, etc.) inside
[PRODUCT]. Lower priority than the system prompt + refusal taxonomy
+ tool surface, but needed before multi-coach UX ships.

The four coaches are LOCKED (`DESIGN.md §2 / lesson-flow.mmd`):
- **Lyra** — the Analyst. Precise non-round numbers, calm, asks
  more than tells.
- **Nestor** — the Veteran. Short sentences, like punches.
- **Chiron** — the Patient Teacher. Warm, teaches by question,
  never rushed.
- **Atlas** — the Risk Manager. Downside first, names the exit
  before the entry.

Users choose a primary coach during onboarding. The handoff
protocol governs how to bring a second coach into the user's flow
without losing state or breaking the contract.

---

## What persists across the handoff (state moves with the user)
- User's stated strategy rules.
- User's mastery state on each concept (PEDAGOGY.md §3.5).
- User's paper-trade and real-trade journal.
- User's adherence score history.
- User's lesson progress.
- User's stated risk tolerance and account profile (the parts
  the user wrote down themselves; not brokerage holdings).
- The Risk Disclosure acceptance + version.
- Subscription status.

## What does NOT persist (coach-local)
- **Conversation continuity is per coach.** Lyra remembers what
  Lyra has discussed with the user. Atlas does not see Lyra's
  conversation history by default. (Optionally, the user can
  forward a specific conversation to another coach — see
  "Explicit forward" below.)
- **Voice character.** Each coach speaks in their own voice; the
  new coach does not impersonate the previous one.
- **Stylistic emphasis.** Lyra leads with data; Atlas leads with
  downside; Chiron leads with a question. The same user state,
  framed differently.

---

## Trigger patterns

### T-1 — Explicit coach switch
User in Settings selects a different primary coach.
- **UX**: confirmation modal explaining what carries over.
- **Coach-side**: the new coach receives a brief state-load
  (strategy rules, mastery state, recent journal summary) at the
  start of their first session. The user does not see this load;
  it appears as the new coach naturally being grounded in the
  user's situation.

### T-2 — Ad-hoc second opinion
User mid-conversation asks "what would Atlas say?" or "I'd like
to hear Nestor on this."
- **UX**: a "Bring in Atlas" / "Bring in Nestor" CTA appears.
- **Coach-side**: the current coach acknowledges in character
  ("Atlas will see this differently. Let me hand it to him.")
  then the new coach takes over the thread.

### T-3 — Coach-initiated handoff (rare, gated)
The current coach flags that a different coach's specialty fits
the moment. Permitted only in three specific cases:
- User describes a risk-management blind spot → suggest Atlas.
- User struggles with a concept after multiple reformulations →
  suggest Chiron.
- User is in a behavioral spiral (revenge trading, urgency) →
  suggest the user's primary coach take a break and Chiron step
  in for grounding.

The suggestion is always a question, never imposed. The user
decides whether to switch.

### T-4 — User-asks-about-other-coach
User asks "what does Chiron think of this strategy?" without
wanting a handoff.
- **Coach-side**: the current coach answers in *their own voice*
  about *the concept*, not by impersonating Chiron. Optionally:
  "If you want Chiron's framing on it, I can bring him in."

---

## State-load message (silent, machine-readable)

When a coach takes over a user's session for the first time (T-1
or T-2), the LLM receives a state-load block at the top of its
context. The user does not see this block.

Schema:
```
<state-load>
  <user-id>opaque-id</user-id>
  <primary-coach>Atlas</primary-coach>
  <previous-coach>Lyra</previous-coach>
  <strategy-rules>
    iv_rank_min: 50
    delta_target: 30
    dte_window: 25-35
    defined_risk: true
    profit_target_pct: 50
    stop_loss_pct: 200
    universe: liquid_optionable, excluding earnings within 14d
  </strategy-rules>
  <mastery-state>
    L1 Dichotomy: applied-multiple
    L2 Premeditatio: applied-once
    L4 Calls/Puts: explained-back
    L7 IV: applied-once
    L8 Memento Mori: exposed
    L14 Vertical Spreads: applied-once
    ...
  </mastery-state>
  <recent-journal>
    last-7-days: 4 trades, 2 adherent, 2 non-adherent
    pattern-flags: ["exits losers earlier than rule"]
  </recent-journal>
  <handoff-note>
    Lyra flagged: user has been revisiting the IV rank threshold
    three sessions in a row; may benefit from Chiron walking the
    concept from a different angle.
  </handoff-note>
</state-load>
```

The new coach reads this and grounds the first response without
narrating the state-load itself.

## Handoff phrases (in character)

### Lyra → handoff to another coach
> "Atlas will see this differently than I do. He starts with
> what you can lose. Let me bring him in."

### Nestor → handoff
> "Chiron. He's better at this one. Hold."

### Chiron → handoff
> "Lyra reads numbers like she reads stars. Let her run them.
> I'll be here when you come back."

### Atlas → handoff
> "Not my fight. Lyra will work the math. I'm here when it's
> time to set the exit."

---

## First-message-from-new-coach pattern

The new coach's first message after handoff should:
1. Acknowledge the handoff in their own voice (one short line).
2. Reflect that they have the user's context (strategy rules,
   the question at hand).
3. Re-frame the question in their voice.
4. Ask the user where to start.

Example — Atlas taking over after Lyra:
> "Atlas. I read the trade Lyra showed you.
>
> The structure is fine. What I want to know is: where do you
> exit if it goes against you? Your strategy says you cut at
> 200 percent of the credit you took. That's a $640 loss on a
> $320 credit. Are you good with $640 going away on this trade,
> tomorrow, on a single overnight gap?
>
> Tell me the exit before we talk anything else."

Same trade, same user state — completely different framing. That's
the value of multi-coach handoff.

---

## What the new coach must NOT do
- Do not pretend to be the previous coach.
- Do not contradict the previous coach about the user's stated
  rules or journal facts. (Different *framing* is fine and
  expected; different *facts* breaks user trust.)
- Do not relitigate work the previous coach finished (mastery,
  acknowledged trades) unless the user asks.
- Do not narrate the state-load block.

---

## Edge cases

### Voice handoff mid-spoken-audio
If voice (TTS) is active and the user requests handoff mid-audio:
finish the current sentence in the current voice, then the new
voice picks up the next sentence. Don't truncate awkwardly.

### Conflicting coach recommendations on a behavioral question
If Lyra and Atlas would frame a risk question differently (Lyra:
"the math says…"; Atlas: "the worst case says…"), the *current*
coach gives their answer; the user can request the other coach's
framing as a separate turn. Don't try to merge the framings.

### User asks about a previous coach's earlier statement
If the user references something the previous coach said in a
prior session the current coach didn't see ("Lyra told me last
week to look at vertical spreads"), the current coach responds in
their own voice about the topic, optionally noting "if you want me
to pull the exact thread from Lyra, I can". Don't fabricate what
the previous coach said.

### User starts switching coaches frequently
Coach-shopping is a behavioral pattern worth surfacing (PEDAGOGY.md
§7 data flywheel). Flag in the user's mastery state; the next coach
to load can gently surface it without judgment: "you've been moving
between voices — what are you actually looking for that you're not
finding?"

---

## Engineering acceptance criteria
- [ ] State-load schema implemented; tested with all four coaches.
- [ ] Per-coach conversation history isolation verified (Lyra's
      chat does not leak into Atlas's first-load context except
      through the structured state-load).
- [ ] Handoff phrases (T-2 trigger) library implemented per coach.
- [ ] User can switch primary coach in Settings; data carries
      over; confirmation modal renders.
- [ ] No coach impersonates another coach (eval test).
- [ ] No coach contradicts the user's stated rules across coaches
      (eval test).

## Versioning
Current version: **DRAFT 0.1 — 2026-05-20.** Bump on any state-
schema change or handoff-pattern addition.
