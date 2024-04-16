from sqlalchemy import String, Integer, Column, Text, DateTime
from datetime import datetime
from database.config import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,name='id', primary_key=True)
    title = Column(String(30), name='title', nullable=False)
    description = Column(Text, name='description', nullable=False)
    created_on = Column(DateTime, default=datetime.now())
    updated_on = Column(DateTime, default=datetime.now())