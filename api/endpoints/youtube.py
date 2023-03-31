import re
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pytube import YouTube
from hurry.filesize import size, alternative

from api.models.youtube_schema import YouTubeSchema

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
	"/youtube",
	response_model=YouTubeSchema,
	responses={
		**responses,
		200: {
			"description": "Successfully response",
			"content": {
				"application/json": {
					"example": {
						"author": "Sandy Sayang Gawr Gura",
						"status": 200,
						"title": "[ORIGINAL ANIMATION] Gawr Gura - Shark'd 🦈 #GawrGura",
						"description": "#GawrGura #Gura3DLive\nhttps://twitter.com/gawrgura\n\n🦈 Gawr Gura 3D Live\nhttps://youtu.be/5-hwTE_O8WY\n\n🦈 Animation By:\nTonari Animation\nhttps://twitter.com/tonarianimation\nhttps://tonarianimation.com/\n\n🦈 Music By:\nFarhan Sarasin\nhttps://twitter.com/FaaatSaw\nhttps://www.farhansarasin.com/\n\n🦈 SFX/Voice Direction By:\nKickback Sound Design",
						"thumbnail": "https://i.ytimg.com/vi/kJGsWORSg-4/sddefault.jpg?v=632678f2",
						"audio": {
							"url": "https://rr2---sn-2utxuvt5-jb3e.googlevideo.com/videoplayback?expire=1666884033&ei=YU1aY_njB9GevwS7mImQAg&ip=103.208.205.174&id=o-AMqG_VEZ2yruZ_aF09c2P4ua-VW9PdC_-S-URclC6okP&itag=140&source=youtube&requiressl=yes&mh=h6&mm=31%2C29&mn=sn-2utxuvt5-jb3e%2Csn-npoe7nds&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=641250&vprv=1&mime=audio%2Fmp4&gir=yes&clen=3545864&dur=219.057&lmt=1663493635488507&mt=1666861978&fvip=4&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOwYe4mnzUSQdrc2v8b5nnVQ3jDTUH9d4agOZ5JmgytmAiEAwGkOurrxCkj67qrUqzLrWe4YblOB1rCvOp_pwkxlLI4%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgAR2yrQ7d_WxHrt0BnOqVR0qmjo0P_3H5GcEBJEwNI98CIH464MqjYfpzfPhp-3etGtAV5KOB7mFRQknDMTWwvBku",
							"size": "3 MB",
							"mimeType": 'audio/mp4; codecs="mp4a.40.2"',
						},
						"video": {
							"url": "https://rr2---sn-2utxuvt5-jb3e.googlevideo.com/videoplayback?expire=1666884033&ei=YU1aY_njB9GevwS7mImQAg&ip=103.208.205.174&id=o-AMqG_VEZ2yruZ_aF09c2P4ua-VW9PdC_-S-URclC6okP&itag=22&source=youtube&requiressl=yes&mh=h6&mm=31%2C29&mn=sn-2utxuvt5-jb3e%2Csn-npoe7nds&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=641250&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=219.057&lmt=1663496015815166&mt=1666861978&fvip=4&fexp=24001373%2C24007246&c=ANDROID&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAJt9xGAb93xSGP9fBWKeBcfrRjbUTwrSA5ddcYWzmP-FAiBwvT95MZ7kHwPNrToKsLsAPRDpIuumjAA2s5fLBENUgQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgAR2yrQ7d_WxHrt0BnOqVR0qmjo0P_3H5GcEBJEwNI98CIH464MqjYfpzfPhp-3etGtAV5KOB7mFRQknDMTWwvBku",
							"size": "10 MB",
							"mimeType": 'video/mp4; codecs="avc1.64001F, mp4a.40.2"',
						},
					}
				}
			},
		},
	},
	summary="YouTube Downloader",
)	
async def youtube(url: Optional[str] = Query(None)):
	"""
	Download video and audio from YouTube
	"""
	if not re.search(r"http[s]\:\/\/", url):
		return JSONResponse(
			status_code=406,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 406, "message": "Invalid URL"}
			),
		)
	data = YouTube(url)
	if data:
		raw = data.vid_info
		stream = data.streaming_data
		resAudio = stream["adaptiveFormats"]
		resAudio = [a for a in resAudio if a["itag"] == 140][0]
		resVideo = stream["formats"]
		resVideo = [b for b in resVideo if b["itag"] == 22][0]
		results = {
			"author": AUTHOR,
			"status": 200,
			"title": data.title,
			"description": data.description,
			"thumbnail": data.thumbnail_url,
			"audio": {
				"url": resAudio["url"],
				"size": size(
					data.streams.get_by_itag(140).filesize, system=alternative
				),
				"mimeType": resAudio["mimeType"],
			},
			"video": {
				"url": resVideo["url"],
				"size": size(data.streams.get_by_itag(22).filesize, system=alternative),
				"mimeType": resVideo["mimeType"],
			},
		}
		return JSONResponse(status_code=200, content=jsonable_encoder(results))
	else:
		return JSONResponse(
			status_code=404,
			content=jsonable_encoder(
				{"author": AUTHOR, "status": 404, "message": "Not found!"}
			),
		)
