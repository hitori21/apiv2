import requests
from bs4 import BeautifulSoup as bs


def Itch(query) -> dict:
	"""
	Itch.io scraper
	"""
	try:
		results = []
		params = {"q": query}
		data = requests.get("https://itch.io/search", params=params)
		html = bs(data.text, "html.parser")
		game_grid = html.find("div", {"class": "game_grid_widget"})
		game_cell = game_grid.find_all("div", {"class": "game_cell"})
		for game in game_cell:
			title = game.find("div", {"class": "game_title"}).text
			thumbnail = game.find("img").get("data-lazy_src")
			url = game.find("a", {"class": "game_link"}).get("href")
			author = game.find("div", {"class": "game_author"}).find("a").get("href")
			genre = game.find("div", {"class": "game_genre"})
			text = game.find("div", {"class": "game_text"})
			if not genre:
				genre = "N/A"
			else:
				genre = genre.text
			if not text:
				text = "N/A"
			else:
				text = text.text
			results.append(
				{
					"id": int(game.get("data-game_id")),
					"title": title,
					"thumbnail": thumbnail,
					"url": url,
					"author": author,
					"genre": genre,
					"caption": text,
				}
			)
		return results
	except Exception as e:
		raise e
