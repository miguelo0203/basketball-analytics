"""Rule set modeling and retrieval based on explicit tournament configurations."""

import pandas as pd
from typing import Dict, Optional
from pydantic import BaseModel, ConfigDict
from src.config import RULE_SETS_CSV


class RuleSet(BaseModel):
    """Pydantic model for a FIBA regulatory era."""
    model_config = ConfigDict(frozen=True)

    rule_set_id: str
    effective_from: str
    effective_to: str
    rule_3pt_distance_m: float
    shot_clock_seconds: int
    shot_clock_orb_seconds: int
    lane_geometry: str
    no_charge_semicircle: bool
    game_duration_minutes: int
    ot_duration_minutes: int
    description: str


class RuleSetRegistry:
    """Registry managing rulesets loaded from config/rule_sets.csv."""

    def __init__(self, csv_path: Optional[str] = None):
        self._path = csv_path or str(RULE_SETS_CSV)
        self._rulesets: Dict[str, RuleSet] = {}
        self._load()

    def _load(self) -> None:
        df = pd.read_csv(self._path)
        for _, row in df.iterrows():
            item = RuleSet(
                rule_set_id=str(row["rule_set_id"]),
                effective_from=str(row["effective_from"]),
                effective_to=str(row["effective_to"]),
                rule_3pt_distance_m=float(row["rule_3pt_distance_m"]),
                shot_clock_seconds=int(row["shot_clock_seconds"]),
                shot_clock_orb_seconds=int(row["shot_clock_orb_seconds"]),
                lane_geometry=str(row["lane_geometry"]),
                no_charge_semicircle=bool(str(row["no_charge_semicircle"]).lower() == "true"),
                game_duration_minutes=int(row["game_duration_minutes"]),
                ot_duration_minutes=int(row["ot_duration_minutes"]),
                description=str(row["description"]),
            )
            self._rulesets[item.rule_set_id] = item

    def get(self, rule_set_id: str) -> RuleSet:
        if rule_set_id not in self._rulesets:
            raise KeyError(f"Rule set '{rule_set_id}' not found in registry.")
        return self._rulesets[rule_set_id]

    def all(self) -> Dict[str, RuleSet]:
        return self._rulesets
