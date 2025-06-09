from app import db
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    national_id = db.Column(db.String(20))
    credit_status = db.Column(
        db.String(20),
        CheckConstraint("credit_status IN ('Active','Completed','Defaulted')")
    )
    
    sales = relationship("Sale", back_populates="customer")

class Phone(db.Model):
    __tablename__ = 'phones'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    price = db.Column(db.Integer)
    stock_quantity = db.Column(db.Integer)
    
    sales = relationship("Sale", back_populates="phone")

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    amount_paid = db.Column(db.Integer)
    date_paid = db.Column(db.DateTime, default=datetime.utcnow)
    next_due_date = db.Column(db.DateTime)
    
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    sale = relationship("Sale", back_populates="payments")

class Sale(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
    deposit_paid = db.Column(db.Integer)
    balance_due = db.Column(db.Integer)
    installment_amount = db.Column(db.Integer)
    status = db.Column(
        db.String(20),
        CheckConstraint("status IN ('Ongoing', 'Completed', 'Defaulted')")
    )
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'))
    
    payments = relationship("Payment", back_populates="sale", cascade="all, delete-orphan")
    customer = relationship("Customer", back_populates="sales")
    phone = relationship("Phone", back_populates="sales")
