from fastapi import FastAPI, Response, status
from fastapi.templating import Jinja2Templates

TITLE = "Sebuah REST API"
VERSION = "0.0.1"
DESCRIPTION = "Kontradiksi"

APP = FastAPI(
	title=TITLE, version=VERSION, description=DESCRIPTION, openapi_url="/openapi.json"
)

TEMPLATES = Jinja2Templates(directory="public")


@APP.exception_handler(404)
async def handler_404(request, response: Response):
	response.status_code = status.HTTP_404_NOT_FOUND
	return TEMPLATES.TemplateResponse(
		"handler.html",
		{
			"request": request,
			"Title": "404 Not Found",
			"Code": "404",
			"Message": "Not Found",
		},
	)


@APP.exception_handler(405)
async def handler_405(request, response: Response):
	response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED
	return TEMPLATES.TemplateResponse(
		"handler.html",
		{
			"request": request,
			"Title": "405 Method Not Allowed",
			"Code": "405",
			"Message": "Method Not Allowed",
		},
	)


@APP.exception_handler(422)
async def handler_422(request, response: Response):
	response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
	return TEMPLATES.TemplateResponse(
		"handler.html",
		{
			"request": request,
			"Title": "422 Unprocessable Entity",
			"Code": "422",
			"Message": "Unprocessable Entity",
		},
	)


@APP.exception_handler(500)
async def handler_500(request, response: Response):
	response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
	return TEMPLATES.TemplateResponse(
		"handler.html",
		{
			"request": request,
			"Title": "500 Internal Server Error",
			"Code": "500",
			"Message": "Internal Server Error",
		},
	)
