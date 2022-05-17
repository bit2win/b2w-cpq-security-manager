from fastapi import FastAPI
from .routers import (
    security_route,
)
from .labels import APP_TITLE, APP_VERSION, APP_DESC
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESC,
    version=APP_VERSION,
)
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    security_route.router,
    tags=["security"],
)
