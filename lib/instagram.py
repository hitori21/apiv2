import requests
from bs4 import BeautifulSoup as bs


class Instagram:
	"""
	All Instagram scaper tools
	"""
	
	def Reel(url) -> dict:
		results = {}
		payload = {"url": url}
		try:
			data = requests.post("https://downloadgram.org/reel-downloader.php#downloadhere", data=payload)
			html = bs(data.text, "html.parser")
			video = html.find("video")
			if not video:
				pass
			else:
				source = video.find("source").get("src")
				results.update({"url": source})
			return results
		except Exception as e:
			raise e
			
	def Story(url) -> dict:
		results = []
		payload = {"url": url}
		try:
			data = requests.post("https://downloadgram.org/story-downloader.php#downloadhere", data=payload)
			html = bs(data.text, "html.parser")
			downloadhere = html.find("div", {"id": "downloadhere"})
			if not downloadhere:
				pass
			else:
				dlsection = downloadhere.find_all("a")
				for href in dlsection:
					results.append({"url": href.get("href")})
			return results
		except Exception as e:
			raise e
			
	def Photo(url) -> dict:
		results = []
		payload = {"url": url}
		try:
			data = requests.post("https://downloadgram.org/photo-downloader.php#downloadhere", data=payload)
			html = bs(data.text, "html.parser")
			downloadhere = html.find("div", {"id": "downloadhere"})
			if not downloadhere:
				pass
			else:
				dlsection = downloadhere.find_all("a")
				for href in dlsection:
					results.append({"url": href.get("href")})
			return results
		except Exception as e:
			raise e
			
	def IGTV(url) -> dict:
		results = {}
		payload = {"url": url}
		try:
			data = requests.post("https://downloadgram.org/igtv-downloader.php#downloadhere", data=payload)
			html = bs(data.text, "html.parser")
			video = html.find("video")
			if not video:
				pass
			else:
				source = video.find("source").get("src")
				results.update({"url": source})
			return results
		except Exception as e:
			raise e
			