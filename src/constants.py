from config import settings

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

SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"