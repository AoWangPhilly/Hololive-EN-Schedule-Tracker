from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null

class Idol(Base):
    __tablename__ = "idols"
    __table_args__ = (UniqueConstraint("author_id"),)

    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    icon_path = Column(String, nullable=False)

class TwitterPost(Base):
    __tablename__ = "twitter_posts"

    id = Column(Integer, primary_key=True, nullable=False)
    twitter_post_id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    twitter_text = Column(String, nullable=False)
    image_path = Column(String, nullable=False)
    youtube_link = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey(column="idols.author_id", ondelete="CASCADE"), nullable=False)
    author = relationship("Idol")

