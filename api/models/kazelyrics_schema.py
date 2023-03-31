from pydantic import BaseModel, HttpUrl
from typing import Dict

AUTHOR = "Sandy Sayang Gawr Gura"
	

class KazelyricsResultsSchema(BaseModel):
	title: str
	url: HttpUrl
	thumbnail: HttpUrl
	lyrics: str


class KazelyricsSchema(BaseModel):
	author: str
	status: int
	results: list[KazelyricsResultsSchema]

	class Config:
		schema_extra = {
			"example": {
				"author": AUTHOR,
				"status": 200,
				"results": [
					{
						"title": "[Lirik+Terjemahan] back number - Suiheisen (Horison)",
						"url": "https://www.kazelyrics.com/2020/08/lirikterjemahan-back-number-suiheisen.html",
						"thumbnail": "https://1.bp.blogspot.com/-diiFLhgiZvY/YRaBhBkMgQI/AAAAAAAAjuQ/rTWemUtGzpo8YTz3EjgcU-oy4abL02JSgCLcBGAsYHQ/w330-h330-p-k-no-nu/back%2Bnumber%2B-%2BSuiheisen%2BLyrics%2BTranslation.jpg",
						"lyrics": 'ROMAJI:\n\nDekiru dake uso wa nai you ni\n\nDonna toki mo yasashiku areru you ni\n\nHito ga itami wo kanjita toki ni wa\n\nJibun no koto no you ni omoeru you ni\n\n\n\nTadashisa wo betsu no tadashisa de\n\nNakusu kanashimi ni mo deau keredo\n\n\n\nSuiheisen ga hikaru asa ni\n\nAnata no kibou ga kuzure ochite\n\nKaze ni tobasareru kakera ni\n\nDareka ga kirei to tsubuyaiteru\n\n\n\nKanashii koe de utai nagara\n\nItsushika umi ni nagaretsuite hikatte\n\nAnata wa sore wo miru deshou\n\n\nJibun no senaka wa mienai no dakara\n\nHazukashi garazu hito ni tazuneru to ii\n\nKokoro wa darenimo mienai no dakara\n\nMieru mono yori mo daiji ni suru to ii\n\n\n\nMainichi ga kasanaru koto de\n\nAenaku naru hito mo dekiru keredo\n\n\n\nSukitooru hodo awai yoru ni\n\nAnata no yume ga hitotsu kanatte\n\nKansei to hakushu no naka ni \n\nDareka no himei ga kakurete iru\n\n\n\nTaeru riyuu wo sagashi nagara\n\nIkutsu mo kotae wo kakae nagara\n\nNayande\n\nAnata wa jibun wo shiru deshou\n\n\n\nDare no kokoro ni nokoru koto mo\n\nMe ni yakitsuku koto mo nai kyou mo\n\nZatsuon to ashioto no oku de\n\nWatashi wa koko da to sakendeiru\n\n\n\nSuiheisen ga hikaru asa ni\n\nAnata no kibou ga kuzure ochite\n\nKaze ni tobasareru kakera ni\n\nDareka ga kirei to tsubuyaiteru\n\n\n\nKanashii koe de utai nagara\n\nItsushika umi ni nagaretsuite hikatte\n\nAnata wa sore wo miru deshou\n\n\n\nAnata wa sore wo miru deshou\n\n\n\n\n\nKANJI:\n\nback number - 水平線\n\n\n\n出来るだけ嘘は無いように\n\nどんな時も優しくあれるように\n\n人が痛みを感じた時には\n\n自分の事のように思えるように\n\n\n\n正しさを別の正しさで\n\n失くす悲しみにも出会うけれど\n\n\n\n水平線が光る朝に\n\nあなたの希望が崩れ落ちて\n\n風に飛ばされる欠片に\n\n誰かが綺麗と呟いてる\n\n\n\n悲しい声で歌いながら\n\nいつしか海に流れ着いて 光って\n\nあなたはそれを見るでしょう\n\n\n\n自分の背中は見えないのだから\n\n恥ずかしがらず人に尋ねるといい\n\n心は誰にも見えないのだから\n\n見えるものよりも大事にするといい\n\n\n\n毎日が重なる事で\n\n会えなくなる人も出来るけれど\n\n\n\n透き通るほど淡い夜に\n\nあなたの夢がひとつ叶って\n\n歓声と拍手の中に\n\n誰かの悲鳴が隠れている\n\n\n\n耐える理由を探しながら\n\nいくつも答えを抱えながら\n\n悩んで\n\nあなたは自分を知るでしょう\n\n\n\n誰の心に残る事も\n\n目に焼き付く事もない今日も\n\n雑音と足音の奥で\n\n私はここだと叫んでいる\n\n\n\n水平線が光る朝に\n\nあなたの希望が崩れ落ちて\n\n風に飛ばされる欠片に\n\n誰かが綺麗と呟いてる\n\n\n\n悲しい声で歌いながら\n\nいつしか海に流れ着いて 光って\n\nあなたはそれを見るでしょう\n\n\n\nあなたはそれを見るでしょう\n\nENGLISH TRANSLATION:\n\nback number - Horizon\n\nDon\'t tell as many lies as possible\nGive your kindness at any time\nWhen someone feels sadness\nThink as if you feel it too\n\nIf you justify it with another truth\nThe sadness that was lost will only return\n\nOn the horizon when the morning sun shines\nAll your hopes will be crushed\nIt became fragments blown by the wind\nSomeone will mutter "so beautiful"\n\nWhile you sing a sad voice\nOne day, it will flow into the sea and shine\nYou can see it too, right?\n\nYour back is something that can\'t see by yourself\nTherefore, don\'t be shy about asking for help from others\nYour heart is something no one else can see\nYou should value it more than anything seen\n\nWith the overlapping days\nWe can meet people we cannot meet\n\nOn a faint and transparent night\nYour one hope will come true\nIn the boisterous cheers and applause\nSomeone\'s scream can definitely hide\n\nWhile looking for reasons to survive\nWhile looking for answers several times\nYou feel anxious\nYou can figure it out on your own, right?\n\nToday will never remain in anyone\'s heart\nToday won\'t be a good memory either\nBehind the sound of steps and noise\nShout out loud "I\'m here"\n\nOn the horizon when the morning sun shines\nAll your hopes will be crushed\nIt became fragments blown by the wind\nSomeone will mutter "so beautiful"\n\nWhile you sing a sad voice\nOne day, it will flow into the sea and shine\nYou can see it too, right?\n\nYou can see it too, right?\n\n\n\n\n\nINDONESIA:\n\nJangan hanya mengucapkan kebohongan\n\nBerbuatlah kebaikan di saat kapan pun\n\nKetika seseorang merasakan kesedihan\n\nBerpikirlah seolah kau merasakannya juga\n\n\n\nJika membenarkan dengan kebenaran lainnya\n\nKesedihan yang telah hilang hanya akan kembali\n\n\n\nDi horison ketika matahari pagi bersinar\n\nSegala harapanmu akan runtuh dan hancur\n\nMenjadi pecahan yang diterbangkan angin\n\nSeseorang akan bergumam "indah sekali"\n\n\n\nKetika kau menyanyikan suara yang sedih\n\nSuatu saat ia akan mengalir ke laut dan bersinar\n\nKau pasti dapat melihatnya juga, iya kan?\n\n\n\nPunggung adalah sesuatu yang tak bisa kau lihat sendiri\n\nKarenanya jangan malu untuk meminta bantuan orang lain\n\nHati adalah sesuatu yang tak bisa dilihat orang lain\nKau harus lebih menghargainya melebihi apa yang terlihat\n\n\nDengan setiap hari yang terus tumpang-tindih\n\nKita dapat bertemu orang yang tak dapat kita temui\n\n\n\nDi malam yang fana dan seolah transparan\n\nSatu harapanmu akan dapat menjadi nyata\n\nDi dalam riuhnya sorakan dan tepuk tangan\n\nTeriakan seseorang pasti dapat bersembunyi\n\n\n\nSementara mencari alasan untuk bertahan\n\nSementara mencari jawaban beberapa kali\n\nKau merasa cemas\n\nKau pasti dapat mengetahuinya, iya kan?\n\n\n\nHari ini takkan terkenang di hati seseorang\n\nHari ini juga takkan menjadi kenangan yang indah\n\nDi balik suara langkah dan kebisingan itu\n\nBerteriaklah dengan keras "aku ada di sini"\n\n\n\nDi horison ketika matahari pagi bersinar\n\nSegala harapanmu akan runtuh dan hancur\n\nMenjadi pecahan yang diterbangkan angin\n\nSeseorang akan bergumam "indah sekali"\n\n\n\nKetika kau menyanyikan suara yang sedih\n\nSuatu saat ia akan mengalir ke laut dan bersinar\n\nKau pasti dapat melihatnya juga, iya kan?\n\n\n\nKau pasti dapat melihatnya juga, iya kan?',
					}
				],
			}
		}
