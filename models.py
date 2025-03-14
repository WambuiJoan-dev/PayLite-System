from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime 


# paylite = 'sqlite.///PayLite.db'

Base = declarative_base()
# engine = create_engine(paylite)
# PayLite_engine = create_engine("sqlite:///PayLite.db")



#one to many r/ship with sales
class Customer(Base):    
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    national_id = Column(Integer())
    credit_status = Column(String())

    sales = relationship("Sale", back_populates="customer")

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer(), primary_key=True)
    brand = Column(String())
    model = Column(String())
    price = Column(Integer())
    stock_quantity = Column(Integer())

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer(), primary_key=True)
    amount_paid = Column(Integer())
    date_paid = Column(DateTime(), default=datetime.utcnow)
    next_due_date = Column(DateTime())

    sale_id = Column(Integer(), ForeignKey('sales.id'), nullable=False)
    sale = relationship("Sale", back_populates="payments")
 

 #one to many r/ship with payments
class Sale(Base):    
    __tablename__ = 'sales' 

    id = Column(Integer(), primary_key=True)
    total_price = Column(Integer())
    deposit_paid = Column(Integer())
    balance_due = Column(Integer())
    installment_amount = Column(Integer())
    status = Column(String())

    customer_id = Column(Integer(), ForeignKey('customers.id'))
    phone_id = Column(Integer(), ForeignKey('phones.id'))

    payments = relationship("Payment", back_populates="sales", cascade="all, delete-orphan")
    customer = relationship("Customer", back_populates="sales")
    phone = relationship("Phone", back_populates="sales")



PayLite_engine = create_engine("sqlite:///PayLite.db")
Base.metadata.create_all(PayLite_engine)


Session = sessionmaker(bind=PayLite_engine)
session = Session()    
