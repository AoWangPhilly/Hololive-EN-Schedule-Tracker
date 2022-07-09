import schedule
import time
from multiprocessing import Process

from src.database import engine
import src.models as models
from src.twitter import IdolListener
from src.twitter.Idol import Idol
import src.youtube.YouTubeRunner as YouTubeRunner


def idol_metrics_process():
    schedule.every().day.at("06:00").do(YouTubeRunner.run)
    schedule.every().day.at("06:00").do(Idol.store_idol_metrics)

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    models.Base.metadata.create_all(engine)

    p1 = Process(target=idol_metrics_process)
    p2 = Process(target=IdolListener.run)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
