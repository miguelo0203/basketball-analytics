"""Match table parsing and score extraction for international basketball tournaments (EuroBasket, World Cup, Olympics)."""

import re
from typing import Dict, Any, Optional, List
from bs4 import BeautifulSoup
import unicodedata

# Enhanced Mapping from common country names to canonical 3-letter codes
TEAM_NAME_MAP = {
    # Europe
    "spain": "ESP",
    "france": "FRA",
    "germany": "GER",
    "lithuania": "LTU",
    "serbia": "SRB",
    "serbia and montenegro": "SCG",
    "montenegro": "MNE",
    "greece": "GRE",
    "italy": "ITA",
    "russia": "RUS",
    "croatia": "CRO",
    "slovenia": "SLO",
    "turkey": "TUR",
    "israel": "ISR",
    "latvia": "LAT",
    "poland": "POL",
    "ukraine": "UKR",
    "georgia": "GEO",
    "czech republic": "CZE",
    "czechia": "CZE",
    "belgium": "BEL",
    "great britain": "GBR",
    "finland": "FIN",
    "bosnia and herzegovina": "BIH",
    "macedonia": "MKD",
    "north macedonia": "MKD",
    "f.y.r.o.m": "MKD",
    "fyrom": "MKD",
    "bulgaria": "BUL",
    "hungary": "HUN",
    "netherlands": "NED",
    "sweden": "SWE",
    "iceland": "ISL",
    "portugal": "POR",
    "estonia": "EST",
    "romania": "ROU",

    # Americas
    "united states": "USA",
    "usa": "USA",
    "argentina": "ARG",
    "brazil": "BRA",
    "canada": "CAN",
    "puerto rico": "PUR",
    "venezuela": "VEN",
    "dominican republic": "DOM",
    "mexico": "MEX",
    "panama": "PAN",

    # Asia & Oceania
    "australia": "AUS",
    "new zealand": "NZL",
    "china": "CHN",
    "japan": "JPN",
    "philippines": "PHI",
    "iran": "IRI",
    "jordan": "JOR",
    "lebanon": "LBN",
    "south korea": "KOR",
    "korea": "KOR",
    "qatar": "QAT",

    # Africa
    "nigeria": "NGR",
    "angola": "ANG",
    "senegal": "SEN",
    "tunisia": "TUN",
    "egypt": "EGY",
    "ivory coast": "CIV",
    "cote d'ivoire": "CIV",
    "south sudan": "SSD",
    "cape verde": "CPV",
}


def clean_text(text: str) -> str:
    """Normalize unicode characters and whitespace."""
    if not text:
        return ""
    norm = unicodedata.normalize("NFKD", text)
    ascii_text = "".join([c for c in norm if not unicodedata.combining(c)])
    return " ".join(ascii_text.split())


def parse_match_table(
    table: BeautifulSoup,
    tournament_id: str,
    default_stage: str = "Group Phase",
) -> Optional[Dict[str, Any]]:
    """Parse a single basketball match table extracting teams, score, overtimes, and date."""
    text = clean_text(table.get_text(separator=" ", strip=True))
    if "Pts:" not in text and "Pts :" not in text:
        return None

    # Check overtimes
    overtimes = 0
    if "(3OT)" in text or "3OT" in text or "triple overtime" in text.lower():
        overtimes = 3
    elif "(2OT)" in text or "2OT" in text or "second overtime" in text.lower():
        overtimes = 2
    elif "(OT)" in text or "Overtime" in text or "overtime" in text.lower():
        overtimes = 1

    # Strip footnote references like [1], [a], [0] before regex matching
    cleaned_score_text = re.sub(r'\[[a-zA-Z0-9]\]', '', text)
    # Remove 0/letter prefix from (OT)/(2OT): e.g. 76 0 (OT) -> 76 (OT), 109 0 (2OT) -> 109 (2OT)
    cleaned_score_text = re.sub(r'(\d{2,3})\s*[0oOa-zA-Z]\s*\((3?2?OT)\)', r'\1 (\2)', cleaned_score_text)
    cleaned_score_text = re.sub(r'(\d{2,3})0\((3?2?OT)\)', r'\1 (\2)', cleaned_score_text)

    # Match pattern: TeamA score1 - score2 TeamB
    score_match = re.search(
        r'([A-Za-z\s\.\-\'\’]+?)\s+(\d{2,3})\s*[–\-\?]\s*(\d{2,3})\s*(?:\(OT\)|\(2OT\)|\(3OT\)|(?:\([A-Za-z0-9]+\)))?\s*([A-Za-z\s\.\-\'\’]+)',
        cleaned_score_text,
    )
    if not score_match:
        return None

    raw_home = score_match.group(1).strip()
    home_score = int(score_match.group(2))
    away_score = int(score_match.group(3))
    raw_away = score_match.group(4).strip()

    # Resolve team codes
    home_code = None
    away_code = None

    for name, code in sorted(TEAM_NAME_MAP.items(), key=lambda x: len(x[0]), reverse=True):
        if not home_code and name in raw_home.lower():
            home_code = code
        if not away_code and name in raw_away.lower():
            away_code = code

    if not home_code or not away_code:
        return None

    date_match = re.search(
        r'(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})',
        text,
    )
    game_date = date_match.group(1) if date_match else "Unknown"

    return {
        "tournament_id": tournament_id,
        "stage": default_stage,
        "home_team_id": home_code,
        "away_team_id": away_code,
        "home_score": home_score,
        "away_score": away_score,
        "overtimes": overtimes,
        "game_date": game_date,
    }


def parse_compact_group_table(
    table: BeautifulSoup,
    tournament_id: str,
    default_stage: str = "Preliminary Round",
) -> List[Dict[str, Any]]:
    """Parse compact group result tables (e.g. 2006 FIBA World Championship summary rows)."""
    matches = []
    pattern = r'([A-Za-z\s\.\-\'\’]+?)\s+(\d{2,3})\s*[–\-\?]\s*(\d{2,3})\s*(?:\(OT\)|\(2OT\)|\(3OT\))?\s*([A-Za-z\s\.\-\'\’]+)'
    
    rows = table.find_all('tr')
    for tr in rows:
        row_text = clean_text(tr.get_text())
        if "Pts:" in row_text or "Scoring by quarter" in row_text:
            continue
            
        overtimes = 0
        if "(3OT)" in row_text:
            overtimes = 3
        elif "(2OT)" in row_text:
            overtimes = 2
        elif "(OT)" in row_text:
            overtimes = 1

        m = re.search(pattern, row_text)
        if m:
            raw_home = m.group(1).strip()
            score_home = int(m.group(2))
            score_away = int(m.group(3))
            raw_away = m.group(4).strip()

            home_code = None
            away_code = None
            for name, code in sorted(TEAM_NAME_MAP.items(), key=lambda x: len(x[0]), reverse=True):
                if not home_code and name in raw_home.lower():
                    home_code = code
                if not away_code and name in raw_away.lower():
                    away_code = code

            if home_code and away_code:
                matches.append({
                    "tournament_id": tournament_id,
                    "stage": default_stage,
                    "home_team_id": home_code,
                    "away_team_id": away_code,
                    "home_score": score_home,
                    "away_score": score_away,
                    "overtimes": overtimes,
                    "game_date": "Historical",
                })
    return matches
