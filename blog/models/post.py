from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from blog.models.database import db
from blog.models.user import User


class Post(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=True, nullable=False)
    text = Column(String(), unique=True, nullable=False)
    author = Column(Integer, ForeignKey(User.id))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Post {self.id} {self.title}>'
