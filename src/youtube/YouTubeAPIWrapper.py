from typing import Dict, List, Optional
from dataclasses import dataclass
from pprint import pprint
import json

import requests

from src.database import get_db
from src.models import YouTubeIdol, YouTubeStatistic


@dataclass
class YouTubeAPIWrapper:
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
            snippet = idol["snippet"]

            temp["youtube_id"] = idol["id"]
            temp["title"] = snippet["title"]
            temp["description"] = snippet["description"]
            temp["published_at"] = snippet["publishedAt"]
            temp["thumbnail"] = snippet["thumbnails"]["high"]["url"]
            output.append(temp)

        return output

    def save_idol_info_to_db(self):
        db_gen = get_db()
        db = next(db_gen)

        idol_infos = self.get_idol_info()

        for idol_info in idol_infos:
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

        for idol in data["items"]:
            temp = {}
            stats = idol["statistics"]

            temp["youtube_id"] = idol["id"]
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
