from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String, Table,
                        Text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from blog.extensions import db

article_tag_association_table = Table(
    'article_tag_association',
    db.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tag.id'), nullable=False)
)


class Article(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(80), nullable=False)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __str__(self):
        return self.title
