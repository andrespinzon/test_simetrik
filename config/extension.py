from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from django.conf import settings

engine = create_engine(settings.DB_EXTERNAL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
