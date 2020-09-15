from pytube import YouTube
url = ""
destination = "/Users/mac/documents/CourseVideos/"
YouTube(url).streams.first().download(destination);
