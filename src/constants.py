from config import settings

HOLOLIVE_EN_MYTH_TAGS = [
    "moricalliope",
    "takanashikiara",
    "ninomaeinanis",
    "gawrgura",
    "watsonameliaEN",
]

HOLOLIVE_EN_VSINGER_TAGS = ["irys_en"]

HOLOLIVE_EN_COUNCIL_TAGS = [
    "tsukumosana",
    "ceresfauna",
    "ourokronii",
    "nanashimumei_en",
    "hakosbaelz",
]

SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

TWITTER_FIELDS = "id,text,author_id,created_at,entities,referenced_tweets"
EXPANSIONS = "author_id,attachments.media_keys"
MEDIA_FIELDS = "duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text"
USER_FIELDS = "username,name"
