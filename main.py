from googleapiclient.discovery import build
from os import system

youtubeApiKey = "AIzaSyD3At1eJPVyPlYycyhV6BgCBfyBi8vhTho" #coloque aqui sua chave api
playlistId = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey = youtubeApiKey)

videos = youtube.playlistItems().list(part = "snippet", playlistId = playlistId, maxResults = 20).execute()
playlist = videos["items"]

videoViewsDict = {}

for video in playlist:
    videoId = video["snippet"]["resourceId"]["videoId"]
    videoName = video["snippet"]["title"]
    statisticResponse = youtube.videos().list(part = "statistics", id = videoId).execute()
    views = statisticResponse["items"][0]["statistics"].get("viewCount", 0)
    videoViewsDict[videoName] = views

videoViewsDictSorted = dict(sorted(videoViewsDict.items(), key = lambda item: item[1], reverse = True))

system("cls")

print("Vídeos de \"Race Highlights 2024\" Ordenados por vizualizações:\n")

i=1

for key, value in videoViewsDictSorted.items():
    print(f"{i}º Vídeo\nTítulo: {key}\nVizualizações: {value}")
    print()
    i = i+1