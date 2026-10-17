"""Start the service: python -m hello_api."""

from __future__ import annotations

import uvicorn

from hello_api import logs
from hello_api.app import create_app
from hello_api.config import Settings


def main() -> None:
    settings = Settings.from_env()
    logs.configure(settings.log_level)
    uvicorn.run(
        create_app(settings),
        host=settings.host,
        port=settings.port,
        log_config=None,  # keep the JSON handler from logs.configure
        log_level=settings.log_level,
        proxy_headers=True,
    )


if __name__ == "__main__":
    main()
