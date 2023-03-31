from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

ROUTER = APIRouter()

TEMPLATES = Jinja2Templates(directory="public")


@ROUTER.get("/", response_class=HTMLResponse, summary="Home page", status_code=200)
async def root(request: Request):
	"""
	Return the main page of this web
	"""
	return TEMPLATES.TemplateResponse("main/index.html", {"request": request})


@ROUTER.get(
	"/about", response_class=HTMLResponse, summary="About page", status_code=200
)
async def about(request: Request):
	"""
	About me
	"""
	return TEMPLATES.TemplateResponse("main/about.html", {"request": request})
