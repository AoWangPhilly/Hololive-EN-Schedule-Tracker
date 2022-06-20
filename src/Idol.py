from typing import Optional
import tweepy
from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from dataclasses import dataclass

@dataclass
class Idol:
    ...

def connect_to_twitter() -> Optional[tweepy.API]:
    auth = tweepy.OAuthHandler(
        consumer_key=API_KEY, 
        consumer_secret=API_KEY_SECRET, 
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")

if __name__ == "__main__":

    api = connect_to_twitter()
    mori_tweets = api.user_timeline(screen_name="moricalliope")
    for tweet in mori_tweets:
        if "SCHEDULE" in tweet.text:
            print(tweet.entities["media"][0]["media_url"])
