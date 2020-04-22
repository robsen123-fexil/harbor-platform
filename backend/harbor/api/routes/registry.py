from __future__ import annotations

from fastapi import FastAPI

from harbor.domains import ROUTERS


def include_domain_routers(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)
