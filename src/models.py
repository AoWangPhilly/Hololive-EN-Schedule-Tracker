"""SQLAlchemy data models that represent a SQL table in the Hololive db, where the attributes of a model translate to columns in a table
"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import DateTime, TIMESTAMP
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.sql import func


from src.database import Base


class Idol(Base):
    __tablename__ = "idols"
    __table_args__ = (UniqueConstraint("author_id"),)

    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(BigInteger, nullable=False)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    icon_path = Column(String, nullable=False)


class TwitterPost(Base):
    __tablename__ = "twitter_posts"
    __table_args__ = (UniqueConstraint("twitter_post_id"),)

    id = Column(Integer, primary_key=True, nullable=False)
    twitter_post_id = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    text = Column(String, nullable=False)
    image_path = Column(String)
    youtube_link = Column(String)

    author_id = Column(
        BigInteger,
        ForeignKey(column="idols.author_id", ondelete="CASCADE"),
        nullable=False,
    )
    author = relationship("Idol")


class YouTubeIdol(Base):
    __tablename__ = "youtube_idols"
    __table_args__ = (UniqueConstraint("youtube_id"),)

    id = Column(Integer, primary_key=True, nullable=False)
    youtube_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    published_at = Column(TIMESTAMP(timezone=True), nullable=False)
    thumbnail = Column(String, nullable=False)


class YouTubeStatistic(Base):
    __tablename__ = "youtube_statistics"

    id = Column(Integer, primary_key=True, nullable=False)
    youtube_id = Column(
        String,
        ForeignKey(column="youtube_idols.youtube_id", ondelete="CASCADE"),
        nullable=False,
    )
    subscriber_count = Column(Integer, nullable=False)
    video_count = Column(Integer, nullable=False)
    view_count = Column(Integer, nullable=False)
    recorded_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    idol = relationship("YouTubeIdol")
