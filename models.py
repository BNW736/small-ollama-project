from database import Base
from sqlalchemy import Column, Integer, String


class data(Base):
    __tablename__ = "new"
    id = Column(Integer , primary_key=True)
    prompt = Column(String)
    responce1 = Column(String)
    data=Column(String)
