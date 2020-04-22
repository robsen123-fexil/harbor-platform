from __future__ import annotations

import time
from typing import Callable

from fastapi import Request, Response


async def request_timer(request: Request, call_next: Callable) -> Response:
    started = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time-Ms"] = f"{(time.perf_counter() - started) * 1000:.2f}"
    return response
