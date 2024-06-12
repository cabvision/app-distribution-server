from fastapi import FastAPI

from app_distribution_server.config import (
    APP_TITLE,
    APP_VERSION,
)
from app_distribution_server.router import router

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    summary="Simple, self-hosted IPA & APK app distribution server.",
    description="[Source code, issues and documentation](https://github.com/cabvision/app-distribution-server)",
)


app.include_router(router)
