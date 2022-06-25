from database import get_db, engine
import models
from pprint import pprint

if __name__ == "__main__":
    # models.Base.metadata.create_all(engine)

    # get_db()

    a = {
        "data": {
            "attachments": {"media_keys": ["16_1540395710331228161"]},
            "author_id": "1283646922406760448",
            "created_at": "2022-06-24T18:05:33.000Z",
            "entities": {
                "urls": [
                    {
                        "display_url": "pic.twitter.com/EKNJmPRSDH",
                        "end": 42,
                        "expanded_url": "https://twitter.com/takanashikiara/status/1540395721194516480/photo/1",
                        "media_key": "16_1540395710331228161",
                        "start": 19,
                        "url": "https://t.co/EKNJmPRSDH",
                    }
                ]
            },
            "id": "1540395721194516480",
            "text": "Kikkerikiiiiiiìiii https://t.co/EKNJmPRSDH",
        },
        "includes": {
            "media": [
                {
                    "height": 122,
                    "media_key": "16_1540395710331228161",
                    "preview_image_url": "https://pbs.twimg.com/tweet_video_thumb/FWCVvLfUEAEsMeQ.jpg",
                    "public_metrics": {},
                    "type": "animated_gif",
                    "width": 220,
                }
            ],
            "users": [
                {
                    "id": "1283646922406760448",
                    "name": "Takanashi Kiara🐔",
                    "username": "takanashikiara",
                }
            ],
        },
        "matching_rules": [{"id": "1539063278017585153", "tag": ""}],
    }
    pprint(a)
