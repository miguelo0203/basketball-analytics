"""Domain enumerations for classification, validation, and epistemology."""

from enum import Enum


class Epistemology(str, Enum):
    """Epistemological classification of metric origin."""
    OBSERVED = "OBSERVED"
    ESTIMATED = "ESTIMATED"
    DERIVED = "DERIVED"
    MODELED = "MODELED"


class ValidationSeverity(str, Enum):
    """Severity levels for data quality issues."""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class ValidationStatus(str, Enum):
    """Promotion status of an entity record."""
    VALIDATED = "VALIDATED"
    WARNING = "WARNING"
    QUARANTINED = "QUARANTINED"


class IdentityConfidence(str, Enum):
    """Confidence level of player entity resolution."""
    EXACT = "EXACT"
    DETERMINISTIC = "DETERMINISTIC"
    MANUAL = "MANUAL"
    PROBABILISTIC = "PROBABILISTIC"
    UNRESOLVED = "UNRESOLVED"


class PossessionMethod(str, Enum):
    """Method used to calculate or estimate game possessions."""
    EST_SIMPLE = "EST_SIMPLE"
    EST_BILATERAL = "EST_BILATERAL"
    PBP_EXACT = "PBP_EXACT"
    UNAVAILABLE = "UNAVAILABLE"


class CompetitionType(str, Enum):
    """Competition category."""
    EUROBASKET = "FIBA EuroBasket"
    WORLD_CUP = "FIBA World Cup"
    OLYMPICS = "Olympic Games"
