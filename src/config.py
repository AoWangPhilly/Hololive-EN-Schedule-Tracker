from typing import Optional
import tweepy as tw
from decouple import config
from pydantic import BaseSettings


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


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    database_name: str

    class Config:
        env_file = ".env"


settings = Settings()
