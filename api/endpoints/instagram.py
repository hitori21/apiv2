import re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

from lib.instagram import Instagram
from api.models.instagram_schema import (
	InstagramReelSchema,
	InstagramIGTVSchema,
	InstagramPhotoSchema,
)

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
					"message": "URL not found!",
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
	"/instareel",
	response_model=InstagramReelSchema,
	responses={
		**responses,
		200: {
			"description": "Successfully response",
			"content": {
				"application/json": {
					"example": {
						"author": AUTHOR,
						"status": 200,
						"url": "https://scontent.cdninstagram.com/v/t50.2886-16/10000000_453210176760423_5982953937762759260_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=103&_nc_ohc=2_3AnXipa_YAX9oSA8w&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfCUh-bdc48iRjZ2sgjoVlecUz35JzbHlqwjDnKxbrdYNA&oe=635DA81D&_nc_sid=78c662",
					}
				}
			},
		},
	},
	summary="Reel Instagram API",
)
async def reel(url: Optional[str] = Query(None)):
	"""
	Create downloadable URL from reel Instagram
	"""
	if not re.search(r"http[s]\:\/\/", url):
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid URL"}
			),
		)
	data = Instagram.Reel(url)
	if data:
		return JSONResponse(
			status_code=200,
			content=jsonable_encoder({"author": AUTHOR, "status": 200, **data}),
		)
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)


@ROUTER.get(
	"/igtv",
	response_model=InstagramIGTVSchema,
	responses={
		**responses,
		200: {
			"description": "Successfully response",
			"content": {
				"application/json": {
					"example": {
						"author": AUTHOR,
						"status": 200,
						"url": "https://scontent.cdninstagram.com/v/t50.2886-16/254349781_577407653567462_428437404955935907_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjcyMC5mZWVkLmRlZmF1bHQiLCJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_ohc=5AOKxtLZLgAAX_iNUVY&edm=AJBgZrYBAAAA&vs=17940535984634658_4034568477&_nc_vs=HBksFQAYJEdOVVJLUS1tMnhReUpnMENBS09FNDhLTUhmSUZia1lMQUFBRhUAAsgBABUAGCRHSjhLS1E4TTR6VnJOQUlCQVBNNzNMcDFibzBUYmtZTEFBQUYVAgLIAQAoABgAGwAVAAAm4I%2Bpgcau6j8VAigCQzMsF0BNTMzMzMzNGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXqBwA%3D&_nc_rid=697008c3da&ccb=7-5&oh=00_AfBOAumX6tE9h4849UdPCRz3lDgZBDkWoDDUK9chhWRnaQ&oe=635D528F&_nc_sid=78c662",
					}
				}
			},
		},
	},
	summary="Instagram TV API",
)
async def igtv(url: Optional[str] = Query(None)):
	"""
	Create downloadable URL from IGTV
	"""
	if not re.search(r"http[s]\:\/\/", url):
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid URL"}
			),
		)
	data = Instagram.IGTV(url)
	if data:
		return JSONResponse(
			status_code=200,
			content=jsonable_encoder({"author": AUTHOR, "status": 200, **data}),
		)
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)


@ROUTER.get(
	"/instaphoto",
	response_model=InstagramPhotoSchema,
	responses={
		**responses,
		200: {
			"description": "Successfully response",
			"content": {
				"application/json": {
					"example": {
						"author": AUTHOR,
						"status": 200,
						"results": [
							{
								"url": "https://scontent.cdninstagram.com/v/t51.2885-15/312504842_773624213718727_474125086103595899_n.webp?stp=dst-jpg_e35&_nc_ht=scontent.cdninstagram.com&_nc_cat=107&_nc_ohc=7MNAe7WAFzcAX96EHfd&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfANQmLeMaGTRogoqix27yrNcbXka1Y6AIb_nnQbI5RsJA&oe=635FD411&_nc_sid=78c662&dl=1"
							},
							{
								"url": "https://scontent.cdninstagram.com/v/t51.2885-15/312364417_615321637048978_7160478317032015470_n.webp?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=110&_nc_ohc=m5GLTcRVcVsAX_UilJx&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfCwpThlsd5nkyVToa_Gj0Aa8HaxOi_iUSfi6L3KXYSogw&oe=63610AD6&_nc_sid=78c662&dl=1"
							},
							{
								"url": "https://scontent.cdninstagram.com/v/t51.2885-15/312414152_861201608647623_7439049099926950951_n.webp?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=103&_nc_ohc=IcHiqaxw0n0AX9g28ki&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfD49GjYnwiku3ImLlzTImtZOiSq6SdBAetIwljKI8ckEw&oe=63607E7F&_nc_sid=78c662&dl=1"
							},
							{
								"url": "https://scontent.cdninstagram.com/v/t51.2885-15/312827330_984605419163369_6622295413242724571_n.webp?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=GO-5WB0-YLwAX-mFW_h&edm=AJBgZrYBAAAA&ccb=7-5&oh=00_AfAuW58NhNPH3lFXTZVLx-UxkovElmBkyk3xWXw6A_ceOg&oe=6360E328&_nc_sid=78c662&dl=1"
							},
						],
					}
				}
			},
		},
	},
	summary="Instagram photos API",
)
async def photo(url: Optional[str] = Query(None)):
	"""
	Create downloadable URL from Instagram photo
	"""
	if not re.search(r"http[s]\:\/\/", url):
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid URL"}
			),
		)
	data = Instagram.Photo(url)
	if data:
		return JSONResponse(
			status_code=200,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 200, "results": data}
			),
		)
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)
