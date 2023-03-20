from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from blog.extensions import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), unique=False, nullable=False)
    last_name = Column(String(80), unique=False, nullable=True)
    email = Column(String(150), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    author = relationship('Author', uselist=False, back_populates='user')

    def __repr__(self):
        return f'<User {self.id} {self.email}>'
