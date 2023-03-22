from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from blog.extensions import db


class Author(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
