"""SQLAlchemy data models that represent a SQL table in the Hololive db, where the attributes of a model translate to columns in a table
"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import DateTime, TIMESTAMP
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql import func
from src.database import Base


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
    __table_args__ = (UniqueConstraint("youtube_id"),)

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
