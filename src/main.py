import schedule
import time
from multiprocessing import Process

from src.database import engine
import src.models as models
from src.twitter import IdolListener
import src.youtube.YouTubeRunner as YouTubeRunner


def youtube_process():
    schedule.every().day.at("12:00").do(YouTubeRunner.run)

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    models.Base.metadata.create_all(engine)

    p1 = Process(target=youtube_process)
    p2 = Process(target=IdolListener.run)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
