from __future__ import annotations
from pydantic import BaseModel, validator, root_validator
from typing import Optional

class ApplicantRecord(BaseModel):
    applicant_id: str
    age: Optional[int]
    income: Optional[float]
    loan_amount: Optional[float]
    loan_term_months: Optional[int]
    employment_years: Optional[float]
    credit_score: Optional[int]
    existing_debt: Optional[float]
    defaulted: Optional[int]

    @validator("age")
    def age_range(cls, v):  # noqa: D401
        if v is not None and not (18 <= v <= 100):
            raise ValueError("age out of range")
        return v

    @validator("credit_score")
    def credit_score_range(cls, v):
        if v is not None and not (300 <= v <= 900):
            raise ValueError("credit_score out of range")
        return v

    @root_validator
    def logical_checks(cls, values):
        income, loan_amount = values.get("income"), values.get("loan_amount")
        if income is not None and loan_amount is not None:
            if loan_amount > 50 * income:
                raise ValueError("loan_amount unrealistically high vs income")
        return values
