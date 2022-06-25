import tweepy as tw
from decouple import config
from util import generate_holo_en_rule
from json import loads
from pprint import pprint

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
            pprint(tweet_data)
            print()
            

if __name__ == "__main__":
    rule = generate_holo_en_rule()
    streaming_client = IdolListener(config("BEARER_TOKEN"))
    streaming_client.add_rules(tw.StreamRule(rule))

    streaming_client.filter(
        tweet_fields="id,text,author_id,created_at,entities,referenced_tweets",
        expansions="author_id,attachments.media_keys",
        media_fields="duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text",
        user_fields="username,name"
    )




