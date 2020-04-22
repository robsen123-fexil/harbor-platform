from __future__ import annotations

from fastapi import FastAPI

from harbor.core.config import load_settings
from harbor.core.logging import configure_logging, get_logger
from harbor.core.middleware import request_timer
from harbor.api.routes.health import router as health_router
from harbor.api.routes.registry import include_domain_routers


def create_app() -> FastAPI:
    settings = load_settings()
    configure_logging()
    logger = get_logger("harbor.api")
    app = FastAPI(title="Harbor API", version="1.0.0")
    app.middleware("http")(request_timer)
    app.include_router(health_router)
    include_domain_routers(app)
    logger.info("Harbor API ready env=%s port=%s", settings.environment, settings.api_port)
    return app


app = create_app()
