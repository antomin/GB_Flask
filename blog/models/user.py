from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from blog.models.database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User {self.id} {self.username}>'
