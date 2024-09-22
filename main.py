from googleapiclient.discovery import build
from os import system

youtubeApiKey = "AIzaSyD3At1eJPVyPlYycyhV6BgCBfyBi8vhTho"
idPlaylist = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey = youtubeApiKey)

videos = youtube.playlistItems().list(part = "snippet", playlistId = idPlaylist, maxResults = 20).execute()
playlist = videos["items"]

statisticVideos = []

for video in playlist:
    idVideo = video["snippet"]["resourceId"]["videoId"]
    statisticResponse = youtube.videos().list(part = "statistics", id = idVideo).execute()
    statisticVideos.append(statisticResponse)

system("cls")

for video in statisticVideos:
    views = video["items"][0]["statistics"].get("viewCount", 0)
    print(views)
    print()