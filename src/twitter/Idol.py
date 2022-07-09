from pprint import pprint
from typing import Any
import logging

from src.utils.constants import (
    HOLOLIVE_EN_COUNCIL_TAGS,
    HOLOLIVE_EN_MYTH_TAGS,
    HOLOLIVE_EN_VSINGER_TAGS,
    TWITTER_FIELDS,
    EXPANSIONS,
    MEDIA_FIELDS,
    USER_FIELDS,
)

from src.utils.util import (
    connect_to_twitter_api,
    connect_to_twitter_client,
)

from src.twitter.ResponseFormatter import (
    ResponseFormatter,
    extract_thumbnail_link_from_youtube_link,
)

from src.database import get_db
import src.models as models


logging.basicConfig(
    filename="std.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Idol:
    @staticmethod
    def get_idol_info(screen_name: str) -> dict:
        api = connect_to_twitter_api()
        user = api.get_user(screen_name=screen_name)
        return {
            "author_id": user.id,
            "username": screen_name,
            "name": user.name,
            "icon_path": user.profile_image_url_https,
        }

    @staticmethod
    def store_all_idol_info_to_db() -> None:
        IDOLS = (
            HOLOLIVE_EN_COUNCIL_TAGS + HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS,
        )[0]

        db_gen = get_db()
        db = next(db_gen)
        for idol_screen_name in IDOLS:
            idol_info = Idol.get_idol_info(idol_screen_name)
            idol = models.Idol(**idol_info)
            db.add(idol)
            db.commit()
            db.refresh(idol)
            print(idol)

    @staticmethod
    def generate_holo_en_rule() -> str:
        hololive_tags = (
            HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
        )
        hololive_tag = [f"from:{tag}" for tag in hololive_tags]
        return " OR ".join(hololive_tag)

    @staticmethod
    def store_twitter_post(data: dict[str, Any]) -> None:
        db_gen = get_db()
        db = next(db_gen)
        try:
            data = ResponseFormatter.reformat_response(data)
            new_post = models.TwitterPost(**data)

            pprint(data)
            pprint(new_post)

            db.add(new_post)
            db.commit()
            db.refresh(new_post)
            print("SUCCESS!! Now in the database :)\n\n")
        except Exception as e:
            logging.critical(f"Critical: {e}")

    @staticmethod
    def gather_historic_tweets(username: str) -> dict[str, Any]:
        client = connect_to_twitter_client()
        db_gen = get_db()
        db = next(db_gen)
        user = client.get_user(username=username)

        tweets = client.get_users_tweets(
            id=user.data.id,
            exclude=["retweets", "replies"],
            tweet_fields=TWITTER_FIELDS,
            expansions=EXPANSIONS,
            user_fields=USER_FIELDS,
            media_fields=MEDIA_FIELDS,
            max_results=100,
        )

        twitter_posts, includes, _, _ = tweets

        for t in twitter_posts:
            output = {}
            output["author_id"] = t.author_id
            output["created_at"] = t.created_at
            output["twitter_post_id"] = t.id
            output["text"] = t.text
            if (
                t.entities
                and (urls := t.entities.get("urls"))
                and (url := urls[0]["expanded_url"])
                and url.startswith("https://youtu.be")
            ):
                thumbnail_picture = extract_thumbnail_link_from_youtube_link(url)
                output["youtube_link"] = url
                output["image_path"] = thumbnail_picture

                if not output.get("image_path"):
                    media_key = t.entities["urls"][1]["media_key"]
                    if "media" in includes:
                        for media in includes["media"]:
                            if media.media_key == media_key:
                                if media.url:
                                    output["image"] = media.url
                                elif media.preview_image_url:
                                    output["image"] = media.preview_image_url
            pprint(output)
            post = (
                db.query(models.TwitterPost)
                .filter(models.TwitterPost.twitter_post_id == output["twitter_post_id"])
                .first()
            )
            if not post:
                print("SUCCESS")
                new_post = models.TwitterPost(**output)
                db.add(new_post)
                db.commit()
                db.refresh(new_post)
            print("\n\n")

    @staticmethod
    def get_all_idols_historic_tweets():
        usernames = (
            HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
        )
        for username in usernames:
            Idol.gather_historic_tweets(username=username)
