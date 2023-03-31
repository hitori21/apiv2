from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class KusonimeDownloadSchema(BaseModel):
	sd: list[HttpUrl]
	hd: list[HttpUrl]


class KusonimeInfoSchema(BaseModel):
	japanese: str
	genres: str
	seasons: str
	producers: str
	types: str
	status: str
	total_episodes: str
	scores: str
	duration: str
	released_on: str


class KusonimeResultsSchema(BaseModel):
	title: str
	url: HttpUrl
	description: str
	info: KusonimeInfoSchema
	download: KusonimeDownloadSchema
		

class KusonimeSchema(BaseModel):
	author: str
	status: int
	results: list[KusonimeResultsSchema]

	class Config:
		schema_extra = {
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
