from googleapiclient.discovery import build
from os import system

chaveApiYoutube = "AIzaSyD3At1eJPVyPlYycyhV6BgCBfyBi8vhTho"
idPlaylist = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

youtube = build("youtube", "v3", developerKey = chaveApiYoutube)

videos = youtube.playlistItems().list(part = "snippet", playlistId = idPlaylist, maxResults = 20).execute()
playlist = videos["items"]

system("cls")

for video in playlist:
    print(video["snippet"]["title"])