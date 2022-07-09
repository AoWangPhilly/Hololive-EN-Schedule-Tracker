from decouple import config

from src.utils.constants import (
    HOLOLIVE_EN_MYTH_YOUTUBE_ID,
    HOLOLIVE_EN_COUNCIL_YOUTUBE_ID,
    HOLOLIVE_EN_VSINGER_YOUTUBE_ID,
)
from src.youtube.YouTubeAPIWrapper import YouTubeAPIWrapper

API_KEY = config("YOUTUBE_API_KEY")


def run():
    yt_ids = (
        HOLOLIVE_EN_MYTH_YOUTUBE_ID
        + HOLOLIVE_EN_COUNCIL_YOUTUBE_ID
        + HOLOLIVE_EN_VSINGER_YOUTUBE_ID
    )
    yt = YouTubeAPIWrapper(api_key=API_KEY, channel_ids=yt_ids)
    # yt.save_idol_info_to_db()

    yt.save_statistics_to_db()
