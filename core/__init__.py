from fastapi import APIRouter
from .views import index
from .views import tools

ROOT = APIRouter(
	tags=["MAIN"]
)

ROOT.include_router(index.ROUTER)
ROOT.include_router(tools.ROUTER)