from app import app, db
from app.models import User, Customer, Phone, Sale, Payment
from datetime import datetime, timedelta

with app.app_context():
    #db.drop_all()
    db.create_all()

    admin = User(username='Jane', role="admin")
    admin.set_password('Jane@1')

    phone1 = Phone(brand="Techno", model="Camon 18", price=18000, stock_quantity=35)
    phone2 = Phone(brand="Samsung", model="Galaxy S21", price=80000, stock_quantity=20)

    customer1 = Customer(name="Ann Masinde", national_id="12345678", credit_status="Active")
    customer2 = Customer(name="Jacob Njuguna", national_id="87654321", credit_status="Defaulted")

    sale1 = Sale(
        customer=customer1,
        phone=phone1,
        total_price=18000,
        deposit_paid=3000,
        balance_due=15000,
        installment_amount=3000,
        status="Ongoing"
    )

    payment1 = Payment(
        amount_paid=3000,
        sale=sale1,
        date_paid=datetime.utcnow(),
        next_due_date=datetime.utcnow() + timedelta(days=30)
    )

    db.session.add_all([admin, phone1, phone2, customer1, customer2, sale1, payment1])
    db.session.commit()

    print("Database seeded successfully.")
    