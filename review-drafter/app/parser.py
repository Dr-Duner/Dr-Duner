"""Turn pasted text or a CSV export into normalized Review[].

Flexible CSV headers; plain paste = one review per block (blocks split
on a '---' line or a blank line).
"""
from __future__ import annotations

import csv
import io
import re

from .models import Review

# Map many possible export headers onto our fields.
_HEADER_ALIASES = {
    "text": {"text", "review", "review text", "comment", "content", "body"},
    "author": {"author", "name", "reviewer", "customer", "reviewer name"},
    "rating": {"rating", "stars", "star rating", "score"},
    "platform": {"platform", "source", "site"},
    "date": {"date", "created", "review date", "time"},
}


def _canonical(header: str) -> str | None:
    h = header.strip().lower()
    for canon, aliases in _HEADER_ALIASES.items():
        if h in aliases:
            return canon
    return None


def _coerce_rating(value: str) -> int | None:
    if not value:
        return None
    m = re.search(r"[1-5]", str(value))
    return int(m.group()) if m else None


def parse_csv(raw: str) -> list[Review]:
    reader = csv.DictReader(io.StringIO(raw))
    if not reader.fieldnames:
        return []
    colmap = {fn: _canonical(fn) for fn in reader.fieldnames}
    reviews: list[Review] = []
    for row in reader:
        fields = {"text": "", "author": "", "rating": None,
                  "platform": "other", "date": ""}
        for raw_col, canon in colmap.items():
            if canon is None:
                continue
            val = (row.get(raw_col) or "").strip()
            if canon == "rating":
                fields["rating"] = _coerce_rating(val)
            else:
                fields[canon] = val
        if not fields["text"]:
            continue  # reject rows with no review text
        reviews.append(Review(**fields))
    return reviews


def parse_pasted_text(raw: str) -> list[Review]:
    raw = raw.strip()
    if not raw:
        return []
    # Split on a line that is only dashes, else on blank lines.
    if re.search(r"^\s*-{3,}\s*$", raw, re.M):
        blocks = re.split(r"^\s*-{3,}\s*$", raw, flags=re.M)
    else:
        blocks = re.split(r"\n\s*\n", raw)
    reviews = []
    for b in blocks:
        b = b.strip()
        if b:
            reviews.append(Review(text=b, platform="manual"))
    return reviews


def parse(raw: str, is_csv: bool) -> list[Review]:
    return parse_csv(raw) if is_csv else parse_pasted_text(raw)
