"""Domain router registry."""

from typing import List

from fastapi import APIRouter

ROUTERS: List[APIRouter] = []


def register(router: APIRouter) -> None:
    ROUTERS.append(router)

from harbor.domains._registry import *  # noqa: F401,F403
