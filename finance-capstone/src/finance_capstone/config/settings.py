from __future__ import annotations
import os
from pydantic import BaseSettings, Field
from functools import lru_cache

class Settings(BaseSettings):
    """Central application settings.

    Values can be overridden via environment variables.
    """
    ENV: str = Field("local", description="Runtime environment tag")
    RANDOM_SEED: int = 42
    DATA_DIR: str = "data/raw"
    ARTIFACT_DIR: str = "artifacts"
    MODEL_NAME: str = "credit_risk_model"

    class Config:
        case_sensitive = False
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
