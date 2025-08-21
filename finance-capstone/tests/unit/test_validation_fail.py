import pytest
from pydantic import ValidationError
from finance_capstone.data.validation import validate_records

def test_validate_records_failure():
    bad = [{
        "applicant_id": "B1",
        "age": 10,  # invalid age (<18)
        "income": 3000.0,
        "loan_amount": 10000.0,
        "loan_term_months": 24,
        "employment_years": 2,
        "credit_score": 250,  # invalid credit score (<300)
        "existing_debt": 500.0,
        "defaulted": 0,
    }]
    with pytest.raises(ValidationError):
        validate_records(bad)
