from src.utils.config import settings

SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

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

TWITTER_FIELDS = (
    "id,text,author_id,created_at,entities,referenced_tweets,public_metrics"
)
EXPANSIONS = "author_id,attachments.media_keys"
MEDIA_FIELDS = "duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text"
USER_FIELDS = "username,name"

HOLOLIVE_EN_MYTH_YOUTUBE_ID = [
    "UCoSrY_IQQVpmIRZ9Xf-y93g",  # Gawr Gura
    "UCHsx4Hqa-1ORjQTh9TYDhww",  # Takanashi Kiara
    "UCL_qhgtOy0dy1Agp8vkySQg",  # Mori Calliope
    "UCMwGHR0BTZuLsmjY_NT5Pwg",  # Ninomae Ina'nis
    "UCyl1z3jo3XHR1riLFKG5UAg",  # Watson Amelia
]

HOLOLIVE_EN_COUNCIL_YOUTUBE_ID = [
    "UC3n5uGu18FoCy23ggWWp8tA",  # Nanashi Mumei
    "UCO_aKKYxn4tvrqPjcTzZ6EQ",  # Ceres Fauna
    "UCgmPnx-EEeOrZSg5Tiw7ZRQ",  # Hakos Baelz
    "UCmbs8T6MWqUHP1tIQvSgKrg",  # Ouro Kronii
    "UCsUj0dszADCGbF3gNrQEuSQ",  # Tsukumo Sana
]

HOLOLIVE_EN_VSINGER_YOUTUBE_ID = ["UC8rcEBzJSleTkf_-agPM20g"]  # IRyS
