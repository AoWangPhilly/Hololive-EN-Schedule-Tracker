import tweepy
from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Idol:
    ...

def connect_to_twitter() -> tweepy.API:
    auth = tweepy.OAuthHandler(
        consumer_key=API_KEY, 
        consumer_secret=API_KEY_SECRET, 
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth)
    return api

if __name__ == "__main__":

    api = connect_to_twitter()
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    user = api.get_user(screen_name='moricalliope')
