from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import URL

# DB_URL = URL.create()
engine = create_engine(url="sqlite:///db.sqlite3", echo=True)
Session = sessionmaker(bind=engine, autoflush=True, autocommit =False)
session = Session()
Base = declarative_base()