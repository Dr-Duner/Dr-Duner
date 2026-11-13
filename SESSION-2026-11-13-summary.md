# Session summary — Eden / Personal Brand Strategist thread

Branch: `claude/eden-personal-brand-strategist-hc7fzc`
Brand-strategy work is **PAUSED here** — Kevin moved it elsewhere.
This file records what happened and what is still open.

---

## What happened

**1. Eden install failed — environment, not user error.**
`eden.so` and `mcp.eden.so` are both blocked by this environment's egress
proxy (403 on CONNECT). The install file, the five skill files, the zip
and the MCP server were all unreachable. Eden's installer also routes the
skill through their hosted MCP, so the skill would have been a thin
client over their server.

**2. Built an independent replacement instead**, at Kevin's direction
("i do not want it with eden"). `.claude/skills/personal-brand-strategist/`
— SKILL.md, four references, one HTML template. No Eden, no external MCP,
no network calls. Original work: Eden's SKILL.md was never reachable, so
none of their content was seen or copied.

**3. Repo rules added** (both in `CLAUDE.md`, auto-loaded every session):
- **RULE 1b** — SOAPscribe is discontinued; do not resurrect.
- **RULE 1c** — HIPAA governs all clinical content; never asked about.

**4. Ran the skill end to end.** Interview → positioning → name → tone →
episode slate → EP01 script → EP01 storyboard. Output in `brand/`.

**5. Side thread: dictation setup.** Unresolved — see below.

---

## Still open — Kevin's to do

| # | Item | Where |
|---|---|---|
| 1 | **Delete the ~16 SOAPscribe skills** still synced to the account. They re-inject SOAPscribe as live context every session; `CLAUDE.md` RULE 1b only overrides them repo-side. | claude.ai → Settings → Skills |
| 2 | **Register the handles** — "Blame the Dentist", confirmed available on both. | YouTube + Reddit |
| 3 | **Dictation** — the input-meter test was never reported back (Mac: Settings → Sound → Input; Windows: Settings → System → Sound → Input). Bars moving = permissions problem; bars still = wrong input device or another app holding the mic. | His machine |

## Still open — needs Kevin's input before anyone can act

| # | Item |
|---|---|
| 4 | **Rewrite 3 SOAPscribe-framed but reusable skills** (`landing-page-copy`, `soap-note-engine`, `nextjs-saas-deploy`) to strip the dead-product framing. Offered, never taken up. Would be handed over as files to re-upload — cannot be installed to the account from here. |

## Paused — brand strategy, moved elsewhere

Not to be continued in this thread. Recorded so nothing is lost:

- EP01 **S7 shot** — two candidates generated, neither picked
- EP01 **narrator voice** — four tests submitted, session interrupted
  before they returned; never auditioned
- EP01 remaining production — voiceover, assembly, burned subtitles,
  thumbnail
- EP02 ("The four parents I meet every day") — slated, not built

State at pause: script locked and clinically checked; both bookend
frames final; middle six shots generated and unreviewed; character
bible locked. ~148.5 Higgsfield credits remaining, ~50 spent.

---

## Files produced

| Path | What |
|---|---|
| `.claude/skills/personal-brand-strategist/` | The skill — 6 files |
| `brand/brand-strategy.md` | Positioning, name, tone, formats, episode slate, 90-day plan |
| `brand/scripts/ep01-the-5pm-four-year-old.md` | EP01 script, shot plan, generation log, technique notes |
| `CLAUDE.md` | RULE 1b, RULE 1c |

Everything is committed and pushed. The container is ephemeral; the
repo is the only thing that survives.
