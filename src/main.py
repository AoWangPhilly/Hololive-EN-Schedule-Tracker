from typing import Any
from database import get_db, engine
import models
from pprint import pprint


def clean_data(dirty_json: dict[str, Any]) -> dict[str, Any]:
    cleaned_dict = {}
    data = dirty_json.get("data")
    includes = dirty_json.get("includes")

    if data is None:
        print("Bad connection?? Missing data key!")
        print("-" * 150)
        print(dirty_json)
    else:
        cleaned_dict["author_id"] = data["author_id"]
        cleaned_dict["created_at"] = data["created_at"]
        cleaned_dict["twitter_post_id"] = data["id"]
        cleaned_dict["text"] = data["text"]

        if includes is None:
            print("Missing includes Key!!")
            print("-" * 150)
            print(dirty_json)
        else:
            cleaned_dict["image_path"] = includes["media"][0]["preview_image_url"]
            for user in includes["users"]:
                if user["id"] == cleaned_dict["author_id"]:
                    cleaned_dict["username"] = user["username"]
                    cleaned_dict["name"] = user["name"]

    return cleaned_dict


if __name__ == "__main__":
    # models.Base.metadata.create_all(engine)

    # get_db()

    # a = {
    #     "data": {
    #         "attachments": {"media_keys": ["16_1540395710331228161"]},
    #         "author_id": "1283646922406760448",
    #         "created_at": "2022-06-24T18:05:33.000Z",
    #         "entities": {
    #             "urls": [
    #                 {
    #                     "display_url": "pic.twitter.com/EKNJmPRSDH",
    #                     "end": 42,
    #                     "expanded_url": "https://twitter.com/takanashikiara/status/1540395721194516480/photo/1",
    #                     "media_key": "16_1540395710331228161",
    #                     "start": 19,
    #                     "url": "https://t.co/EKNJmPRSDH",
    #                 }
    #             ]
    #         },
    #         "id": "1540395721194516480",
    #         "text": "Kikkerikiiiiiiìiii https://t.co/EKNJmPRSDH",
    #     },
    #     "includes": {
    #         "media": [
    #             {
    #                 "height": 122,
    #                 "media_key": "16_1540395710331228161",
    #                 "preview_image_url": "https://pbs.twimg.com/tweet_video_thumb/FWCVvLfUEAEsMeQ.jpg",
    #                 "public_metrics": {},
    #                 "type": "animated_gif",
    #                 "width": 220,
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "id": "1283646922406760448",
    #                 "name": "Takanashi Kiara🐔",
    #                 "username": "takanashikiara",
    #             }
    #         ],
    #     },
    #     "matching_rules": [{"id": "1539063278017585153", "tag": ""}],
    # }

    b = {
        "data": {
            "attachments": {},
            "author_id": "1363705980261855232",
            "created_at": "2022-06-25T06:29:10.000Z",
            "entities": {},
            "id": "1540582858745851904",
            "text": "Recording hell really do be hell for my throat😵\u200d💫 "
            "discussed with my manager to try to hold back on streaming "
            "/ using voice during this period so today will be rest "
            "day_(:3 」∠)_",
        },
        "includes": {
            "users": [
                {
                    "id": "1363705980261855232",
                    "name": "IRyS💎holoEN ✨INTERNET OVERDOSE✨",
                    "username": "irys_en",
                }
            ]
        },
        "matching_rules": [{"id": "1539063278017585153", "tag": ""}],
    }
    pprint(clean_data(b))
