import tweepy as tw
from decouple import config

from src.twitter.Idol import Idol
from src.utils.constants import (
    TWITTER_FIELDS,
    EXPANSIONS,
    MEDIA_FIELDS,
    USER_FIELDS,
)


class IdolListener(tw.StreamingClient):
    def on_connect(self):
        print("Connected!")

    def on_response(self, response: tw.StreamResponse):
        if response.data and not response.data.referenced_tweets:
            Idol.store_twitter_post(response)


def run():
    rule = Idol.generate_holo_en_rule()
    streaming_client = IdolListener(config("BEARER_TOKEN"))
    streaming_client.add_rules(tw.StreamRule(rule))

    streaming_client.filter(
        tweet_fields=TWITTER_FIELDS,
        expansions=EXPANSIONS,
        media_fields=MEDIA_FIELDS,
        user_fields=USER_FIELDS,
    )
