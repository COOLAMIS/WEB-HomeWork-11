from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    secondname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phonenumber = Column(String)
    birthday = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())




