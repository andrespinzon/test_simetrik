from sqlalchemy import Column, Integer, String, Date

from config.extension import Base


class Transaction(Base):
    __tablename__: str = 'transaction'

    transaction_id: str = Column(String, primary_key=True)
    transaction_date: Date = Column(Date)
    transaction_amount: int = Column(Integer)
    client_id: int = Column(Integer)
    client_name: str = Column(String)
