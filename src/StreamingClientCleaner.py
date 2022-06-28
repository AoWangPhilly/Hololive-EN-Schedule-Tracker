from typing import Any


class StreamingClientCleaner:
    def clean_data(self, dirty_json: dict[str, Any]) -> dict[str, Any]:
        cleaned_dict = {}
        data = dirty_json.get("data")
        includes = dirty_json.get("includes")
        entities = data.get("entities")

        cleaned_dict["author_id"] = data["author_id"]
        cleaned_dict["created_at"] = data["created_at"]
        cleaned_dict["twitter_post_id"] = data["id"]
        cleaned_dict["text"] = data["text"]

        if entities is not None and "urls" in entities:
            urls = entities["urls"][0]
            if "unwound_url" in urls and urls["unwound_url"].startswith(
                "https://www.youtube.com"
            ):
                cleaned_dict["youtube_link"] = urls["unwound_url"]

                thumbnail_picture = self.__extract_thumbnail_link_from_youtube_link(
                    cleaned_dict["youtube_link"]
                )
                cleaned_dict["image_path"] = thumbnail_picture

        if includes is not None:
            media = includes.get("media")
            if media is not None:
                content = includes["media"][0]
                if "url" in content:
                    cleaned_dict["image_path"] = content["url"]
                elif "preview_image_url" in content:
                    cleaned_dict["image_path"] = content["preview_image_url"]
        return cleaned_dict

    def __extract_thumbnail_link_from_youtube_link(self, youtube_link: str) -> str:
        start_index = youtube_link.find("=") + 1
        end_index = youtube_link.find("&")
        if end_index != -1:
            video_id = youtube_link[start_index:end_index]
        else:
            video_id = youtube_link[start_index:]
        return f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
