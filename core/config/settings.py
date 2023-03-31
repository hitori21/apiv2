from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.config.handler import APP

from api import ROUTER
from core import ROOT

ORIGINS = ["https://localhost:8000"]

APP.add_middleware(
	CORSMiddleware,
	allow_origins=ORIGINS,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

APP.mount("/static", StaticFiles(directory="static"), name="static")
APP.mount("/tmp", StaticFiles(directory="tmp"), name="tmp")

APP.include_router(ROOT)
APP.include_router(ROUTER)