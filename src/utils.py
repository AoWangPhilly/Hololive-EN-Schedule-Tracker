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


def connect_to_twitter_api() -> Optional[tw.API]:
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


def connect_to_twitter_client() -> Optional[tw.Client]:
    return tw.Client(bearer_token=config("BEARER_TOKEN"))


def store_twitter_post(data: dict[str, Any]) -> None:
    db_gen = get_db()
    db = next(db_gen)
    try:
        data = StreamingClientCleaner.reformat_response(data)
        new_post = models.TwitterPost(**data)

        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        print("SUCCESS!! Now in the database :)")
    except Exception as e:
        logging.critical(f"Critical: {e}")
