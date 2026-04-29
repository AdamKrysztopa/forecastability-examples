"""Print paths of notebooks that have no code-cell outputs yet.

Used by CI to avoid re-executing notebooks already committed with outputs.
Prints one path per line to stdout; exits 0 even when the list is empty.

Usage:
    python scripts/find_unexecuted_notebooks.py [dir ...]

Defaults to: walkthroughs triage_walkthroughs recipes
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def has_outputs(nb_path: Path) -> bool:
    """Return True if any code cell in the notebook has outputs or was executed."""
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs") or cell.get("execution_count") is not None:
            return True
    return False


def main() -> None:
    roots = sys.argv[1:] or ["walkthroughs", "triage_walkthroughs", "recipes"]
    for root in roots:
        for nb in sorted(Path(root).rglob("*.ipynb")):
            if not has_outputs(nb):
                print(nb)


if __name__ == "__main__":
    main()
