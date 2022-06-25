from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.sql.expression import null


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

    id = Column(Integer, primary_key=True, nullable=False)
    twitter_post_id = Column(BigInteger, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    text = Column(String, nullable=False)
    image_path = Column(String)
    youtube_link = Column(String)

    author_id = Column(
        Integer,
        ForeignKey(column="idols.author_id", ondelete="CASCADE"),
        nullable=False,
    )
    author = relationship("Idol")
