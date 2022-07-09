import logging
from typing import Optional

import tweepy as tw
from decouple import config

from src.twitter.ResponseFormatter import ResponseFormatter


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
