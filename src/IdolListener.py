import tweepy as tw
from utils import store_twitter_post


class IdolListener(tw.StreamingClient):
    def on_connect(self):
        print("Connected!")

    def on_response(self, response):
        if not response.data.referenced_tweets:
            store_twitter_post(response)
