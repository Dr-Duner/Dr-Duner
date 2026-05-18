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

    def to_dict(self) -> dict:
        return {
            "review": self.review.to_dict(),
            "variants": [vars(v) for v in self.variants],
            "used_fallback": self.used_fallback,
        }


@dataclass
class PracticeConfig:
    practice_name: str = "Your Practice"
    office_phone: str = ""
    sign_off: str = "— The Team"
    voice_profile: dict = field(default_factory=dict)
    platforms: list[str] = field(default_factory=lambda: ["google"])

    @staticmethod
    def from_dict(d: dict) -> "PracticeConfig":
        return PracticeConfig(
            practice_name=d.get("practice_name", "Your Practice"),
            office_phone=d.get("office_phone", ""),
            sign_off=d.get("sign_off", "— The Team"),
            voice_profile=d.get("voice_profile", {}),
            platforms=d.get("platforms", ["google"]),
        )
