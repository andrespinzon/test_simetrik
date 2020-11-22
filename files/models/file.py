from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer

from config.extension import Base


class File(Base):
    __tablename__: str = 'file'

    name: str = Column(String, primary_key=True)
    created_at: datetime = Column(DateTime)
