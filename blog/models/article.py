from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from blog.extensions import db


class Article(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(80), nullable=False)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    author = relationship('Author', back_populates='articles')
