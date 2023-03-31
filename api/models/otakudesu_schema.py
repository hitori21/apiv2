from pydantic import BaseModel, HttpUrl

AUTHOR = "Sandy Sayang Gawr Gura"


class OtakudesuInfoSchema(BaseModel):
	title: str
	japanese: str
	score: str
	producer: str
	types: str
	status: str
	total_episodes: int
	duration: str
	release: str
	studio: str
	genres: str


class OtakudesuDownloadURLSchema(BaseModel):
	name: str
	url: HttpUrl
	size: str


class OtakudesuDownloadSchema(BaseModel):
	sd_360p: list[OtakudesuDownloadURLSchema]
	sd_480p: list[OtakudesuDownloadURLSchema]
	hd_720p: list[OtakudesuDownloadURLSchema]


class OtakudesuEpisodeSchema(BaseModel):
	title: str
	url: HttpUrl
	upload: str
	download: OtakudesuDownloadSchema


class OtakudesuBatchSchema(BaseModel):
	url: HttpUrl
	upload: str
	download: OtakudesuDownloadSchema


class OtakudesuSchema(BaseModel):
	author: str
	status: int
	title: str
	url: HttpUrl
	thumbnail: HttpUrl
	info: OtakudesuInfoSchema
	batch: OtakudesuBatchSchema
	episode: OtakudesuEpisodeSchema
		
	class Config:
		schema_extra = {
			"example": {
				"author": AUTHOR,
				"status": 200,
				"title": "Lycoris Recoil (Episode 1 – 12) Subtitle Indonesia",
				"url": "https://otakudesu.video/anime/lycoris-subtitle-indonesia/",
				"thumbnail": "https://otakudesu.video/wp-content/uploads/2022/09/Lycoris-Recoil-Sub-Indo.jpg",
				"info": {
					"title": "Lycoris Recoil",
					"japanese": "リコリス・リコイル",
					"score": "8.36",
					"producer": "Aniplex",
					"types": "TV",
					"status": "Completed",
					"total_episodes": "13",
					"duration": "23 Menit",
					"release": "Jul 02, 2022",
					"studio": "A-1 Pictures",
					"genres": "Action, Sci-Fi",
				},
				"batch": {
					"url": "https://otakudesu.video/batch/lr-batch-sub-indo/",
					"upload": "26 September,2022",
					"download": {
						"sd_360p": [
							{
								"name": "Racaty",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lXeVVTTUo5KzhYd1I5MlZ3RXp0Rk9QcmpZMFFRQWZBPT0=",
								"size": "0.50 GB",
							},
							{
								"name": "OtakuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYmtNTktKNzZNa2w0ZktZaklqeEd4Wk1vZGJpNFB5Wk1rc3RvRzkrME5UQUwxRkxuYzE5dkhUbFBlZXVQNHFTQ000K1NSVCtHcEk5bUhvLytKREdIRituaWF3cXNrSXdKSkdaM0k5OStEdEE4QnZUV2xyZGtFV0IydE5RMEFDbVFoRHJqZmRZRDFOdz09",
								"size": "0.50 GB",
							},
							{
								"name": "DesuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYndONVBjWitGdW5JemZKYWdnakhnUmJSaFFVOEQxdkk5a2ZwWTh0RUxYQk9JRm9HODgrTHhXbGYzWXUvY3JCbll4SVd5UThQQVhkQ0VvYzZTQTB6eDVtbWloYk1NT2docFpPM3hsYU9WdFRVQXZ6ZWlqOU01VGdhMU9sST0=",
								"size": "0.50 GB",
							},
							{
								"name": "Uptobox",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lSMkZPQ01jbnFId0ptbXhZR21vVk1LL21RMkZzQ0tNTT0=",
								"size": "0.50 GB",
							},
							{
								"name": "Mega",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmkvQmZmdnE2MUdSS0pQQ05xU2J2ZHFsSlVFNVh6ODR5amZsZy9kUUJRUU9nTjUyLy92djFRVldCY1BuY3pSU2U2T09KWHc9PQ==",
								"size": "0.50 GB",
							},
							{
								"name": "Acefile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lGeTBLTE9zcjNId0ptMlY4Yng0TWVlZnJmMHdaR0k5T1dqUURvU29sUktoUUU5Lzhhck9JSGxMWVZHU2FtTUE9PQ==",
								"size": "0.50 GB",
							},
							{
								"name": "Hxfile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRteGtBSHpJWlNlL09CaFU4Wg==",
								"size": "0.50 GB",
							},
							{
								"name": "DesuFiles",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYm05SllPYTJCakZJYVk1aWVna2p2SDZCTlNUOFp4ZnBHalA1UjV1NHhWajZSTW9Mai9OSE9ibXowWTlySmlnRGI5K09HZWVQRFJPKzZ0c0dUSUUzWDgxUzMwNUlIQkJWUGZvcjU3YVRhaWpzT3V5S2QzL0ViWXdtcFVsODNCbW9qTnIvS2MrejE=",
								"size": "0.50 GB",
							},
						],
						"sd_480p": [
							{
								"name": "Racaty",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lXeVVTTUo5KzhYd1I5MlY5ZGtONWZPZktHMGxWWkp3PT0=",
								"size": "0.85 GB",
							},
							{
								"name": "OtakuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYmtNTktKNzZNa2w0ZktZaklqeEd4ZGNwSWJ6Y016dGtWNzgwQTkrMHZjQUdTSnJ2cm85dXNaVUxlWWVDZ3VTMk55N3FlZitLWWZOR1hpZHVXTXhYQyt3R3J4NTAzT3dKN1JJWHM4TG1oNlRZTW16T1N2Tll4VUh1RVF6MFNhVXNwSXFQc1RxYjFOdz09",
								"size": "0.85 GB",
							},
							{
								"name": "DesuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYndONVBjYWkrakY0N0l1MkZzejNkVnJSS1hSc3p5K1lZdXZsMjY4MVhRR1NqTDVid3dyckxNVW54UUlYS3JublovTHVNWGR5ZVFjV2MvN1dzTUhmSDgxUDg0cFVPQXdoUWN1elR6SXpmdlY4T2xoMkJ1T3A4UnlpRE9sST0=",
								"size": "0.85 GB",
							},
							{
								"name": "Uptobox",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lSMkZPQ01jbnFId0ptbXhaUXpjTmRMNktPbUZnSU9zbz0=",
								"size": "0.85 GB",
							},
							{
								"name": "Mega",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnFmUllKTHk4MW54S09wV3dzQ1Q2VEs5d1VFaFN5OVkxdGRrQTk5UURRbTJrSWJqZzVySEVRMUNHYmRMcHRBbSt6cmpjWHc9PQ==",
								"size": "0.85 GB",
							},
							{
								"name": "Acefile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lGeTBLTE9zcjNId0ptMlY4Yng0TWVlZnJmMHdOR0k5T1dqUURvU29sUktoUUU5Lzhhck9JQW1yWVZHU2FtTUE9PQ==",
								"size": "0.85 GB",
							},
							{
								"name": "Hxfile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaGtOUm1ObEVQcnZlMEFOZg==",
								"size": "0.85 GB",
							},
							{
								"name": "DesuFiles",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYm05SllPYTJCakZJYVk1aWVna2p1ZUxSblkwczQ5T3hHaTh0aDJPMVZVQnlkTmJibjRPUEpSR2pGVUlYOGpDM2F3dVNHSCtDSVJlMlhodTJRVjFmZ3kxeisvYjRMTmlJb0dldjI4TmlGakFjLzRDYXpyTllzVENPRVZWMEJKR1k5QzR2SVZlejE=",
								"size": "0.85 GB",
							},
						],
						"hd_720p": [
							{
								"name": "Racaty",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lXeVVTTUo5KzhYd1I5MlV4Tmw4OVRkTE9ZaTF3SWZRPT0=",
								"size": "1.52 GB",
							},
							{
								"name": "OtakuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYmtNTktKNzZNa2w0ZktZaklqeEd4ZUw1eVFDazU2K003dGMxeTlORTNRemUrTnFMY29QSEtXVFRLUTlMcXdpVzVsWmVlWXVLQVpkZVZxTGlSSTJyRy9HUDJ5cThLSFExNFJLK1g2N2pla2pVQnZSK1VyL3N4UnlhYk13MEJIbVFoQ3ByalFwRDFOdz09",
								"size": "1.52 GB",
							},
							{
								"name": "DesuDrive",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYndONVBjWWEvcGs0bkJNKzh0VEs1UXE0VVFSSUZ4UFlIall4Y3c4a3lYeTJTY2JmbjhjN1hVR2YyVU1UQ2xRS1p4YnV1WmV1bFo5cUNpUFMrTWszOTJtT0k1Y3dRT3lJc2ZMVHA4STZWc1JzWTQwR0F1K2dpZmgyMU9sST0=",
								"size": "1.52 GB",
							},
							{
								"name": "Uptobox",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lSMkZPQ01jbnFId0ptbXhaUXh0WmNkZjJabFZNYlA1ND0=",
								"size": "1.52 GB",
							},
							{
								"name": "Mega",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmtORkFmcWFLcW5WS0s5YUJvZ0Q4RzVrWGNSSVIwKzhsa2ZkVzErb01ZaGFZSi83ODJPN2FPR1A3UUk3eWlnK1kxK1dRWlE9PQ==",
								"size": "1.52 GB",
							},
							{
								"name": "Acefile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lGeTBLTE9zcjNId0ptMlY4Yng0TWVlZnJmMHdKR0k5T1dqUURvU29sUktoUUU5Lzhhck9JRGtMWVZHU2FtTUE9PQ==",
								"size": "1.52 GB",
							},
							{
								"name": "Hxfile",
								"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtd2x4V2w5bGRlTHljaFY4YQ==",
								"size": "1.52 GB",
							},
							{
								"name": "DesuFiles",
								"url": "https://desudrive.com/link/?id=eVYzczJkMWJLV2tCMjFLSkljL2tWRTlxbVZRYm05SllPYTJCakZJYVk1aWVna2pZVnNOMVNrZ053ZmN6aDg5NTJNQWRaV2VLT3AzaTVQajVSMkRrYnVEd2lTNnYxdVd4ZE9PWlRlMjloTzJUTUZIazJseUEwNUlUQkNOUEdZZnZsOVNXZ0FZNG5TTEZyTzhFWXhHYlVRTVJiVjBqRkp2SlZlejE=",
								"size": "1.52 GB",
							},
						],
					},
				},
				"episode": [
					{
						"title": "Lycoris Recoil Episode 13 (End) Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-13-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk4V3ZpUzNCV0lsaUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "38.2 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta1FoT25ZRlNJL21QZ3djWg==",
									"size": "38.2 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym1QQVNEcU95MVdOS2V1aWt5d0R0U1lobmRUa1p6TlFkaCtsQnhONEpCUTZ2RDZEKzE4SGJOWDM1WGQzZm5UemZ6b21PWHc9PQ==",
									"size": "38.2 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlkvV1FnRWI1WjhzZEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "65.3 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbFExWm5JQlBmUHFMaWs4Tg==",
									"size": "65.3 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym1QaGxIb09raW01S0dNdTdvUUhKVjZoVGRTQUN5Tk5Cc2M4QXpjY2hlQWF0RG9EbDF1elRUWDNvQVlmd2dRN2Y0SmVpZlE9PQ==",
									"size": "65.3 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvNmIweURxVFpzVktCd0k3OFZZdHNsWnpnPT0=",
									"size": "120.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtamdrR21zMGFLYVNIa2dZZA==",
									"size": "120.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Yms5VklIL3FLczNWS0d0T2lzeS85Y0loN1BqOCs2Y3drc3Z4VjhQWVhmQXYwQWJuUHh1dk9kR0w2WlBmQnpIaXVpNHVuYlE9PQ==",
									"size": "120.0 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 12 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-12-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvVEdyMGJsR294UUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "43.6 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbWxoQnlZUklJS2JhMUFVSQ==",
									"size": "43.6 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnBmUnRmYUc2Z1dOS0FkR1ZnMGZpQXBocE1VaFh4OEVRNnNSYzcvOHBZQ0wwRllmNy9iRFZOMmJvVG83a3Z5Vzd3T2FLZlE9PQ==",
									"size": "43.6 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk4V1BqQWYrVmI5VEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "74.3 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtZ3doV3pkRVpJSzNjaGdRWQ==",
									"size": "74.3 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynh0RnREbzZLa0haS0M4U3ZyeUxWZHBaK1V3OGp0WkVhcnZCaWt2TlZmVzJVZHFXN3BzYjhkRGJGUWZPbnZSMkF4S0dVWlE9PQ==",
									"size": "74.3 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk4VzV0U0hrWXFOZ0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "133.7 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbEF4V25OUkFJYm1FMGtZYQ==",
									"size": "133.7 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynh1UWFINk9LcTI1S0JZcXZna2ZBVGFKdWRSODUxL1FtdSt0NncvSXRReWZ5SzRMeDhlYitaWExVRGZuZ3ZRMmswcVdBV3c9PQ==",
									"size": "133.7 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 11 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-11-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk5N0dvaUx2UjVCc0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "41.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbms1WmxjSWVOS3JSaEZRQw==",
									"size": "41.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynh2c1NCS1dpaDNWS0lkYXVreEhtWXNvV01TVXY4T0V5dFpCbDFxc3hlRG1PTjdXOG9ycnJVelhkZmZYUWpDZUY3NGFvUXc9PQ==",
									"size": "41.0 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlkvNi9wMFg4WWNOMEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "69.7 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaGc5UWxvSVlOTHZaa1UxWQ==",
									"size": "69.7 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnkrQVNHcDZqaW4xS0FNMlpwQlBjYUlvUVkwSVk4Y3NRaXRKUno3UVRVekdKSkxmY3lPN0pRWGZIWk83OXVEWFo4K0NqU3c9PQ==",
									"size": "69.7 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvV3V0Q1R1UTVGR0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "131.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtd3d4Zmp0UklKL1BhZ1VaZg==",
									"size": "131.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnV2UnVJWmloMTJOS0JQN1BpUTM4ZjV0WFlTb1Q1SkFnamVKdDd1UVVBQUNYRnB6czMvQ3RhakRnQk03aG5SeTg0ZUt6RkE9PQ==",
									"size": "131.0 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 10 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-10-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk1T1VyaCs2UXI1bUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "34.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtZ0F0T2hkUWVLSzdZMTBFYQ==",
									"size": "34.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym05VWJENmVrMUcxS0Z2ZWRsd0RaYTRKdGJSRUh5OHhCNnRjRzdMSXBiUkNBTnViejh1M0hVVExEWVBtK294dU80K0d0ZlE9PQ==",
									"size": "34.9 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlkvTy9zeHZvWEkxUUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "56.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRteGxKUXpvQlBQcVNhMlZCUg==",
									"size": "56.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmkvQmxGS3lwaDFaS0c1Q2hreExsZTh4U1l6Z2x5dXduc2RoTzVOYzNXaVN0Q0lQazBibktXblQ4UXNIZmlIalo0NVNvZVE9PQ==",
									"size": "56.9 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvVENyejNEVHBoUUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "102.5 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtamtGT2xOSmRPcjJBMEZvUA==",
									"size": "102.5 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynl0WkFOWWl4cW1SS2U4eVJoMExPSHNOZFRFdFgwdG9ocG9SVmxlUUFlQ3ltZXVDOHdNYmtPRGZpWXZIL3JYaU00dUN0YlE9PQ==",
									"size": "102.5 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 9 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-9-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk4V1N2anJiSDRoc0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "35.5 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta2d0WGtjNWRkTExRakZCYg==",
									"size": "35.5 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ymkvc1NGSWk1aVdWS0pKN0dvd1BPWnExUlZ5MGp0K1FSaUloVjVQQW5WMmV3TW9YazNNUC9UVXJWVllMNnF5Mko0N1NLUXc9PQ==",
									"size": "35.5 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlkrMnZvQUxOWXJCOEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "59.1 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbTA5T2tOOGVmZnlSMkFWZQ==",
									"size": "59.1 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym5QdHROcXl4bzNWS0lOVEcwMDMvVElCM1lqRXd4K0lkNnVWU3pMNFVZanFFREtYRXhjSHpWMVBIYllLbGt3Uy9ucm15VHc9PQ==",
									"size": "59.1 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrckNwVVhEU3AxaUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "101.3 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtamc1R21vQVNQYmpSbUZCYw==",
									"size": "101.3 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnV2UjlHNTJ5MTFaS2ZQV2R2Q3JaWFprZGRDTXQ2UEFHcW9wYzc5ZElCaXoxRll1OTZ0ek9VM0hvVnNUS3dnK0Y0YmVSRkE9PQ==",
									"size": "101.3 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 8 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-8-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvVFAxQUxVWjRoQktCd0k3OFZZdHNsWnpnPT0=",
									"size": "37.6 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaGw5Y3g5bGZJYjZkMFUwTQ==",
									"size": "37.6 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmtQQklEcnlob1ZWS0tNN2Fxa0c0Y0p0WFNBMHI1T1lidHNobnhzRUNiSG1KY2JEUC9mRGtibWpuZmM2cnN3Uzl4K0NuYlE9PQ==",
									"size": "37.6 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk1ZStnZzMyV290UktCd0k3OFZZdHNsWnpnPT0=",
									"size": "63.4 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta2wwRXo0TlRMYUtBbGxWZA==",
									"size": "63.4 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnJmUklDWitLbzN4S09NU0FvRVhkUTU1WE1EUlE0dllWc3RoMnhPd01RakNFQlliUTlzN25ObDNHWmMvYXd4YXQ1K2U3ZlE9PQ==",
									"size": "63.4 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk5YkUxMFRjYXM1c0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "107.4 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbVVNTWtNSkFPNzZLMkVkZg==",
									"size": "107.4 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmovQmZLNmFpckcxS0t2YWZseXppUXE1VU5nb1J0ZWtkdlB4WTFPQTJVaWUxQjVlNm9ycXNTSEtCWVlYaGdTR3l4S1BjUnc9PQ==",
									"size": "107.4 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 7 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-7-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrdWdoeEMxV29vU0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "38.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtamw5TWtJSlJkUCtaMkFNVA==",
									"size": "38.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnJ0SVRHWnE4Z1ZWS0orNndnU2ZqR3JCVWFBc0k3SmM2cElnTngvWlJWbTIrQytYZDM3cjVXRlBxYmNEd2poUzZ5ZVdQSEE9PQ==",
									"size": "38.0 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk5YkFsVGIyV2MwVUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "64.7 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtd1ZFTng5WmZLUG1MbUFFTg==",
									"size": "64.7 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmorTWFmSnFqdVhWS2RjcVpnajdhYUwwU2ZnSTF6TmsxaDlFRTU5TXZEUnYvS29YbXFjdXRiV0w3WUlUUXVRQzQwUHpSU3c9PQ==",
									"size": "64.7 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrR3Z0aG01UWN4TUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "116.7 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtejE1T2tvRlpLS2VFMEZwZg==",
									"size": "116.7 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnVmOFRKWSt5dWxaS0hKN0dsa2YvUTh0OVprMFA3dFlUNSt4KzhkWXVZemVQQWY3Q3l1WG5aVzM2YlAvV2x5aXg3NzJNYlE9PQ==",
									"size": "116.7 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 6 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-6-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkreTZsRWIwVExsSEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "38.4 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbjFFQXk0Sk5ldnJRamtVSQ==",
									"size": "38.4 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnF0RnRmcUtza201S2ZkT1pnUUxpVHJjU054a05zTUlmcVBSYnp2QUdCVHFVSWFYOTVNanJlbTZHV09MV2lTbUI3WW1oZFE9PQ==",
									"size": "38.4 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk4S1pvekRyUXBSeUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "65.8 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbDFSZGk5VWRlcXlOMkZrTg==",
									"size": "65.8 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynp2Qm1OS0twcW41S1laK1ZyVERaUUswSmNTbys3ZmtadW9oenh1OFdSZzd6SnVIUjRlanhOSGFLQm9EQWtpM2ZuL3lSZlE9PQ==",
									"size": "65.8 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrdkFxQVBMR0xFUktCd0k3OFZZdHNsWnpnPT0=",
									"size": "120.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbWs1YmlvTmFQNmVPZ1VFRw==",
									"size": "120.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmtQdFlKS3lxaDMxS0Q5K1ZxZ2E2V1pFSmR5QXQxdWhFcmRKTjc4RU9ZVFdFSFpmWm9jaWtjVEQ3YnVYWXJSbUducGFlUXc9PQ==",
									"size": "120.0 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 5 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-5-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrNml0QWJnUUtKTEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "42.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbjFJRWxJUkJJSzJKbEZvUg==",
									"size": "42.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YngvQVNEWWlrcW1SS0lmZXkxQkRpRjU5SmJqUVM4dlVEdmVWaWxyNERBaEtSRTdEUnl1dmFla1haWTRXaHFnclFrcm13U3c9PQ==",
									"size": "42.9 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk1V0dyaVBwZUpkREtCd0k3OFZZdHNsWnpnPT0=",
									"size": "71.4 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaDE5WG00ZElLckdTMVE4Qg==",
									"size": "71.4 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym0vTitDbzJ4cWxaS08reXpzeC9PRzlkdVpBNVE0Sk1CcUlsaThMTW1XRDZlRnFUOHh2R3FWbGZsQTlqMXBIbVJrWlcyWlE9PQ==",
									"size": "71.4 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvR2h2Qy9FRzR4U0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "132.1 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta1VnSG5NTWRQdjZEa2xZRQ==",
									"size": "132.1 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnVkVmZEcUc3cW5SS0lOVEdneEhWYkpKTVN4d29zODlPcTRwQTUrY0hCenV5RTVUanFQSDZTVkw4ZnRtcXZqbWl5SVNqWlE9PQ==",
									"size": "132.1 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 4 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-4-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvR0RxQkwyYks1ZEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "44.2 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaEFsZnlvTmVOTDZQaUFBQQ==",
									"size": "44.2 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmtPUWFHUHE2cW0xS1B2YWh5eEMrWDU5OWR6VUk0WkltbXQ5dTI5VXNabU9XZEl2RTlickhNVExCVmVUVWwzbWt5K2ExWVE9PQ==",
									"size": "44.2 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk1UzQxQnJGYTVCdktCd0k3OFZZdHNsWnpnPT0=",
									"size": "76.0 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtZ2xCRmw5OUNKZktGbVFJUA==",
									"size": "76.0 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnF1ZFBHNmVpcVh0S1BaUzZyeC9pR1p4N1NEUWs3OFlPcFBOYTZOWUtXUTZzYzdETXZmMnNTekdHQXZHbXd3K0ZrNE9xSEE9PQ==",
									"size": "76.0 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk1ZWYwQi9kVzVOZUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "135.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbEVFRmw4NFlQYStma1FJUg==",
									"size": "135.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Yng5VkFKSTJrcVdOS09OQ2JvMDM3WEtKK1Ywa3B3ZE1IczhSQThQUTFaanlqSmVycXlzWHRibFRDUXVmNm1pclp6THU5Unc9PQ==",
									"size": "135.9 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 3 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-3-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkvREdsQSswUnF4bEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "43.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta2s4Tng0VmZKN3lLaWxFVA==",
									"size": "43.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnRmdGxGTEs1cEc1S0JlU2tpQjdGYU0xSk53Qlg1TVlBcTlwV3ljSXlaZ0tKS3BMV3lzZmVXR3JVWm9UTWxoYVIwcGlGVHc9PQ==",
									"size": "43.9 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk4eWNvMGJjYnM1Y0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "73.6 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtZ1FzRGtOUlBQTHVNa3djQw==",
									"size": "73.6 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmkrQnVOcWU3bUhaS0JzUE9vajc1ZmNsN1dFTTcwdWdPa054YTFPOFdjRHlOZS83SDFNWDZSRjJDV2Y3QWxTV094WWFJWlE9PQ==",
									"size": "73.6 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk4cThuMERMZUtCb0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "129.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbEVwTm1OaENJYktBa0FBQw==",
									"size": "129.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmovQWJEcUNLb1g1S050YU9xQmZpSFlsaWJEZ1U3cGxFcE5sRGt0OGdWeitnT0x6UjljL0ZlWHpERGQvRmx4U1l4NmlEUXc9PQ==",
									"size": "129.9 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 2 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-2-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrcXRzRDdvZDRCektCd0k3OFZZdHNsWnpnPT0=",
									"size": "41.3 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta0VOVHk4NFRkS1hmMHdVSQ==",
									"size": "41.3 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YmkrZGZIYWVpb2xaS0E0cWZweDdWSEoxdFBpZ082TWNac29sUXhhc3ZiREQxQ1lUSTFOSFZia1dLQnU3ZnlCYU05NUtpZlE9PQ==",
									"size": "41.3 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlkvMmUxUU8rRnJOZUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "70.2 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtaHdzRmpzUkJlYUNjakFCYg==",
									"size": "70.2 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ynp1ZCtDb3FyaUdOS0l1L0hxQnI1SFk0UmFCNDc2dUl4bTgxQTI4Y1haRDJVSkw3RCt2N2FNekxSWk5uQnF5L2UzSWVPZlE9PQ==",
									"size": "70.2 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlkrcVZpd1Q4Zks5eEtCd0k3OFZZdHNsWnpnPT0=",
									"size": "121.6 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtd1ZwVGk4WmRQYVNhaDBBYQ==",
									"size": "121.6 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnF2OWxIWWk1ckgxS2UvS0VuampQWUpCR2Ewc0M2dGNCamM5NDQ5QU9lZ0h4R3FtK29zN3paVzdtV1BYTWxqK3Y0S3VCZlE9PQ==",
									"size": "121.6 MB",
								},
							],
						},
					},
					{
						"title": "Lycoris Recoil Episode 1 Subtitle Indonesia",
						"url": "https://otakudesu.video/episode/lr-episode-1-sub-indo/",
						"upload": "28 September,2022",
						"download": {
							"sd_360p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEZllJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk5T0ZrRDNyYlpGb0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "37.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRta0ZjTW1zUkZQNzdaMlY4Sw==",
									"size": "37.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3YnZlUitPL202czFaS0NOYXpqZ09oSHFoalB6TVVzYzRWNit4USt0Y0liUittQktyL3liSGViMHJaZDhTa21RdmJuN21QR0E9PQ==",
									"size": "37.9 MB",
								},
							],
							"sd_480p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEYlo0am9XQkY1ajBwY25zVk9ZcWlIalJnZlk5YUVvd0s2V1pjY0tCd0k3OFZZdHNsWnpnPT0=",
									"size": "64.4 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtbVE5R3pjOVRlTDJOajFRSQ==",
									"size": "64.4 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ymo5VllDNW15c1c1S0I1R3RpaVRrSDV0bFF4WVNzKzVPcDRVQWx1b1dWVGF3RDVyQXdjVGtYemZXRFB6NnVBK2o3WUtwRkE9PQ==",
									"size": "64.4 MB",
								},
							],
							"hd_720p": [
								{
									"name": "ZippyShare",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lUMzFEY1pJam9XQkY1ajBwY25zVk9ZcWlIalJnZlk4KzIxaTNnZFloZUtCd0k3OFZZdHNsWnpnPT0=",
									"size": "113.9 MB",
								},
								{
									"name": "Hxfile",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lNMEVHRVA4TzhVZzRtZ2xSQm1zNWVLUDJFaWdNQQ==",
									"size": "113.9 MB",
								},
								{
									"name": "Mega",
									"url": "https://desudrive.com/link/?id=eVYzczJaUk9LU0lKelVDTWZjam9IZ2RnbWx3Ym5OVnVGTE9rMUdWS2VwR1p0U2ZuUmRkdWZoSVordlVpcjlrQS9lTVFZaCtRS2J1Ky9PTDJlWDd6Wk82aHlnR2F6dWFEYlE9PQ==",
									"size": "113.9 MB",
								},
							],
						},
					},
				],
			}
		}
