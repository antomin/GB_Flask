from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from blog.extensions import db
from blog.models.article import article_tag_association_table


class Tag(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')

    def __str__(self):
        return self.name
