from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

ROUTER = APIRouter(prefix="/tools")

TEMPLATES = Jinja2Templates(directory="public")

def Clear():
	import os, shutil
	from pathlib import Path
	
	
	PATH = Path(__file__).parent.parent.parent
	os.chdir(Path(PATH, "tmp"))
	shutil.rmtree("insta")
	os.mkdir("insta")
	os.chdir("insta")
	open("log.txt", "w").write("Lorem ipsum dolor sit amet")
	os.chdir(PATH)


@ROUTER.get("/", response_class=HTMLResponse, summary="Tools page", status_code=200)
async def root(request: Request):
	"""
	Return the main page of this web
	"""
	return TEMPLATES.TemplateResponse("tools/index.html", {"request": request})


@ROUTER.get(
	"/youtube",
	response_class=HTMLResponse,
	summary="Tools YouTube page",
	status_code=200,
)
async def youtube(request: Request):
	"""
	Return the main page of this web
	"""
	Clear()
	return TEMPLATES.TemplateResponse("tools/youtube.html", {"request": request})
	

@ROUTER.post("/youtube", summary="Tools YouTube page", status_code=200)
async def youtube_res(request: Request, url: str = Form(...)):
	"""
	Return the main page of this web
	"""
	import re, json
	from pytube import YouTube
	from hurry.filesize import size, alternative
	
	regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
	
	def video_id(value):
		match = regex.match(value)
		return match.group('id')

	if not re.search(regex, url):
		return TEMPLATES.TemplateResponse("tools/youtube.html", {"request": request})
	data = YouTube(url)
	try:
		raw = data.vid_info
		stream = data.streaming_data
		resAudio = stream["adaptiveFormats"]
		resAudio = [a for a in resAudio if a["itag"] == 140][0]
		resVideo = stream["formats"]
		resVideo = [b for b in resVideo if b["itag"] == 22][0]
		return TEMPLATES.TemplateResponse(
			"tools/results/youtube.html",
			{
				"request": request,
				"url": url,
				"Title": data.title,
				"Description": data.description,
				"ID": video_id(url),
				"Audio_URL": resAudio["url"],
				"Video_URL": resVideo["url"],
				"Audio_Size": size(
					data.streams.get_by_itag(140).filesize, system=alternative
				),
				"Video_Size": size(
					data.streams.get_by_itag(22).filesize, system=alternative
				),
			},
		)
	except Exception as e:
		return TEMPLATES.TemplateResponse("tools/youtube.html", {"request": request})
	
	
@ROUTER.get(
	"/mediafire",
	response_class=HTMLResponse,
	summary="Tools MediaFire page",
	status_code=200,
)
async def mediafire(request: Request):
	"""
	Return the main page of this web
	"""
	Clear()
	return TEMPLATES.TemplateResponse("tools/mediafire.html", {"request": request})


@ROUTER.post("/mediafire", summary="Tools MediaFire page", status_code=200)
async def mediafire_res(request: Request, url: str = Form(...)):
	"""
	Return the main page of this web
	"""
	import re
	from lib.mediafire import Mediafire2
	
	if not re.search(r"http[s]\:\/\/", url):
		return TEMPLATES.TemplateResponse("tools/mediafire.html", {"request": request})
	data = Mediafire2(url)
	try:
		return TEMPLATES.TemplateResponse(
			"tools/results/mediafire.html",
			{
				"request": request,
				"url": url,
				"Title": data["title"],
				"FileSize": data["filesize"],
				"DownloadUrl": data["url"]
			},
		)
	except Exception as e:
		return TEMPLATES.TemplateResponse("tools/mediafire.html", {"request": request})
	
	
@ROUTER.get(
	"/instagram",
	response_class=HTMLResponse,
	summary="Tools Instagram page",
	status_code=200,
)
async def instagram(request: Request):
	"""
	Return the main page of this web
	"""
	Clear()
	return TEMPLATES.TemplateResponse("tools/instagram.html", {"request": request})


@ROUTER.post("/instagram", summary="Tools Instagram page", status_code=200)
async def instagram_res(request: Request, url: str = Form(...)):
	"""
	Return the main page of this web
	"""
	import re, os
	import requests as r
	from pathlib import Path
	from lib.instagram import Instagram
	
	if not re.search(r"http[s]\:\/\/", url):
		return TEMPLATES.TemplateResponse("tools/instagram.html", {"request": request})
	try:
		if re.search(r"\/reel\/", url):
			reel = Instagram.Reel(url)
			return TEMPLATES.TemplateResponse(
				"tools/results/insta_reel.html",
				{
					"request": request,
					"url": url,
					"src": reel["url"]
				},
			)
		elif re.search(r"\/tv\/", url):
			vid = Instagram.IGTV(url)
			return TEMPLATES.TemplateResponse(
				"tools/results/insta_video.html",
				{
					"request": request,
					"url": url,
					"src": vid["url"]
				},
			)
		elif re.search(r"\/p\/", url):
			title = url.split("p/")[1]
			title = title.split("/")[0]
			photo = Instagram.Photo(url)
			PATH = Path(__file__).parent.parent.parent
			os.chdir(Path(PATH, "tmp/insta"))
			try:
				os.mkdir(title)
			except:
				pass
			os.chdir(title)
			for src in range(len(photo)):
				data = r.get(photo[src]["url"])
				open(f"{title}_{str(src)}.jpg", "wb").write(data.content)
			result = []
			for res in range(len(photo)):
				result.append({"url": f"/tmp/insta/{title}/{title}_{res}.jpg"})
			os.chdir(PATH)
			return TEMPLATES.TemplateResponse(
				"tools/results/insta_photo.html",
				{
					"request": request,
					"url": url,
					"src": result
				},
			)
		else:
			return TEMPLATES.TemplateResponse("tools/instagram.html", {"request": request})
	except Exception as e:
		raise e