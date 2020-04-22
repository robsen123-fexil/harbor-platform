from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str
    database_url: str
    redis_url: str
    jwt_secret: str
    api_port: int


def load_settings() -> Settings:
    return Settings(
        environment=os.getenv("HARBOR_ENV", "development"),
        database_url=os.getenv("HARBOR_DATABASE_URL", "postgresql://harbor:harbor@localhost:5432/harbor"),
        redis_url=os.getenv("HARBOR_REDIS_URL", "redis://localhost:6379/0"),
        jwt_secret=os.getenv("HARBOR_JWT_SECRET", "change-me"),
        api_port=int(os.getenv("HARBOR_API_PORT", "7200")),
    )
