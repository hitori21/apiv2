from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"

	
class MediafireSchema(BaseModel):
	author: str
	status: int
	title: str
	filetype: str
	filesize: str
	url: HttpUrl

	class Config:
		schema_extra = {
			"example": {
				"author": AUTHOR, 
				"status": 200, 
				"title": "MediaFire - Getting Started",
				"filetype": "PDF",
				"filesize": "372 KB",
				"url": "https://download2388.mediafire.com/oc4r1hff0qog/hr89y25syeuwr79/MediaFire+-+Getting+Started.pdf"
			}
		}
