from sqlalchemy import Column, String, Text

from core.model import BaseModel


class Post(BaseModel):
    __tablename__ = 'post'
    title = Column(String(128))
    body = Column(Text)