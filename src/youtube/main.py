from decouple import config
import schedule
import time

from src.database import engine
from src.youtube.YouTubeStats import run
import src.youtube.models as youtube_models

if __name__ == "__main__":
    youtube_models.Base.metadata.create_all(engine)

    schedule.every().day.at("17:00").do(run)

    while True:
        schedule.run_pending()
        time.sleep(60)
