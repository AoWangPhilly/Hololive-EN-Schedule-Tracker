from typing import Optional
import tweepy
from decouple import config

def connect_to_twitter() -> Optional[tweepy.API]:
    config_info = {
        "consumer_key": config("CONSUMER_KEY"),
        "consumer_secret": config("CONSUMER_SECRET"),
        "access_token": config("ACCESS_TOKEN"),
        "access_token_secret": config("ACCESS_TOKEN_SECRET")
    }
    auth = tweepy.OAuthHandler(**config_info)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        raise e
    return api