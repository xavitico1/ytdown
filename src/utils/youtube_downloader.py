class YouTubeDownloader:
    def __init__(self):
        pass

    def download_video(self, url):
        from pytube import YouTube
        
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()
            return f"Downloaded: {video.title}"
        except Exception as e:
            return f"An error occurred: {str(e)}"