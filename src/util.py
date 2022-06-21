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

def generate_holo_en_rule() -> str:
    hololive_tags = HOLOLIVE_EN_MYTH_TAGS + HOLOLIVE_EN_VSINGER_TAGS + HOLOLIVE_EN_COUNCIL_TAGS
    hololive_tag = [f"from:{tag}" for tag in hololive_tags]
    return " OR ".join(hololive_tag)