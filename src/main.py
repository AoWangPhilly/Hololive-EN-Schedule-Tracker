from database import engine
import models
from Idol import generate_holo_en_rule
from decouple import config
from IdolListener import IdolListener
import tweepy as tw
from constants import TWITTER_FIELDS, EXPANSIONS, MEDIA_FIELDS, USER_FIELDS

if __name__ == "__main__":
    models.Base.metadata.create_all(engine)

    rule = generate_holo_en_rule()
    streaming_client = IdolListener(config("BEARER_TOKEN"))
    streaming_client.add_rules(tw.StreamRule(rule))

    streaming_client.filter(
        tweet_fields=TWITTER_FIELDS,
        expansions=EXPANSIONS,
        media_fields=MEDIA_FIELDS,
        user_fields=USER_FIELDS,
    )
