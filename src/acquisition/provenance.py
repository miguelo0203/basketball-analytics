"""Data provenance and metadata management for raw payload immutability."""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from pydantic import BaseModel, ConfigDict


class RawProvenance(BaseModel):
    """Metadata attached to every immutable raw payload."""
    model_config = ConfigDict(frozen=True)

    source_id: str
    source_url: str
    retrieval_timestamp_utc: str
    content_sha256: str
    parser_version: str
    ingestion_run_id: str
    http_status: int = 200
    request_params: Optional[Dict[str, Any]] = None


def compute_sha256(content: bytes) -> str:
    """Compute SHA-256 hexadecimal hash of bytes content."""
    return hashlib.sha256(content).hexdigest()


def create_provenance(
    source_id: str,
    source_url: str,
    content: bytes,
    parser_version: str = "1.0.0",
    http_status: int = 200,
    request_params: Optional[Dict[str, Any]] = None,
    ingestion_run_id: Optional[str] = None,
) -> RawProvenance:
    """Generate immutable provenance record for fetched payload."""
    return RawProvenance(
        source_id=source_id,
        source_url=source_url,
        retrieval_timestamp_utc=datetime.now(timezone.utc).isoformat(),
        content_sha256=compute_sha256(content),
        parser_version=parser_version,
        ingestion_run_id=ingestion_run_id or str(uuid.uuid4()),
        http_status=http_status,
        request_params=request_params,
    )
