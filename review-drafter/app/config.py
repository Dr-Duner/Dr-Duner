"""Single place for runtime config. Edit env, not code."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRACTICES_DIR = ROOT / "practices"
FIXTURES_DIR = ROOT / "fixtures"

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6").strip()

# Drafting behaviour knobs (first-draft defaults; tune freely).
MAX_COMPLIANCE_RETRIES = 2
MAX_OUTPUT_TOKENS = 1024


def has_api_key() -> bool:
    return bool(ANTHROPIC_API_KEY)
