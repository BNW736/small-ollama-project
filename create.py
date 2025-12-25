import logging
from database import engine
from models import Base
logging.info("new")
Base.metadata.drop_all(bind=engine)
print("start")
Base.metadata.create_all(bind=engine)
print("Done")
