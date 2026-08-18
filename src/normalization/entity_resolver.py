"""Deterministic entity resolver for player identities across multi-era sources."""

from typing import Dict, Optional, Tuple
from difflib import SequenceMatcher
from src.domain.enums import IdentityConfidence
from src.normalization.slugs import normalize_string, generate_player_slug


class EntityResolver:
    """Multi-stage deterministic entity resolver with alias caching."""

    def __init__(self):
        # Maps (source_id, source_player_id) -> canonical_player_id
        self._source_id_index: Dict[Tuple[str, str], str] = {}
        # Maps (normalized_name, country_code) -> canonical_player_id
        self._alias_index: Dict[Tuple[str, str], str] = {}
        # Known canonical player directory
        self._canonical_players: Dict[str, dict] = {}

    def register_canonical_player(
        self,
        canonical_player_id: str,
        full_canonical_name: str,
        birth_year: int,
        primary_position: str,
        birth_date: Optional[str] = None,
    ) -> None:
        """Register a canonical person in the resolver index."""
        self._canonical_players[canonical_player_id] = {
            "canonical_player_id": canonical_player_id,
            "full_canonical_name": full_canonical_name,
            "birth_year": birth_year,
            "primary_position": primary_position,
            "birth_date": birth_date,
        }

    def register_alias(
        self,
        canonical_player_id: str,
        raw_name: str,
        country_code: str,
        source_id: Optional[str] = None,
        source_player_id: Optional[str] = None,
    ) -> None:
        """Register a source alias or name variation."""
        norm_name = normalize_string(raw_name)
        self._alias_index[(norm_name, country_code.upper())] = canonical_player_id
        if source_id and source_player_id:
            self._source_id_index[(source_id, str(source_player_id))] = canonical_player_id

    def resolve(
        self,
        raw_name: str,
        country_code: str,
        source_id: Optional[str] = None,
        source_player_id: Optional[str] = None,
        birth_year: Optional[int] = None,
    ) -> Tuple[str, IdentityConfidence]:
        """Resolve a raw player appearance to canonical_player_id and confidence score."""
        country = country_code.upper() if country_code else "UNK"

        # Stage 1: Exact source ID lookup
        if source_id and source_player_id:
            key = (source_id, str(source_player_id))
            if key in self._source_id_index:
                return self._source_id_index[key], IdentityConfidence.EXACT

        norm_name = normalize_string(raw_name)

        # Stage 2: Exact Alias Match (Name + Country)
        alias_key = (norm_name, country)
        if alias_key in self._alias_index:
            return self._alias_index[alias_key], IdentityConfidence.DETERMINISTIC

        # Stage 3: Deterministic Generation (if birth_year provided)
        if birth_year:
            candidate_slug = generate_player_slug(raw_name, birth_year)
            if candidate_slug in self._canonical_players:
                return candidate_slug, IdentityConfidence.DETERMINISTIC

        # Stage 4: High-threshold fuzzy matching within the same country
        best_match_id: Optional[str] = None
        best_ratio = 0.0

        for (known_name, known_country), can_id in self._alias_index.items():
            if known_country == country:
                ratio = SequenceMatcher(None, norm_name, known_name).ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match_id = can_id

        if best_ratio >= 0.94 and best_match_id:
            return best_match_id, IdentityConfidence.PROBABILISTIC

        # Stage 5: Unresolved fallback
        fallback_slug = f"unresolved_{norm_name.replace(' ', '_')}_{country.lower()}"
        return fallback_slug, IdentityConfidence.UNRESOLVED
