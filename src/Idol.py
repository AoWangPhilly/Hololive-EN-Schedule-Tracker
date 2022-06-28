from constants import (
    HOLOLIVE_EN_COUNCIL_TAGS,
    HOLOLIVE_EN_MYTH_TAGS,
    HOLOLIVE_EN_VSINGER_TAGS,
)
from util import connect_to_twitter
from database import get_db
import models


class Idol:
    @staticmethod
    def get_idol_info(screen_name: str) -> dict:
        api = connect_to_twitter()
        user = api.get_user(screen_name=screen_name)
        return {
            "author_id": user.id,
            "username": screen_name,
            "name": user.name,
            "icon_path": user.profile_image_url_https,
        }


def generate_holo_en_rule() -> str:
    hololive_tags = (
        HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
    )
    hololive_tag = [f"from:{tag}" for tag in hololive_tags]
    return " OR ".join(hololive_tag)


def store_all_idol_info_to_db() -> None:
    IDOLS = (
        HOLOLIVE_EN_COUNCIL_TAGS + HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS,
    )[0]

    db_gen = get_db()
    db = next(db_gen)
    for idol_screen_name in IDOLS:
        print(idol_screen_name)
        idol_info = Idol.get_idol_info(idol_screen_name)
        idol = models.Idol(**idol_info)
        db.add(idol)
        db.commit()
        db.refresh(idol)
        print(idol)
