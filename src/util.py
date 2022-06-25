from constants import (
    HOLOLIVE_EN_COUNCIL_TAGS,
    HOLOLIVE_EN_MYTH_TAGS,
    HOLOLIVE_EN_VSINGER_TAGS,
)
from typing import Any
from typing import Optional
import tweepy as tw
from decouple import config
from database import get_db, engine
import models


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


def clean_data(dirty_json: dict[str, Any]) -> dict[str, Any]:
    cleaned_dict = {}
    data = dirty_json.get("data")
    includes = dirty_json.get("includes")

    if data is None:
        print("Bad connection?? Missing data key!")
        print("-" * 150)
        print(dirty_json)
    else:
        cleaned_dict["author_id"] = data["author_id"]
        cleaned_dict["created_at"] = data["created_at"]
        cleaned_dict["twitter_post_id"] = data["id"]
        cleaned_dict["text"] = data["text"]

        if includes is None:
            print("Missing includes Key!!")
            print("-" * 150)
            print(dirty_json)
        else:
            media = includes.get("media")
            if media is not None:
                cleaned_dict["image_path"] = includes["media"][0]["preview_image_url"]

            for user in includes["users"]:
                if user["id"] == cleaned_dict["author_id"]:
                    cleaned_dict["username"] = user["username"]
                    cleaned_dict["name"] = user["name"]
                    break

    return cleaned_dict


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
