from database import engine
import models
from util import generate_holo_en_rule
from decouple import config
from IdolListener import IdolListener
import tweepy as tw

if __name__ == "__main__":
    models.Base.metadata.create_all(engine)

    rule = generate_holo_en_rule()
    streaming_client = IdolListener(config("BEARER_TOKEN"))
    streaming_client.add_rules(tw.StreamRule(rule))

    streaming_client.filter(
        tweet_fields="id,text,author_id,created_at,entities,referenced_tweets",
        expansions="author_id,attachments.media_keys",
        media_fields="duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text",
        user_fields="username,name",
    )
