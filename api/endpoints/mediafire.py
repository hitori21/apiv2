import re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

from lib.mediafire import Mediafire
from api.models.mediafire_schema import MediafireSchema

AUTHOR = "Sandy Sayang Gawr Gura"

ROUTER = APIRouter()

responses = {
	404: {
		"description": "Not found!",
		"content": {
			"application/json": {
				"example": {
					"author": AUTHOR,
					"status": 404,
					"message": "Not found!",
				}
			}
		},
	},
	406: {
		"description": "Invalid URL!",
		"content": {
			"application/json": {
				"example": {"author": AUTHOR, "status": 406, "message": "Invalid URL!"}
			}
		},
	},
	422: {
		"description": "Unprocessable",
		"content": {
			"application/json": {
				"example": {
					"author": AUTHOR,
					"status": 422,
					"message": "Unprocessable request!",
				}
			}
		},
	},
}
	

@ROUTER.get(
	"/mediafire",
	response_model=MediafireSchema,
	responses={
		**responses,
		200: {
			"description": "Successfully response",
			"content": {
				"application/json": {
					"example": {
						"author": AUTHOR,
						"status": 200,
						"title": "MediaFire - Getting Started",
						"filetype": "PDF",
						"filesize": "372 KB",
						"url": "https://download2388.mediafire.com/oc4r1hff0qog/hr89y25syeuwr79/MediaFire+-+Getting+Started.pdf"
					}
				}
			},
		},
	},
	summary="Mediafire scraper",
)
async def mediafire(url: Optional[str] = Query(None)):
	"""
	Mediafire scraper include downloadable url
	"""
	if not re.search(r"http[s]\:\/\/", url):
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid URL"}
			),
		)
	if Mediafire(url):
		return JSONResponse(
			status_code=200,
			content=jsonable_encoder({"author": AUTHOR, "status": 200, **Mediafire(url)}),
		)
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)
