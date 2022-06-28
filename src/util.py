from constants import (
    HOLOLIVE_EN_COUNCIL_TAGS,
    HOLOLIVE_EN_MYTH_TAGS,
    HOLOLIVE_EN_VSINGER_TAGS,
)
from typing import Any, Optional
import tweepy as tw
from decouple import config
from database import get_db
import models
from StreamingClientCleaner import StreamingClientCleaner
import logging

logging.basicConfig(
    filename="std.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def connect_to_twitter() -> Optional[tw.API]:
    config_info = {
        "consumer_key": config("CONSUMER_KEY"),
        "consumer_secret": config("CONSUMER_SECRET"),
        "access_token": config("ACCESS_TOKEN"),
        "access_token_secret": config("ACCESS_TOKEN_SECRET"),
    }
    auth = tw.OAuthHandler(**config_info)

    api = tw.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        raise e
    return api


def generate_holo_en_rule() -> str:
    hololive_tags = (
        HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
    )
    hololive_tag = [f"from:{tag}" for tag in hololive_tags]
    return " OR ".join(hololive_tag)


def get_idol_info(screen_name: str) -> dict:
    api = connect_to_twitter()
    user = api.get_user(screen_name=screen_name)
    return {
        "author_id": user.id,
        "username": screen_name,
        "name": user.name,
        "icon_path": user.profile_image_url_https,
    }


def store_all_idol_info_to_db() -> None:
    IDOLS = (
        HOLOLIVE_EN_COUNCIL_TAGS + HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS,
    )[0]

    db_gen = get_db()
    db = next(db_gen)
    for idol_screen_name in IDOLS:
        print(idol_screen_name)
        idol_info = get_idol_info(idol_screen_name)
        idol = models.Idol(**idol_info)
        db.add(idol)
        db.commit()
        db.refresh(idol)
        print(idol)


def store_twitter_post(data: dict[str, Any]) -> None:
    db_gen = get_db()
    db = next(db_gen)
    try:
        data = StreamingClientCleaner.clean_data(data)
        new_post = models.TwitterPost(**data)

        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        print("SUCCESS!! Now in the database :)")
    except Exception as e:
        logging.critical(f"Critical: {e}")
