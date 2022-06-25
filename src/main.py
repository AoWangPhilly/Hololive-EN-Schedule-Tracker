from database import get_db, engine
import models
if __name__ == "__main__":
    models.Base.metadata.create_all(engine)

    get_db()