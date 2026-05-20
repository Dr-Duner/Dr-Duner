"""Plain data shapes shared across modules."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Review:
    text: str
    author: str = ""
    rating: Optional[int] = None  # 1-5, None if unknown (plain paste)
    platform: str = "manual"      # google | yelp | manual | other
    date: str = ""

    @property
    def is_negative(self) -> bool:
        return self.rating is not None and self.rating <= 2

    def to_dict(self) -> dict:
        d = asdict(self)
        d["is_negative"] = self.is_negative
        return d


@dataclass
class DraftVariant:
    text: str
    why_safe: str
    label: str = ""  # "Short & warm" / "Fuller"


@dataclass
class DraftedReview:
    review: Review
    variants: list[DraftVariant] = field(default_factory=list)
    used_fallback: bool = False
    approval_mode: str = "explicit"  # explicit | bulk | auto

    def to_dict(self) -> dict:
        return {
            "review": self.review.to_dict(),
            "variants": [vars(v) for v in self.variants],
            "used_fallback": self.used_fallback,
            "approval_mode": self.approval_mode,
        }


@dataclass
class PracticeConfig:
    practice_name: str = "Your Practice"
    office_phone: str = ""
    sign_off: str = "— The Team"
    voice_profile: dict = field(default_factory=dict)
    # Client picks one: email | link | sms (all supported).
    approval_channel: str = "email"
    approver_contact: str = ""
    # If true, 4-5★ replies skip explicit approval. 1-3★ never do.
    auto_approve_positives: bool = False
    platforms: list[str] = field(default_factory=lambda: ["google"])

    @staticmethod
    def from_dict(d: dict) -> "PracticeConfig":
        return PracticeConfig(
            practice_name=d.get("practice_name", "Your Practice"),
            office_phone=d.get("office_phone", ""),
            sign_off=d.get("sign_off", "— The Team"),
            voice_profile=d.get("voice_profile", {}),
            approval_channel=d.get("approval_channel", "email"),
            approver_contact=d.get("approver_contact", ""),
            auto_approve_positives=d.get("auto_approve_positives", False),
            platforms=d.get("platforms", ["google"]),
        )


def approval_mode(review: Review, practice: PracticeConfig) -> str:
    """Routing rule: positives (4-5★) are bulk-approvable, or auto if
    the practice opted in. 1-3★ and unknown rating ALWAYS require
    explicit per-reply client approval. Never auto-post a 1-3★."""
    is_positive = review.rating is not None and review.rating >= 4
    if not is_positive:
        return "explicit"
    return "auto" if practice.auto_approve_positives else "bulk"
