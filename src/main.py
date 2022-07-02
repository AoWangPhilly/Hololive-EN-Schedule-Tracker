from src.database import engine
import src.models as models
from src.twitter import IdolListener

if __name__ == "__main__":
    models.Base.metadata.create_all(engine)
    IdolListener.run()
