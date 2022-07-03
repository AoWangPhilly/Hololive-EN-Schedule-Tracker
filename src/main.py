from src.database import engine
import src.twitter.models as twitter_models
from src.twitter import IdolListener

if __name__ == "__main__":
    twitter_models.Base.metadata.create_all(engine)

    IdolListener.run()
