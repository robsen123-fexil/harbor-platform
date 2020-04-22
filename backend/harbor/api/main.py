from __future__ import annotations

import uvicorn

from harbor.core.config import load_settings


def run() -> None:
    settings = load_settings()
    uvicorn.run("harbor.api.app:app", host="0.0.0.0", port=settings.api_port, reload=False)


if __name__ == "__main__":
    run()
