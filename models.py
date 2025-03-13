from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(Primary_key=True))
    name = Column(String())
    national_id = Column(Integer())
    credit_status = Column(String())

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer(Primary_key=True))
    brand = Column(String())
    model = Column(String())
    price = Column(Integer())
    stock_quantity = Column(Integer())

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer(Primary_key=True))

class Sale(Base):
    __tablename__ = 'sales'
    