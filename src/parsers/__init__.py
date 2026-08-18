"""Parsers package for tournament match tables and boxscores."""

from src.parsers.eurobasket_match_parser import parse_match_table, clean_text, TEAM_NAME_MAP

__all__ = ["parse_match_table", "clean_text", "TEAM_NAME_MAP"]
