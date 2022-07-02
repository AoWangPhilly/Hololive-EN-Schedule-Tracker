from decouple import config

from src.youtube.YouTubeStats import YouTubeStats
from src.youtube.utils.constants import (
    HOLOLIVE_EN_MYTH_YOUTUBE_ID,
    HOLOLIVE_EN_COUNCIL_YOUTUBE_ID,
    HOLOLIVE_EN_VSINGER_YOUTUBE_ID,
)

API_KEY = config("YOUTUBE_API_KEY")


if __name__ == "__main__":
    yt_ids = (
        HOLOLIVE_EN_MYTH_YOUTUBE_ID
        + HOLOLIVE_EN_COUNCIL_YOUTUBE_ID
        + HOLOLIVE_EN_VSINGER_YOUTUBE_ID
    )
    for yt_id in yt_ids:
        yt = YouTubeStats(api_key=API_KEY, channel_id=yt_id)

        yt.get_channel_statistics()
        print(yt.channel_statistics)
