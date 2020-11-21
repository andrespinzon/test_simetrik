from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer

from config.extension import Base


class File(Base):
    __tablename__: str = 'file'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime)

    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()
