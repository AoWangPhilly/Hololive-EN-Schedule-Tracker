from decouple import config
from YouTubeStats import YouTubeStats

API_KEY = config("YOUTUBE_API_KEY")


if __name__ == "__main__":
    yt = YouTubeStats(api_key=API_KEY, channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g")
    yt.get_channel_statistics()
