"""Name slugification and string normalization."""

import re
import unicodedata


def normalize_string(text: str) -> str:
    """Normalize unicode characters, strip accents, remove punctuation and lower-case."""
    if not text:
        return ""
    # Normalize unicode to NFD and strip combining accents
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_text = "".join([c for c in nfkd if not unicodedata.combining(c)])
    # Lowercase and replace non-alphanumeric with spaces
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", ascii_text).lower()
    # Collapse whitespace
    return " ".join(cleaned.split())


def generate_player_slug(canonical_name: str, birth_year: int) -> str:
    """Generate deterministic canonical player slug: e.g. 'pau_gasol_1980'."""
    norm = normalize_string(canonical_name)
    slug_part = "_".join(norm.split())
    return f"{slug_part}_{birth_year}"


def generate_game_slug(tournament_id: str, stage_slug: str, home_team: str, away_team: str) -> str:
    """Generate canonical game slug: e.g. 'eurobasket_2011_final_esp_fra'."""
    return f"{tournament_id}_{stage_slug}_{home_team.lower()}_{away_team.lower()}"
