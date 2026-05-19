# Lesson 1 — The Dichotomy of Control · FINAL SHOOTING SCRIPT

Status: storyboard + voiceover **locked** 2026-05-18 (Gee).
Structure is the LOCKED release cut (`lesson1-release-cut.mmd/.png`) —
this file adds the **voiceover script** and **voice direction** on top
of it. 9:16, ~40s, chibi 2.5D, App-Store quality. Palette ONLY black
`#000000` / signal green `#00c896` / off-white `#eef6f3`. Coach-facing
on-screen text = IBM Plex Mono.

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
- VISUAL: wide, chibi Lyra at the bronze telescope, marking stars on a
  wax tablet, unaware. 8% slow push-in, idle breathing, light motes.
- AUDIO: soft sea + dawn birds. No music yet.
- VO (Lyra, quiet, almost to herself): "Every morning I measure the
  sky. And every morning the sky ignores me."

### SHOT 2 — THE BUZZ · 4–7s
- VISUAL: cut tighter — modern phone on the marble ledge, dark screen →
  single green pulse. Lyra's head snaps, surprise pop. Light-streak wipe.
- AUDIO: ambient ducks; one clean modern buzz (the hook).
- VO: (none — let the buzz land.)

### SHOT 3 — THE READ (mono) · 7–11s
- VISUAL: phone fills frame, Lyra's chibi face at the edge. The screen
  is the REAL app terminal — pixel-faithful to the canonical home
  screen (DESIGN §3b-1, approved render `96e246fb`): IBM Plex Mono,
  pure black, the constant `[<username>@theta ~] %` prompt, off-white
  majority text, blank-line-per-block readable spacing, cyan `[LYRA]`
  tag. This is exactly what the user sees when a THETA message lands —
  not a bespoke title card. Message types into the terminal flow.
- ON-SCREEN (in the terminal, after the prompt line):
  `[LYRA] msg — 18 May` (cyan tag), then off-white:
  `> THETA: you think you control the outcome.`
  `> you don't.`  (signal green stays reserved for +delta only)
- VO (Lyra, reading it back low and even): "You think you control the
  outcome. You don't."

### SHOT 4 — QUOTE + OPEN THE PAPER TRADE · 11–20s
- VISUAL: full-frame black app card. Θ mark, then the line types in
  (off-white mono, signal green reserved). The quote lands, then the
  card transitions into our REAL paper-trade entry screen and the
  coach acts on it: picks the underlying (ticker) to trade. Dichotomy
  is baked into the screen itself — editable fields (signal green) =
  what you control; read-only/greyed = what you don't.
- ON-SCREEN (mono): `Some things are up to us; some are not.`
  `—Epictetus` → then the live paper-trade entry screen, underlying
  field selected (green/editable), market fields greyed.
- VO (Lyra, calm): "Two thousand years ago a slave wrote that down.
  It still holds. Watch — I'll only touch what's mine."

### SHOT 5 — CONFIRM THE ENTERED TRADE · 20–31s
- VISUAL: the real paper-trade confirmation screen, reading back the
  exact numbers the coach entered — underlying, entry, exit, size,
  everything — in signal green (the inputs that were theirs). The
  uncontrollable rows — price · earnings · the storm at sea — stay
  greyed/read-only. The green-vs-grey on the real screen IS the lesson:
  taught by what the screen let the coach touch, not narrated.
- ON-SCREEN (mono): confirmation rows, green `underlying · entry ·
  exit · size = <entered values>` / grey `price · news · storm  —`
- VO (Lyra, on confirm): "Your method is yours. The chart never was.
  I set what I control; the rest just happens."

### SHOT 6 — SCAN: LIVE CARD (1:1 app UI) · 31–36s
- VISUAL: a real scanner card. Editable = size / entry / exit (signal
  green). Read-only + dimmed = price / news ("not yours"). Defined risk
  pre-filled. Lyra: small approving glance to camera.
- ON-SCREEN: the shipping scanner card UI EXACTLY as the app renders
  it (DESIGN §3b-1 + ref `96e246fb`): same terminal, constant
  `[<username>@theta ~] %` prompt, `[LYRA] scan — 18 May` in cyan,
  off-white scan rows, amber `!` for any alert, green only on a
  `+delta`, `[ PAPER TRADE ] [ OPEN BROKERAGE ]` action line. The
  in-video screen and the real app are the same screen.
- VO (Lyra, low, sure): "This is the only part you touch. Make it
  deserve the trade."

### SHOT 7 — COACH LAND + Θ CTA · 36–40s
- VISUAL: Lyra sets the phone down, returns to the telescope; camera
  pulls back — ancient + modern in one frame. Θ draws on in green
  candlesticks.
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
