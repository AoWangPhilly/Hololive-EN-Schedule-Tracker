
from dataclasses import dataclass
from config import connect_to_twitter

HOLOLIVE_EN_MYTH_TAGS = [
    "moricalliope",
    "takanashikiara",
    "ninomaeinanis",
    "gawrgura",
    "watsonameliaEN",
]

HOLOLIVE_EN_VSINGER_TAGS = [
    "irys_en"
]

HOLOLIVE_EN_COUNCIL_TAGS = [
    "tsukumosana",
    "ceresfauna",
    "ourokronii",
    "nanashimumei_en",
    "hakosbaelz"
]


@dataclass
class Idol:
    twitter_tag: str

if __name__ == "__main__":
    
    api = connect_to_twitter()
    # idol_tweets = api.user_timeline(
    #     screen_name="watsonameliaEN", 
    #     count=200,
    #     include_rts = False,
    #     tweet_mode = 'extended'
    # )

    # for tweet in idol_tweets:
    #     # if "schedule" in tweet.full_text.lower():
    #     # print(tweet.full_text)
    #     try:
    #         print(tweet.entities["media"][0]["media_url_https"])
    #     except:
    #         pass


    
