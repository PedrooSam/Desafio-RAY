from googleapiclient.discovery import build
from os import system

youtubeApiKey = "" #COLOQUE AQUI SUA CHAVE API
playlistId = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey = youtubeApiKey)

#pegando infomrações dos videos da playlist
videos = youtube.playlistItems().list(part = "snippet", playlistId = playlistId, maxResults = 20).execute()
playlist = videos["items"]

videoViewsDict = {}

#obtendo o nome e views de cada video e salvando no dicionário criado
for video in playlist:
    videoId = video["snippet"]["resourceId"]["videoId"]
    videoName = video["snippet"]["title"]
    statisticResponse = youtube.videos().list(part = "statistics", id = videoId).execute()
    views = statisticResponse["items"][0]["statistics"].get("viewCount", 0)
    videoViewsDict[videoName] = views

#ordenando o dicionário pelas views em ordem decrecente
videoViewsDictSorted = dict(sorted(videoViewsDict.items(), key = lambda item: item[1], reverse = True))

system("cls")

print("Vídeos de \"Race Highlights 2024\" Ordenados por vizualizações:\n")

i=1
#imprimindo as informações salvas
for key, value in videoViewsDictSorted.items():
    print(f"{i}º Vídeo\nTítulo: {key}\nVizualizações: {value}")
    print()
    i = i+1