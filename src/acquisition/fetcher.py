"""Data fetcher storing immutable raw payloads with provenance metadata."""

from pathlib import Path
from typing import Optional, Dict, Any, Tuple
import requests
from src.config import RAW_DATA_DIR
from src.acquisition.provenance import create_provenance, RawProvenance
from src.acquisition.rate_limiter import get_limiter


class RawFetcher:
    """Fetcher that caches raw responses immutably to disk with SHA-256 metadata."""

    def __init__(self, raw_dir: Optional[Path] = None, session: Optional[requests.Session] = None):
        self.raw_dir = raw_dir or RAW_DATA_DIR
        self.session = session or requests.Session()
        self.session.headers.update({
            "User-Agent": "SportsAnalyticsResearchBot/1.0 (+https://github.com/sports-analytics-portfolio)"
        })

    def get_raw_storage_path(self, source_id: str, tournament_id: str, resource_name: str, extension: str = "html") -> Path:
        target_dir = self.raw_dir / source_id / tournament_id
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir / f"{resource_name}.{extension}"

    def fetch_and_store(
        self,
        source_id: str,
        tournament_id: str,
        resource_name: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        force_refresh: bool = False,
        extension: str = "html",
    ) -> Tuple[bytes, RawProvenance]:
        """Fetch URL with rate limiting, write payload and provenance JSON to disk."""
        data_path = self.get_raw_storage_path(source_id, tournament_id, resource_name, extension)
        prov_path = data_path.with_suffix(f".{extension}.meta.json")

        if data_path.exists() and prov_path.exists() and not force_refresh:
            content = data_path.read_bytes()
            prov = RawProvenance.model_validate_json(prov_path.read_text(encoding="utf-8"))
            return content, prov

        # Apply rate limiting
        limiter = get_limiter(source_id)
        limiter.wait()

        response = self.session.get(url, params=params, timeout=30)
        content = response.content
        status = response.status_code

        # Write immutable raw payload
        data_path.write_bytes(content)

        # Write provenance metadata
        prov = create_provenance(
            source_id=source_id,
            source_url=url,
            content=content,
            parser_version="1.0.0",
            http_status=status,
            request_params=params,
        )
        prov_path.write_text(prov.model_dump_json(indent=2), encoding="utf-8")

        return content, prov
