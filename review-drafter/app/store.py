"""Per-practice approval/posted state. File-backed, isolated per practice.

Phase 2 persists the review lifecycle so approvals survive a restart and
the operator can see queue state. Stored content is the *public* Google
review text + our draft + decision metadata — no PHI (the HIPAA gate
guarantees drafts carry none, and review text is already public). The
data dir is gitignored and never shared across practices.
"""
from __future__ import annotations

import hashlib
import json
import secrets
import threading
import time
from dataclasses import asdict, dataclass, field

from .config import ROOT

DATA_DIR = ROOT / "data"
_LOCK = threading.Lock()

# Lifecycle: pending -> approved -> posted ; or pending -> rejected.
PENDING, APPROVED, REJECTED, POSTED = "pending", "approved", "rejected", "posted"


def _now() -> float:
    return round(time.time(), 3)


def item_id(practice: str, author: str, date: str, text: str) -> str:
    raw = f"{practice}|{author}|{date}|{text}".encode()
    return hashlib.sha1(raw).hexdigest()[:16]


@dataclass
class ApprovalItem:
    id: str
    practice: str
    review: dict
    reply: str
    why_safe: str
    approval_mode: str           # explicit | bulk | auto
    status: str = PENDING
    token: str = ""
    channel: str = "email"
    created_at: float = field(default_factory=_now)
    decided_at: float | None = None
    posted_at: float | None = None
    posted_ref: str = ""         # provider id for the posted reply
    history: list = field(default_factory=list)

    def log(self, event: str, **extra) -> None:
        self.history.append({"t": _now(), "event": event, **extra})


def _dir(practice: str):
    d = DATA_DIR / practice
    d.mkdir(parents=True, exist_ok=True)
    return d


def _path(practice: str):
    return _dir(practice) / "approvals.json"


def _load_raw(practice: str) -> dict[str, dict]:
    p = _path(practice)
    if not p.exists():
        return {}
    return json.loads(p.read_text() or "{}")


def _save_raw(practice: str, data: dict[str, dict]) -> None:
    _path(practice).write_text(json.dumps(data, indent=2, sort_keys=True))


def upsert_batch(practice: str, items: list[ApprovalItem]) -> list[ApprovalItem]:
    """Add new items; never resurrect or duplicate a decided one."""
    with _LOCK:
        data = _load_raw(practice)
        for it in items:
            if it.id in data and data[it.id]["status"] != PENDING:
                continue  # already decided/posted — leave it
            data[it.id] = asdict(it)
        _save_raw(practice, data)
    return list_items(practice)


def list_items(practice: str, status: str | None = None) -> list[ApprovalItem]:
    data = _load_raw(practice)
    out = [ApprovalItem(**v) for v in data.values()]
    if status:
        out = [i for i in out if i.status == status]
    return sorted(out, key=lambda i: i.created_at)


def get(practice: str, item_id_: str) -> ApprovalItem | None:
    d = _load_raw(practice).get(item_id_)
    return ApprovalItem(**d) if d else None


def find_by_token(token: str) -> tuple[str, ApprovalItem] | None:
    if not token or not DATA_DIR.exists():
        return None
    for pd in DATA_DIR.iterdir():
        if not pd.is_dir():
            continue
        for v in _load_raw(pd.name).values():
            if v.get("token") == token:
                return pd.name, ApprovalItem(**v)
    return None


def save(item: ApprovalItem) -> None:
    with _LOCK:
        data = _load_raw(item.practice)
        data[item.id] = asdict(item)
        _save_raw(item.practice, data)


def new_token() -> str:
    return secrets.token_urlsafe(18)
