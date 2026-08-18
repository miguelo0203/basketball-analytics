"""Parser for international squad rosters and player boxscores across 2005–2025 tournaments."""

import re
from typing import Dict, List, Optional, Tuple, Any
from bs4 import BeautifulSoup
import pandas as pd

from src.normalization.slugs import generate_player_slug, normalize_string
from src.parsers.eurobasket_match_parser import TEAM_NAME_MAP

# Country mapping for squad page section headers
SQUAD_COUNTRY_MAP = {
    **{k.upper(): v for k, v in TEAM_NAME_MAP.items()},
    "BELGIUM": "BEL", "BULGARIA": "BUL", "GEORGIA": "GEO", "MONTENEGRO": "MNE",
    "SPAIN": "ESP", "TURKEY": "TUR", "BOSNIA AND HERZEGOVINA": "BIH", "FRANCE": "FRA",
    "GERMANY": "GER", "HUNGARY": "HUN", "LITHUANIA": "LTU", "SLOVENIA": "SLO",
    "CROATIA": "CRO", "ESTONIA": "EST", "GREAT BRITAIN": "GBR", "GREECE": "GRE",
    "ITALY": "ITA", "UKRAINE": "UKR", "CZECH REPUBLIC": "CZE", "CZECHIA": "CZE",
    "FINLAND": "FIN", "ISRAEL": "ISR", "NETHERLANDS": "NED", "POLAND": "POL",
    "SERBIA": "SRB", "LATVIA": "LAT", "RUSSIA": "RUS", "SWEDEN": "SWE",
    "PORTUGAL": "POR", "MACEDONIA": "MKD", "NORTH MACEDONIA": "MKD",
    "UNITED STATES": "USA", "USA": "USA", "ARGENTINA": "ARG", "BRAZIL": "BRA",
    "CANADA": "CAN", "AUSTRALIA": "AUS", "NEW ZEALAND": "NZL", "CHINA": "CHN",
    "JAPAN": "JPN", "NIGERIA": "NGR", "SOUTH SUDAN": "SSD", "ANGOLA": "ANG",
    "SENEGAL": "SEN", "TUNISIA": "TUN", "EGYPT": "EGY", "CAPE VERDE": "CPV",
    "IVORY COAST": "CIV", "CÔTE D'IVOIRE": "CIV", "MEXICO": "MEX", "VENEZUELA": "VEN",
    "PUERTO RICO": "PUR", "DOMINICAN REPUBLIC": "DOM", "IRAN": "IRI",
    "JORDAN": "JOR", "LEBANON": "LBN", "SOUTH KOREA": "KOR", "KOREA": "KOR",
    "PHILIPPINES": "PHI", "SERBIA AND MONTENEGRO": "SCG",
}


def clean_player_name(raw_name: str) -> str:
    """Clean player name removing captain (C) markers, notes, and footnote brackets."""
    name = re.sub(r"\(C\)|\(c\)", "", raw_name)
    name = re.sub(r"\[\w+\]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def extract_birth_year(text: str, default_year: int = 1990) -> int:
    """Extract 4-digit birth year from text strings like '(1995-08-16)' or '16 August 1995'."""
    m = re.search(r"\((\d{4})-\d{2}-\d{2}\)", text)
    if m:
        return int(m.group(1))
    m2 = re.search(r"\b(19\d{2}|200\d)\b", text)
    if m2:
        return int(m2.group(1))
    return default_year


def extract_height_cm(text: str) -> Optional[int]:
    """Extract height in centimeters from strings like '2.06 m (6 ft 9 in)' or '206 cm'."""
    m = re.search(r"(\d)\.(\d{2})\s*m", text)
    if m:
        return int(m.group(1)) * 100 + int(m.group(2))
    m2 = re.search(r"(\d{3})\s*cm", text)
    if m2:
        return int(m2.group(1))
    return None


def parse_squad_rosters_page(html_content: str, tournament_id: str) -> List[Dict[str, Any]]:
    """Parse Wikipedia squad roster page extracting 12 players per federation."""
    soup = BeautifulSoup(html_content, "html.parser")
    players = []

    # Iterate over headers or table containers
    tables = soup.find_all("table", {"class": lambda c: c and ("toccolours" in c or "wikitable" in c)})
    if not tables:
        tables = soup.find_all("table")

    for t in tables:
        # Find preceding heading
        prev_h = t.find_previous(["h2", "h3", "h4"])
        if not prev_h:
            continue
        h_text = prev_h.get_text().strip().upper()
        h_text_clean = re.sub(r"\[EDIT\]", "", h_text).strip()

        # Match team country
        country_code = None
        for name_key, code in SQUAD_COUNTRY_MAP.items():
            if name_key in h_text_clean:
                country_code = code
                break

        if not country_code:
            continue

        rows = t.find_all("tr")
        for row in rows:
            tds = row.find_all(["td", "th"])
            if len(tds) < 3:
                continue

            row_text = " ".join(td.get_text().strip() for td in tds)
            if "Pos." in row_text or "Players" in row_text or "Head coach" in row_text:
                continue

            # Look for player name link or cell
            name_cell = None
            pos = "G"
            jersey = 0
            b_year = 1990
            height_cm = 198
            club = "National Team"

            for idx, td in enumerate(tds):
                txt = td.get_text().strip()
                # Position check
                if txt in ["PG", "SG", "SF", "PF", "C", "G", "F", "G/F", "F/C"]:
                    pos = txt
                # Height check
                h_val = extract_height_cm(txt)
                if h_val:
                    height_cm = h_val
                # Birth year check
                by = extract_birth_year(txt, default_year=0)
                if by > 0:
                    b_year = by
                # Name cell (usually contains anchor with title)
                a = td.find("a")
                if a and len(a.get_text().strip()) > 3 and not name_cell:
                    name_cell = a.get_text().strip()
                elif len(txt) > 3 and re.search(r"^[A-Z][a-zA-Z\s\.\-']+$", txt) and not name_cell and txt not in ["Players", "Coaches"]:
                    name_cell = txt

            if not name_cell or len(name_cell) < 3:
                continue

            full_name = clean_player_name(name_cell)
            can_id = generate_player_slug(full_name, b_year)

            players.append({
                "tournament_id": tournament_id,
                "team_id": country_code,
                "canonical_player_id": can_id,
                "full_canonical_name": full_name,
                "birth_year": b_year,
                "primary_position": pos,
                "height_cm": height_cm,
                "club": club,
            })

    # De-duplicate within tournament-team
    seen = set()
    unique_players = []
    for p in players:
        key = (p["tournament_id"], p["team_id"], p["canonical_player_id"])
        if key not in seen:
            seen.add(key)
            unique_players.append(p)

    return unique_players
