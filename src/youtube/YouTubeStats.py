from dataclasses import dataclass
from typing import Dict, Optional
import requests
import json


@dataclass
class YouTubeStats:
    api_key: str
    channel_id: str
    channel_statistics: Optional[Dict] = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            statistics = data["items"][0]["statistics"]
        except:
            statistics = None
        self.channel_statistics = statistics
        return statistics
