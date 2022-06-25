import tweepy as tw
from json import loads
from util import store_twitter_post


class IdolListener(tw.StreamingClient):
    def on_connect(self):
        print("Connected!")

    def on_data(self, raw_data):
        tweet_data = loads(raw_data)

        if tweet_data.get("data", None) is None:
            print("WEIRD THING HAPPENED")
            print("-" * 100)
            print(tweet_data)

        elif not tweet_data["data"].get("referenced_tweets"):
            store_twitter_post(tweet_data)
