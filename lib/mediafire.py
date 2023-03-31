from requests import *
from bs4 import BeautifulSoup as bs
from hurry.filesize import size, alternative


def Mediafire(url):
	"""
	Mediafire scraper
	"""
	try:
		results = {}
		data = get(url)
		html = bs(data.text, "html.parser")
		link = html.find("a", {"id": "downloadButton"}).get("href")
		filesize = get(link).headers.get("Content-length")
		info = html.find("div", {"class": "dl-info"})
		filetype = html.find("div", {"class": "filetype"}).find("span").text
		results.update({
			"title": html.find("title").text,
			"filetype": filetype,
			"filesize": size(int(filesize), system=alternative),
			"url": link
		})
		return results
	except Exception as e:
		raise e
		
		
def Mediafire2(url):
	"""
	Mediafire scraper
	"""
	try:
		results = {}
		data = get(url)
		html = bs(data.text, "html.parser")
		link = html.find("a", {"id": "downloadButton"})
		info = html.find("div", {"class": "dl-info"})
		results.update({
			"title": html.find("title").text,
			"filesize": link.text,
			"url": link.get("href")
		})
		return results
	except Exception as e:
		raise e