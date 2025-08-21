from __future__ import annotations
from typing import Iterable, List
from pydantic import ValidationError
from .schemas import ApplicantRecord


def validate_records(records: Iterable[dict]) -> List[ApplicantRecord]:
    """Validate raw applicant dicts into strongly typed records.

    Raises ValidationError aggregate if any record invalid.
    """
    validated = []
    errors = []
    for i, r in enumerate(records):
        try:
            validated.append(ApplicantRecord(**r))
        except ValidationError as e:  # collect but continue
            errors.append({"index": i, "errors": e.errors()})
    if errors:
        # Optionally could raise custom exception; for now raise standard error with context
        raise ValidationError(errors, ApplicantRecord)  # type: ignore[arg-type]
    return validated
