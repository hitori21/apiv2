from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class TextproSchema(BaseModel):
	author: str
	status: int
	title: str
	url: HttpUrl

	class Config:
		schema_extra = {
			"example": {
				"author": "Sandy Sayang Gawr Gura",
				"status": 200,
				"title": "Create scary halloween text effects online",
				"url": "https://textpro.me/images/user_image/2022/10/635a4c2040b58.jpg",
			}
		}
