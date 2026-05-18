"""Load per-practice configs from practices/*.json."""
from __future__ import annotations

import json

from .config import PRACTICES_DIR
from .models import PracticeConfig


def list_practices() -> list[str]:
    return sorted(p.stem for p in PRACTICES_DIR.glob("*.json"))


def load_practice(name: str) -> PracticeConfig:
    path = PRACTICES_DIR / f"{name}.json"
    if not path.exists():
        return PracticeConfig()
    return PracticeConfig.from_dict(json.loads(path.read_text()))
