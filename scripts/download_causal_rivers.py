"""Download and prepare the CausalRivers East Germany station data.

Fetches the CausalRivers benchmark zip from GitHub, extracts the East Germany
river time-series CSV in-memory, subsets to 8 stations of interest, resamples
to 6-hourly means, and writes:

  data/causal_rivers/east_germany_8stations_6h.parquet  — processed frame
  data/causal_rivers/east_germany_8stations_6h.sha256   — SHA-256 manifest
  data/causal_rivers/.FETCHED                           — CI cache sentinel

Usage:
    uv run python scripts/download_causal_rivers.py
    uv run python scripts/download_causal_rivers.py --data-dir /tmp/cr_test
"""

from __future__ import annotations

import argparse
import hashlib
import io
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_DOWNLOAD_URL = (
    "https://github.com/CausalRivers/benchmark/releases/download/"
    "First_release/product.zip"
)
_ZIP_ENTRY = "product/rivers_ts_east_germany.csv"

# Station IDs to keep
_TARGET_STATION: int = 978
_POSITIVE_STATIONS: list[int] = [979, 1095, 313, 758, 490]
_NEGATIVE_STATIONS: list[int] = [67, 71, 99]
_STATIONS: list[int] = [_TARGET_STATION] + _POSITIVE_STATIONS + _NEGATIVE_STATIONS

_PARQUET_NAME = "east_germany_8stations_6h.parquet"
_SHA256_NAME = "east_germany_8stations_6h.sha256"
_FETCHED_NAME = ".FETCHED"

_PREFIX = "[download_causal_rivers]"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sha256_of_file(path: Path) -> str:
    """Return the hex SHA-256 digest of *path*."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_manifest(sha256_path: Path) -> str | None:
    """Return the hex digest stored in *sha256_path*, or ``None`` if missing/malformed."""
    if not sha256_path.exists():
        return None
    text = sha256_path.read_text().strip()
    # Expected format: "<hexdigest>  <filename>"
    parts = text.split()
    if not parts:
        return None
    return parts[0]


def _already_verified(parquet_path: Path, sha256_path: Path) -> bool:
    """Return ``True`` iff both files exist and the digest matches."""
    if not parquet_path.exists():
        return False
    stored = _read_manifest(sha256_path)
    if stored is None:
        return False
    actual = _sha256_of_file(parquet_path)
    return stored == actual


def _fetch_zip_bytes(url: str) -> bytes:
    """Download *url* and return the raw bytes, or raise ``SystemExit`` on failure."""
    print(f"{_PREFIX} downloading {url}")
    try:
        with urllib.request.urlopen(url, timeout=120) as resp:  # noqa: S310
            data: bytes = resp.read()
    except urllib.error.HTTPError as exc:
        print(f"{_PREFIX} HTTP error {exc.code} fetching {url}: {exc.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"{_PREFIX} network error fetching {url}: {exc.reason}", file=sys.stderr)
        sys.exit(1)
    except TimeoutError:
        print(f"{_PREFIX} timeout fetching {url}", file=sys.stderr)
        sys.exit(1)
    print(f"{_PREFIX} downloaded {len(data):,} bytes")
    return data


def _extract_csv(zip_bytes: bytes, entry: str) -> pd.DataFrame:
    """Extract *entry* from the in-memory zip and parse it as a time-indexed CSV."""
    print(f"{_PREFIX} extracting {entry} from zip")
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        with zf.open(entry) as csv_fh:
            frame = pd.read_csv(csv_fh, parse_dates=True, index_col=0)
    return frame


def _process(frame: pd.DataFrame) -> pd.DataFrame:
    """Subset, resample to 6h, and drop all-NaN rows."""
    print(f"{_PREFIX} casting column names to int")
    frame.columns = [int(c) for c in frame.columns]

    print(f"{_PREFIX} subsetting to 8 stations: {_STATIONS}")
    frame = frame[_STATIONS]

    print(f"{_PREFIX} resampling to 6h means")
    frame = frame.resample("6h").mean()

    before = len(frame)
    frame = frame.dropna(how="all")
    after = len(frame)
    print(f"{_PREFIX} dropped {before - after} all-NaN rows, {after} rows remain")

    return frame


def _write_outputs(frame: pd.DataFrame, data_dir: Path) -> None:
    """Write parquet, SHA-256 manifest, and cache sentinel."""
    parquet_path = data_dir / _PARQUET_NAME
    sha256_path = data_dir / _SHA256_NAME
    fetched_path = data_dir / _FETCHED_NAME

    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"{_PREFIX} writing {parquet_path}")
    frame.to_parquet(parquet_path)

    hexdigest = _sha256_of_file(parquet_path)
    manifest_line = f"{hexdigest}  {_PARQUET_NAME}\n"
    sha256_path.write_text(manifest_line)
    print(f"{_PREFIX} wrote manifest {sha256_path}")

    fetched_path.touch()
    print(f"{_PREFIX} wrote cache sentinel {fetched_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point for the download script."""
    parser = argparse.ArgumentParser(
        description="Fetch and prepare CausalRivers East Germany data."
    )
    parser.add_argument(
        "--data-dir",
        default="data/causal_rivers",
        help="Output directory (default: data/causal_rivers)",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    parquet_path = data_dir / _PARQUET_NAME
    sha256_path = data_dir / _SHA256_NAME

    if _already_verified(parquet_path, sha256_path):
        print(
            f"{_PREFIX} data already present and verified — skipping"
        )
        return

    if parquet_path.exists():
        print(f"{_PREFIX} parquet exists but SHA-256 check failed — re-downloading")

    zip_bytes = _fetch_zip_bytes(_DOWNLOAD_URL)
    frame = _extract_csv(zip_bytes, _ZIP_ENTRY)
    frame = _process(frame)
    _write_outputs(frame, data_dir)

    print(f"{_PREFIX} done")


if __name__ == "__main__":
    main()
