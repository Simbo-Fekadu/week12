from finance_capstone.data.validation import validate_records
import pytest


def test_validate_records_success():
    sample = [{
        "applicant_id": "A1",
        "age": 30,
        "income": 4000.0,
        "loan_amount": 8000.0,
        "loan_term_months": 36,
        "employment_years": 3,
        "credit_score": 650,
        "existing_debt": 1500.0,
        "defaulted": 0,
    }]
    validated = validate_records(sample)
    assert len(validated) == 1
    assert validated[0].applicant_id == "A1"


def test_validate_records_failure():
    bad = [{
        "applicant_id": "A2",
        "age": 10,  # invalid age
    }]
    with pytest.raises(Exception):
        validate_records(bad)
