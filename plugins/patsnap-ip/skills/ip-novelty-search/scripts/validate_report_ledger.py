#!/usr/bin/env python3
"""Validate the candidate-ledger reference used by a novelty report draft."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any


_spec = importlib.util.spec_from_file_location(
    "novelty_candidate_ledger", Path(__file__).with_name("validate_candidate_ledger.py")
)
_validator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_validator)


def validate_candidate_ledger_reference(draft: Any, base: Path) -> None:
    """Require and validate the final ledger when the report contract calls for it."""
    report = draft.get("report") if isinstance(draft, dict) else None
    if not isinstance(report, dict):
        raise ValueError("Report data requires a report object")
    relative = report.get("candidate_ledger_file")
    if not relative:
        if report.get("status") == "complete" and report.get("report_data_version", 1) >= 2:
            raise ValueError("Complete report data version 2 requires candidate_ledger_file")
        return
    base = Path(base).resolve()
    path = (base / relative).resolve()
    if not path.is_relative_to(base):
        raise ValueError("Candidate ledger must be inside the task workspace")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Candidate ledger does not exist: {relative}") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Candidate ledger is not readable JSON: {relative}: {exc}") from exc
    errors = _validator.validate_ledger(data, base, "final")
    if errors:
        raise ValueError("Candidate ledger final validation failed: " + "; ".join(errors))
