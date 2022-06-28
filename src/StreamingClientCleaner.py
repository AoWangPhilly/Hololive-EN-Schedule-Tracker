from pprint import pprint
from typing import Any
import tweepy as tw


def extract_thumbnail_link_from_youtube_link(youtube_link: str) -> str:
    start_index = youtube_link.rfind("/") + 1
    video_id = youtube_link[start_index:]
    return f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"


class StreamingClientCleaner:
    @staticmethod
    def reformat_response(response: tw.StreamResponse) -> dict[str, Any]:
        output = {}
        data, includes, _, _ = response
        output["author_id"] = data.author_id
        output["created_at"] = data.created_at
        output["twitter_post_id"] = data.id
        output["text"] = data.text

        if (
            data.entities
            and (url := data.entities["urls"][0]["expanded_url"])
            and url.startswith("https://youtu.be")
        ):
            output["youtube_link"] = url
            thumbnail_picture = extract_thumbnail_link_from_youtube_link(
                output["youtube_link"]
            )
            output["image_path"] = thumbnail_picture
        elif "media" in includes:
            media = includes["media"][0]
            if media.url:
                output["image_path"] = media.url
            elif media.preview_image_url:
                output["image_path"] = media.preview_image_url
        pprint(output)
        return output
