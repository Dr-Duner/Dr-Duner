# Lesson 1 — The Dichotomy of Control · FINAL SHOOTING SCRIPT

Status: **REWRITTEN 2026-05-20 (Gee)** to the app-execution wrapper —
this is now the 7-shot app demo + coach frame. Supersedes the earlier
"S4/S5 reframe" iterations from 2026-05-19. The whole structure now
mirrors `LESSONS.md` FIXED WRAPPER (locked 2026-05-20).
Structure: `lesson1-release-cut.mmd/.png`. This file adds the
**voiceover script** and **voice direction** on top of it. 9:16,
~40s, App-Store quality. Palette ONLY black `#000000` / signal green
`#00c896` / off-white `#eef6f3`. Coach-facing on-screen text = IBM
Plex Mono. Art direction (chibi vs. stylized adult) currently
**unlocked**, A/B test pending — see `lyra-art-direction-ab.md`.

## Lyra — visual identity (LOCKED)
Every frame matches the locked key still: job
`a777c0e0-195e-46f0-b9ae-11b4e45c9b66`. Chibi ~2.5 heads tall, chiton +
himation, bronze telescope, white marble terrace over the Aegean at
dawn, modern phone glowing signal-green on the ledge.

## Lyra — voice direction (LOCKED, Gee 2026-05-18)
- **Kind, but deeper.** A warm low female register — unhurried,
  grounded, never shrill, never bubbly.
- Calm authority: she asks more than she tells; lands the truth softly.
- Pace slow, generous pauses. Breath audible, intimate (close-mic).
- Reference feel: a wise older friend at dawn, not a narrator.
- Tooling note: the video model does NOT synthesize this voice. VO is
  a separate step (TTS/voice talent) then composited over the animation.

---

## Per-shot script (VO + on-screen mono)

### SHOT 1 — COLD OPEN: LYRA'S MORNING · 0–4s
- VISUAL: wide, Lyra at the bronze telescope on the white marble
  terrace over the Aegean, marking stars on a wax tablet, unaware.
  8% slow push-in, idle breathing, light motes. *Full-color Aegean.*
- AUDIO: soft sea + dawn birds. No music yet.
- VO (Lyra, quiet, almost to herself): "Every morning I measure the
  sky. And every morning the sky ignores me."

### SHOT 2 — THE NOTIFICATION · 4–7s
- VISUAL: cut tighter — modern phone on the marble ledge, dark screen
  → it lights up with a real lock-screen push notification. The
  notification card is the only black/green thing in frame.
  Light-streak wipe transition into shot 3.
- ON-SCREEN (the push card, IBM Plex Mono):
  ```
  Θ  THETA          now
  [LYRA] daily scan — matches your strategy
  "Some things are up to us; some are not."
  ```
  Banner uses signal green `#00c896` only on the Θ mark; everything
  else off-white on black.
- AUDIO: ambient ducks; one clean modern buzz.
- VO: (none — let the notification land. This IS how you get notified.)

### SHOT 3 — THE SCANNER (terminal home screen) · 7–13s
- VISUAL: Lyra picks up the phone, taps. The phone fills the frame;
  the screen is the REAL app terminal home (DESIGN §3b-1, approved
  render `96e246fb`). Pixel-faithful: IBM Plex Mono, pure black,
  constant `[<username>@theta ~] %` prompt, off-white majority text,
  cyan `[LYRA]` tag, readable blank-line-per-block spacing. The
  `[LYRA] scan — 18 May` block surfaces the day's trades that match
  the user's strategy — pipeline rows, holdings, vspreads. The cursor
  blinks. **This is sell point #1 — trades, surfaced for the user.**
- ON-SCREEN: the canonical scanner block from DESIGN §3b-1 — header,
  holdings, vspreads, pipeline — with a clear `[ PAPER TRADE ]`
  action button at the bottom.
- VO (Lyra, reading it back low and even): "Your scan. Today, on your
  strategy. Pick one — these are yours to take."

### SHOT 4 — THE ENTRY (paper-trade entry screen) · 13–22s
- VISUAL: Lyra taps a pipeline row (e.g. `MCO` or whichever lesson-1
  example). Transition to the paper-trade entry screen — same
  terminal aesthetic, IBM Plex Mono, black background. Three rows
  fill in via tap, not type: **underlying**, **stop**, **take-profit**.
  Editable rows render signal-green; market rows (price · news ·
  earnings) stay greyed/read-only. No chains. No greeks. No math
  visible. **Sell point #2 begins — this is how dead-easy it is.**
- ON-SCREEN (mono, after the prompt):
  ```
  [LYRA] new paper trade
    underlying       ▮ MCO
    stop             ▮ $420.00
    take-profit      ▮ $470.00
    price            — (live)
    news             — (not yours)
  ```
  Editable rows in signal green, greyed rows visibly read-only.
- VO (Lyra, calm, three short beats — one per tap): "Underlying.
  Stop. Take-profit. The rest isn't mine to set."

### SHOT 5 — THE REVIEW (paper-trade review screen) · 22–28s
- VISUAL: Lyra taps Review. The screen lands on the paper-trade
  review — the same terminal, now showing every value she entered,
  read back, with a clear non-removable `PAPER TRADE` badge in the
  header. Honest framing on-screen — no implication of real money.
  Defined risk is pre-filled from the entry. Lyra's small approving
  glance to camera.
- ON-SCREEN (mono):
  ```
  [LYRA] review              [ PAPER TRADE ]
    underlying       MCO
    stop             $420.00
    take-profit      $470.00
    size             1 contract
    max risk         $138.00     (defined)
  ```
- VO (Lyra, on confirm): "There's the trade I built. Nothing the
  market does next changes the work I just did."

### SHOT 6 — THE SEND + Θ LOGO · 28–34s
- VISUAL: Lyra taps **SEND**. The screen flashes the `PAPER TRADE
  SENT` confirmation — green Θ mark draws on in candlesticks, terminal
  prints the timestamp. Subtle motion: the order tag drops into a
  list, then the Θ logo lands center-frame. **Sell point #2 paid off —
  that easy.**
- ON-SCREEN (mono):
  ```
  [LYRA] sent — 18 May 09:42:11    [ PAPER TRADE ]
    Θ  paper order placed
    MCO  stop 420.00  tp 470.00  size 1
  ```
  Then a clean cut to the Θ mark, green-on-black, full frame.
- VO (Lyra, quiet): "Sent. Now I let it be what it's going to be."

### SHOT 7 — COACH LAND + Θ CTA · 34–40s
- VISUAL: pull back — Lyra sets the phone down, returns to the
  telescope; the marble terrace, the Aegean, the dawn. Ancient +
  modern in one frame. Θ draws on in green candlesticks.
- ON-SCREEN (end hook, locked 2026-05-18): `Θ` / `don't predict it. trade it. now.`
- VO (Lyra, the one line — softest, lands it): "You don't control the
  price. You control whether you deserved the trade."

---

## Production order (when credits allow)
Animation is generated per shot from the locked Lyra still as the start
frame (keeps identity). VO recorded/synthed separately to the script
above, then composited. Cost reality (starter plan, 2026-05-18): 5s
720p clip ≈ 22.5 cr; 4s 480p/fast ≈ 6 cr; full 7-shot lesson far
exceeds a 40-credit balance — needs a budget decision before full gen.
