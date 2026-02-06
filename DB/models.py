from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from DB.database import Base
from sqlalchemy import Column


class DbUser(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DbArticle", back_populates="user")


class DbArticle(Base):
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)  
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("DbUser", back_populates="items")