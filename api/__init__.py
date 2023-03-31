from fastapi import APIRouter
from .endpoints import instagram
from .endpoints import itch
from .endpoints import kazelyrics
from .endpoints import kusonime
from .endpoints import mediafire
from .endpoints import otakudesu
from .endpoints import textpro
from .endpoints import tinyurl
from .endpoints import youtube

ROUTER = APIRouter(
    prefix="/api",
    tags=["REST API"]
)

ROUTER.include_router(instagram.ROUTER)
ROUTER.include_router(itch.ROUTER)
ROUTER.include_router(kazelyrics.ROUTER)
ROUTER.include_router(kusonime.ROUTER)
ROUTER.include_router(mediafire.ROUTER)
ROUTER.include_router(otakudesu.ROUTER)
ROUTER.include_router(textpro.ROUTER)
ROUTER.include_router(tinyurl.ROUTER)
ROUTER.include_router(youtube.ROUTER)