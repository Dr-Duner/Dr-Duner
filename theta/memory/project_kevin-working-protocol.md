# project_ Kevin's Theta working protocol (adopted, repo-adapted)

Original referenced Mac-local paths (~/.claude/..., ~/gamedev/stockpile)
unreachable from cloud. Adapted to git-tracked repo paths so it works
from both Mac and any cloud session.

1. **Binding memory:** `theta/memory/MEMORY.md` index + the files it
   points to. Read before Theta work; act on decided things, do not
   re-litigate.

2. **Memory-capture:** on a correction or "remember this", immediately
   create a type-prefixed `.md` (`feedback_/user_/project_/reference_`)
   in `theta/memory/`, add a one-line pointer in `MEMORY.md`, commit +
   push the same turn.

3. **Session backup ritual** (on "create a handoff" / "back it up" / end
   of session): (a) rewrite `theta/HANDOFF.md` — fixed sections,
   <=100 lines, Gee-facing, Gee is he/him; (b) distill durable decisions
   into a `project_` memory file indexed in MEMORY.md; (c) write
   git-tracked `theta/SESSION-YYYY-MM-DD.md`. Git is the only
   transfer/backup channel.

4. **Style:** detailed-but-decisive, no recaps, pick one and execute,
   end on one clear next action, cite code as path:line, honor any
   banned-words list once it exists in the repo.
