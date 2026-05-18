"""Deterministic HIPAA gate. Mirrors the hipaa-review-compliance skill.

This runs with NO API key and is the product's moat. Edit the term
lists below as new edge cases appear — this module is the source of
truth for what a reply may not say. A draft that fails here is never
shown; the drafter regenerates or falls back to a safe template.
"""
from __future__ import annotations

import re

# Treatment / procedure terms that must not appear as care received,
# even if the reviewer mentioned them first (can't ratify PHI).
TREATMENT_TERMS = [
    "cleaning", "filling", "crown", "root canal", "extraction",
    "implant", "whitening", "braces", "invisalign", "denture",
    "x-ray", "xray", "exam", "surgery", "anesthesia", "sedation",
    "cavity", "veneer", "bridge", "molar", "wisdom tooth",
]

# Visit / appointment phrases that confirm a care relationship.
VISIT_PHRASES = [
    "your appointment", "your visit", "when you came in",
    "see you next", "your next visit", "your last visit",
    "next time you're in", "your treatment", "your procedure",
    "during your", "at your appointment", "see you soon",
]

# Phrasing that confirms the reviewer is/was a patient.
PATIENT_CONFIRMING_PHRASES = [
    "thank you for choosing", "thank you for trusting us with",
    "thanks for trusting us with", "as our patient", "your dentist",
    "glad we could treat", "glad we could fix", "glad we could help you with",
    "we treated", "we fixed", "we extracted", "we placed",
    "trusting us with your", "for choosing us for your",
]


def _hits(text: str, needles: list[str]) -> list[str]:
    low = text.lower()
    found = []
    for n in needles:
        # word-boundary match for single words, substring for phrases
        if " " in n:
            if n in low:
                found.append(n)
        elif re.search(rf"\b{re.escape(n)}\b", low):
            found.append(n)
    return found


def scan(text: str) -> tuple[bool, list[str]]:
    """Return (passed, violations). passed=True means HIPAA-safe."""
    violations: list[str] = []
    for term in _hits(text, TREATMENT_TERMS):
        violations.append(f"treatment term: '{term}'")
    for phrase in _hits(text, VISIT_PHRASES):
        violations.append(f"visit/appointment phrasing: '{phrase}'")
    for phrase in _hits(text, PATIENT_CONFIRMING_PHRASES):
        violations.append(f"patient-confirming phrasing: '{phrase}'")
    return (len(violations) == 0, violations)


def why_safe_note(text: str) -> str:
    """One-line confidence note for the approver (only call when passed)."""
    return "Generic thanks; no patient status, visit, or treatment referenced."
