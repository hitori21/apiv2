import re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

from lib.kusonime import Kusonime
from api.models.kusonime_schema import KusonimeSchema

AUTHOR = "Sandy Sayang Gawr Gura"

ROUTER = APIRouter()

responses = {
	404: {
		"description": "Not found!",
		"content": {
			"application/json": {
				"example": {"author": AUTHOR, "status": 404, "message": "Not found!"}
			}
		},
	},
	406: {
		"description": "Invalid query!",
		"content": {
			"application/json": {
				"example": {
					"author": AUTHOR,
					"status": 406,
					"message": "Invalid query!",
				}
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
	"/kusonime",
	response_model=KusonimeSchema,
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
								"title": "Lycoris Recoil Batch Subtitle Indonesia | Kusonime",
								"url": "https://kusonime.com/lycoris-recoil-subtitle-indonesia-1/",
								"description": "Lycoris Recoil Kafe Jepang “Riko Riko” di Tokyo menyajikan kopi yang nikmat. Punya masalah atau lagi mencemaskan sesuatu? datang ke kafe ini, pelayan kami insya’allah akan membantu menyelesaikan masalahmu. Gadis-gadis unik pelayan kafe siap menyambut kedatanganmu.",
								"info": {
									"japanese": "リコリス・リコイル",
									"genres": "Action, Slice of Life",
									"seasons": "Summer 2022",
									"producers": "Aniplex, BS11, ABC Animation",
									"type": "TV Series",
									"status": "Completed",
									"total_episodes": "13",
									"scores": "8.37",
									"duration": "23 min. per ep.",
									"released_on": "Jul 02, 2022",
								},
								"download": {
									"sd": [
										"https://acefile.co/f/84459078/kusonime-jhon-wick-kw-480pv2-rar",
										"https://drive.google.com/uc?export=download&id=1Nd3YjKIJjKp_FDbeJNyUyMmfMROA8kuO",
										"https://lbx.to/f/Z72zdFf",
										"https://hxfile.co/lh8p788fhdig",
										"https://mega.nz/file/yvYklKhS#1Mht7WlSCpP1u8znwEAj5_SVbZ-8WMLfKbLtqoon5Gc",
										"https://uptobox.com/p32vf6aav86r",
									],
									"hd": [
										"https://acefile.co/f/84459081/kusonime-jhon-wick-kw-720pv2-rar",
										"https://drive.google.com/uc?export=download&id=1LXq98aX9PV8_TPvug5Jx8gVByK-OSAT0",
										"https://lbx.to/f/EuNT2PM",
										"https://hxfile.co/nudf7pgmeomp",
										"https://mega.nz/file/emhDCLgD#2olf3ay__bXBXD2u82SrrHLgRe71yx4E6offd51fWM8",
										"https://uptobox.com/ba381xxl0drg",
									],
								},
							}
						],
					}
				}
			},
		},
	},
	summary="Kusonime scraper",
)	
async def kusonime(query: Optional[str] = Query(None)):
	"""
	Scraping anime data based Kusonime include download url
	"""
	if not query:
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid query"}
			),
		)
	if Kusonime(query):
		results = Kusonime(query)
		return JSONResponse(
			status_code=200,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 200, "results": results}
			),
		)
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)
