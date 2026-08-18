"""Tests for the Entity Resolver and player identity pipeline."""

import pytest
from src.domain.enums import IdentityConfidence
from src.normalization.entity_resolver import EntityResolver
from src.normalization.slugs import normalize_string, generate_player_slug


def test_string_normalization():
    assert normalize_string("Pau Gasol Sáez") == "pau gasol saez"
    assert normalize_string("NAVARRO, J.C.") == "navarro j c"
    assert normalize_string("Jonas Valančiūnas") == "jonas valanciunas"


def test_deterministic_slug_generator():
    slug = generate_player_slug("Pau Gasol", 1980)
    assert slug == "pau_gasol_1980"


def test_entity_resolver_pipeline():
    resolver = EntityResolver()
    # Register canonical players
    resolver.register_canonical_player("pau_gasol_1980", "Pau Gasol", 1980, "C")
    resolver.register_canonical_player("marc_gasol_1985", "Marc Gasol", 1985, "C")

    # Register aliases
    resolver.register_alias("pau_gasol_1980", "Pau Gasol Sáez", "ESP", "SRC_FIBA", "38029")
    resolver.register_alias("pau_gasol_1980", "GASOL, P.", "ESP", "SRC_BREF", "gasolpa01")

    # 1. Exact Source ID match
    p_id, conf = resolver.resolve("Unknown String", "ESP", "SRC_FIBA", "38029")
    assert p_id == "pau_gasol_1980"
    assert conf == IdentityConfidence.EXACT

    # 2. Exact Alias match (String + Country)
    p_id2, conf2 = resolver.resolve("pau gasol saez", "ESP")
    assert p_id2 == "pau_gasol_1980"
    assert conf2 == IdentityConfidence.DETERMINISTIC

    # 3. Deterministic match by name + birth_year
    p_id3, conf3 = resolver.resolve("Marc Gasol", "ESP", birth_year=1985)
    assert p_id3 == "marc_gasol_1985"
    assert conf3 == IdentityConfidence.DETERMINISTIC

    # 4. Unresolved fallback
    p_id4, conf4 = resolver.resolve("Completely Unknown Player", "ARG")
    assert "unresolved" in p_id4
    assert conf4 == IdentityConfidence.UNRESOLVED
