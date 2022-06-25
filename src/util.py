from constants import (
    HOLOLIVE_EN_COUNCIL_TAGS,
    HOLOLIVE_EN_MYTH_TAGS,
    HOLOLIVE_EN_VSINGER_TAGS,
)


def generate_holo_en_rule() -> str:
    hololive_tags = (
        HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
    )
    hololive_tag = [f"from:{tag}" for tag in hololive_tags]
    return " OR ".join(hololive_tag)
