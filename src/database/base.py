from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",    
    host="localhost",
    port=5432,
    database="mixtapetech",
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()