from dataclasses import dataclass
from pprint import pprint
from typing import Dict, List, Optional
import requests
import json

from decouple import config

from src.database import get_db
from src.youtube.models import YouTubeIdol, YouTubeStatistic


from src.youtube.utils.constants import (
    HOLOLIVE_EN_MYTH_YOUTUBE_ID,
    HOLOLIVE_EN_COUNCIL_YOUTUBE_ID,
    HOLOLIVE_EN_VSINGER_YOUTUBE_ID,
)

API_KEY = config("YOUTUBE_API_KEY")


@dataclass
class YouTubeStats:
    api_key: str
    channel_ids: List[str]
    channel_statistics: Optional[Dict] = None

    @property
    def ids(self) -> str:
        return ",".join(self.channel_ids)

    def get_idol_info(self) -> Dict:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet&id={self.ids}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        output = []
        for idol in data["items"]:
            temp = {}
            temp["youtube_id"] = idol["id"]
            snippet = idol["snippet"]
            temp["title"] = snippet["title"]
            temp["description"] = snippet["description"]
            temp["published_at"] = snippet["publishedAt"]
            temp["thumbnail"] = snippet["thumbnails"]["high"]["url"]
            output.append(temp)
        return output

    def save_idol_info_to_db(self):
        db_gen = get_db()
        db = next(db_gen)

        idols_info = self.get_idol_info()

        for idol_info in idols_info:
            pprint(idol_info)
            new_idol = YouTubeIdol(**idol_info)

            db.add(new_idol)
            db.commit()
            db.refresh(new_idol)

    def get_channel_statistics(self):
        ids = ",".join(self.channel_ids)
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={ids}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        output = []
        pprint(data)
        for idol in data["items"]:
            temp = {}
            temp["youtube_id"] = idol["id"]
            stats = idol["statistics"]
            temp["subscriber_count"] = stats["subscriberCount"]
            temp["video_count"] = stats["videoCount"]
            temp["view_count"] = stats["viewCount"]
            output.append(temp)
        return output

    def save_statistics_to_db(self):
        db_gen = get_db()
        db = next(db_gen)

        idol_stats = self.get_channel_statistics()

        for idol_stat in idol_stats:
            new_idol = YouTubeStatistic(**idol_stat)

            db.add(new_idol)
            db.commit()
            db.refresh(new_idol)


def run():
    yt_ids = (
        HOLOLIVE_EN_MYTH_YOUTUBE_ID
        + HOLOLIVE_EN_COUNCIL_YOUTUBE_ID
        + HOLOLIVE_EN_VSINGER_YOUTUBE_ID
    )
    yt = YouTubeStats(api_key=API_KEY, channel_ids=yt_ids)
    # yt.save_idol_info_to_db()

    yt.save_statistics_to_db()
