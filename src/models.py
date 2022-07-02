"""SQLAlchemy data models that represent a SQL table in the Hololive db, where the attributes of a model translate to columns in a table
"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.sql.expression import null

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
