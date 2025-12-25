from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

data_url = "postgresql://postgres:admin123@localhost/new3"
engine = create_engine(data_url)
session = sessionmaker(bind=engine)
Base = declarative_base()
