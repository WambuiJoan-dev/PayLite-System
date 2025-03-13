from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import DateTime, relationship

Base = declarative_base

class Customer(Base):
    __tablename__ = 'customers'

    #one to many r/ship with sales
    id = Column(Integer(), Primary_key=True)
    name = Column(String())
    national_id = Column(Integer())
    credit_status = Column(String())

    sales = relationship("Sale", backref="customer")

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer(), Primary_key=True)
    brand = Column(String())
    model = Column(String())
    price = Column(Integer())
    stock_quantity = Column(Integer())

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer(), Primary_key=True)
    sale_id = Column(Integer(), ForeignKey('sale.id'))
    amount_paid = Column(Integer())
    date_paid = Column(Integer())
    next_due_date = Column(Integer())
 
class Sale(Base):
    __tablename__ = 'sales'

    #one to many(payments)
    total_price = Column(Integer())
    deposit_paid = Column(Integer())
    balance_due = Column(Integer())
    installment_amount = Column(Integer())
    status = Column(String())

    customer_id = Column(Integer(), ForeignKey('customer.id'))
    phone_id = Column(Integer(), ForeignKey('phone.id'))

    payments = relationship("Payment", backref="payment")