from sqlalchemy import Column, String, Boolean

from db.base import ModelBase


class Quote(ModelBase):

    kr_content = Column(String, nullable=True)
    en_content = Column(String, nullable=True)
    author = Column(String, nullable=True)
    is_custom = Column(Boolean, default=False)


class Article(ModelBase):

    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    author = Column(String, nullable=True)
