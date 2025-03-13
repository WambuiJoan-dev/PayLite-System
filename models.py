from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(Primary_key=True))
    name = Column(String())
    national_id = Column(Integer())
    credit_status = Column(String())