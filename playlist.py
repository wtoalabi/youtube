from pytube import Playlist,YouTube
import re
url = "https://www.youtube.com/playlist?list=PLJbE2Yu2zumDjfrfu8kisK9lQVcpMDDzZ"
destination="/Users/mac/documents/CourseVideos/dart/Dart for Beginners"
playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

for url in playlist.video_urls:
    YouTube(url).streams.first().download(destination)
