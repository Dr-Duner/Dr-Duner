"""Google Business Profile seam: ingest reviews + post replies.

Real posting requires the Google Business Profile API + a per-practice
OAuth grant. That access application has lead time and is NOT wired
here. This module defines the exact seam so the live adapter is a small,
known change once access + tokens exist:

  * scope: https://www.googleapis.com/auth/business.manage
  * endpoint: accounts.locations.reviews.updateReply
              PUT .../{name}/reply  body {"comment": "<text>"}
  * ingest:  accounts.locations.reviews.list (poll new since last cursor)

`SimulatedGoogleClient` is the offline default: it reads reviews from a
fixture and records "posted" replies to a per-practice file so the whole
Phase 2 flow is provable without credentials. `LiveGoogleClient` is the
stub that refuses to pretend — it raises until real OAuth is configured.
"""
from __future__ import annotations

import json
from typing import Protocol

from .config import FIXTURES_DIR
from .parser import parse
from .store import _dir


class GoogleNotConfigured(RuntimeError):
    pass


class GoogleClient(Protocol):
    def list_reviews(self, location: str) -> list: ...
    def post_reply(self, practice: str, review_ref: str,
                   text: str) -> str: ...


class SimulatedGoogleClient:
    """Offline stand-in. NOT live. Proves the pipeline end-to-end."""

    live = False

    def __init__(self, fixture: str = "dental_reviews.csv"):
        self._fixture = FIXTURES_DIR / fixture

    def list_reviews(self, location: str) -> list:
        if not self._fixture.exists():
            return []
        return parse(self._fixture.read_text(), is_csv=True)

    def post_reply(self, practice: str, review_ref: str, text: str) -> str:
        log = _dir(practice) / "posted.jsonl"
        ref = f"sim-reply-{abs(hash((review_ref, text))) % 10**8:08d}"
        with log.open("a") as fh:
            fh.write(json.dumps(
                {"review_ref": review_ref, "reply": text, "ref": ref}) + "\n")
        return ref


class LiveGoogleClient:
    """Real adapter placeholder. Refuses rather than fake a live post."""

    live = True

    def __init__(self, oauth_token: str | None = None):
        self._token = oauth_token

    def list_reviews(self, location: str) -> list:
        raise GoogleNotConfigured(
            "Google Business Profile API access not yet granted. "
            "Start the access application; see module docstring.")

    def post_reply(self, practice: str, review_ref: str, text: str) -> str:
        raise GoogleNotConfigured(
            "No OAuth grant for this practice. Capture it at onboarding "
            "(scope business.manage) before live posting.")


def get_client(prefer_live: bool = False) -> GoogleClient:
    """Default to the simulator. A live client only when explicitly
    asked AND it would itself enforce the credential requirement."""
    return LiveGoogleClient() if prefer_live else SimulatedGoogleClient()
