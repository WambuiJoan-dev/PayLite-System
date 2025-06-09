# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from app.models import Customer, Phone, Payment, Sale, User
from app.schemas import CustomerSchema, PhoneSchema, SaleSchema, PaymentSchema
from app import create_app, db
from marshmallow import ValidationError
from sqlalchemy.orm import configure_mappers
from datetime import datetime, timedelta

configure_mappers()

application = create_app()
application.app_context().push()

session = db.session

customer_schema = CustomerSchema()
phone_schema = PhoneSchema()
sale_schema = SaleSchema()
payment_schema = PaymentSchema()

current_user = None  



def start():
    global current_user

    while True:
        print("\nWelcome to PayLite!")
        print("1. Login")
        print("2. Create an account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            current_user = login_user()
            if current_user:
                print(f"\nLogged in as '{current_user.username}' (Role: {current_user.role})")
                main_menu
            #if current_user:
                #print(f"\nLogged in as '{current_user.username}' (Role: {current_user.role})")
                #main_menu()
            
        elif choice == "2":
            create_user()
        elif choice == "3":
            print("Exiting PayLite system...")
            break
        else:
            print("Invalid choice. Please try again.")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = User.query.filter_by(username=username).first()
    if not user:
        print("User not found.")
        return None

    if user.check_password(password):
        return user
    else:
        print("Invalid password.")
        return None



def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Customer Menu")
        print("2. Phone Menu")
        print("3. Sales Menu")
        print("4. Payments Menu")
        print("5. User Menu")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            customer_menu()
        elif choice == "2":
            phone_menu()
        elif choice == "3":
            sales_menu()
        elif choice == "4":
            payments_menu()
        elif choice == "5":
            user_menu()
        elif choice == "6":
            print(f"Logging out '{current_user.username}'...")
            break
        else:
            print("Invalid choice. Please try again.")



def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Create a new user")
        print("2. View all users")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def create_user():
    print("\nCreating a new user:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/user): ").strip().lower()

    if role not in ["admin", "user"]:
        print("Invalid role. Must be 'admin' or 'user'.")
        return

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print("User already exists.")
        return

    user = User(username=username, role=role)
    user.set_password(password)
    session.add(user)
    session.commit()
    print(f"User '{username}' created successfully with role '{role}'.")

def view_users():
    users = User.query.all()
    if not users:
        print("No users found.")
    else:
        print("All users:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Role: {user.role}")



def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Create a new customer")
        print("2. View all customers")
        print("3. Update a customer")
        print("4. Delete a customer")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_customer():
    print("\nCreating a new customer:")
    name = input("Enter the name: ")
    national_id = input("Enter the national ID (8 digits): ")
    credit_status = input("Enter the credit status (Active, Completed, Defaulted): ")

    customer_data = {
        "name": name,
        "national_id": national_id,
        "credit_status": credit_status
    }

    try:
        data = customer_schema.load(customer_data)
        customer = Customer(**data)
        session.add(customer)
        session.commit()
        print("Customer created successfully.")
    except ValidationError as err:
        print("Error adding customer:")
        print(err.messages)

def view_customers():
    customers = Customer.query.all()
    if not customers:
        print("No customers found.")
    else:
        print("All customers:")
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, National ID: {customer.national_id}, Credit Status: {customer.credit_status}")

def update_customer():
    view_customers()
    customer_id = int(input("Enter the ID of the customer you want to update: "))
    customer = Customer.query.get(customer_id)
    if not customer:
        print("Customer not found.")
        return

    name = input(f"Enter the new name (current: {customer.name}): ")
    national_id = input(f"Enter the new national ID (current: {customer.national_id}): ")
    credit_status = input(f"Enter the new credit status (current: {customer.credit_status}): ")

    customer_data = {
        "name": name,
        "national_id": national_id,
        "credit_status": credit_status
    }

    try:
        data = customer_schema.load(customer_data)
        customer.name = data["name"]
        customer.national_id = data["national_id"]
        customer.credit_status = data["credit_status"]
        session.commit()
        print("Customer updated successfully.")
    except ValidationError as err:
        print("Error updating customer:")
        print(err.messages)

def delete_customer():
    if current_user.role != "admin":
        print("Only admins can delete payments.")
        return

    view_customers()
    customer_id = int(input("Enter the ID of the customer you want to delete: "))
    customer = Customer.query.get(customer_id)
    if not customer:
        print("Customer not found.")
        return

    session.delete(customer)
    session.commit()
    print("✅ Customer deleted successfully.")

def phone_menu():
    while True:
        print("\nPhone Menu:")
        print("1. Create a new phone")
        print("2. View all phones")
        print("3. Update a phone")
        print("4. Delete a phone")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_phone()
        elif choice == "2":
            view_phones()
        elif choice == "3":
            update_phone()
        elif choice == "4":
            delete_phone()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_phone():
    print("\nCreating a new phone:")
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    price = input("Enter the price: ")
    stock_quantity = input("Enter the stock quantity: ")

    phone_data = {
        "brand": brand,
        "model": model,
        "price": price,
        "stock_quantity": stock_quantity
    }

    try:
        data = phone_schema.load(phone_data)
        phone = Phone(**data)
        session.add(phone)
        session.commit()
        print("Phone created successfully.")
    except ValidationError as err:
        print("Error adding phone:")
        print(err.messages)

def view_phones():
    phones = Phone.query.all()
    if not phones:
        print("No phones found.")
    else:
        print("All phones:")
        for phone in phones:
            print(f"ID: {phone.id}, Brand: {phone.brand}, Model: {phone.model}, Price: {phone.price}, Stock: {phone.stock_quantity}")

def update_phone():
    view_phones()
    phone_id = int(input("Enter the ID of the phone you want to update: "))
    phone = Phone.query.get(phone_id)
    if not phone:
        print("Phone not found.")
        return

    brand = input(f"Enter the new brand (current: {phone.brand}): ")
    model = input(f"Enter the new model (current: {phone.model}): ")
    price = input(f"Enter the new price (current: {phone.price}): ")
    stock_quantity = input(f"Enter the new stock quantity (current: {phone.stock_quantity}): ")

    phone_data = {
        "brand": brand,
        "model": model,
        "price": price,
        "stock_quantity": stock_quantity
    }

    try:
        data = phone_schema.load(phone_data)
        phone.brand = data["brand"]
        phone.model = data["model"]
        phone.price = data["price"]
        phone.stock_quantity = data["stock_quantity"]
        session.commit()
        print("Phone updated successfully.")
    except ValidationError as err:
        print("Error updating phone:")
        print(err.messages)

def delete_phone():
    if current_user.role != "admin":
        print("Only admins can delete payments.")
        return

    view_phones()
    phone_id = int(input("Enter the ID of the phone you want to delete: "))
    phone = Phone.query.get(phone_id)
    if not phone:
        print("Phone not found.")
        return

    session.delete(phone)
    session.commit()
    print("Phone deleted successfully.")



def sales_menu():
    while True:
        print("\nSales Menu:")
        print("1. Create a new sale")
        print("2. View all sales")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def create_sale():
    print("\nCreating a new sale:")
    view_customers()
    customer_id = input("Enter customer ID: ")
    view_phones()
    phone_id = input("Enter phone ID: ")
    deposit_paid = input("Enter deposit paid: ")
    installment_amount = input("Enter installment amount: ")

    phone = Phone.query.get(phone_id)
    if not phone:
        print("Invalid phone selected.")
        return

    total_price = phone.price
    balance_due = total_price - int(deposit_paid)

    sale_data = {
        "total_price": total_price,
        "deposit_paid": deposit_paid,
        "balance_due": balance_due,
        "installment_amount": installment_amount,
        "status": "Ongoing",
        "customer_id": customer_id,
        "phone_id": phone_id
    }

    try:
        data = sale_schema.load(sale_data)
        sale = Sale(**data)
        phone.stock_quantity -= 1
        session.add(sale)
        session.commit()
        print("Sale created successfully.")
    except ValidationError as err:
        print("Error adding sale:")
        print(err.messages)

def view_sales():
    sales = Sale.query.all()
    if not sales:
        print("No sales found.")
    else:
        print("All sales:")
        for sale in sales:
            print(f"Sale ID: {sale.id}, Customer ID: {sale.customer_id}, Phone ID: {sale.phone_id}, Balance Due: {sale.balance_due}, Status: {sale.status}")



def payments_menu():
    while True:
        print("\nPayments Menu:")
        print("1. Record a payment")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            record_payment()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def record_payment():
    print("\nRecording a payment:")
    view_sales()
    sale_id = input("Enter sale ID: ")
    amount_paid = input("Enter amount paid: ")

    next_due_date = datetime.utcnow() + timedelta(days=30)

    payment_data = {
        "amount_paid": amount_paid,
        "date_paid": datetime.utcnow(),
        "next_due_date": next_due_date,
        "sale_id": sale_id
    }

    try:
        data = payment_schema.load(payment_data)
        payment = Payment(**data)

        sale = Sale.query.get(sale_id)
        sale.balance_due -= int(amount_paid)
        if sale.balance_due <= 0:
            sale.balance_due = 0
            sale.status = "Completed"

        session.add(payment)
        session.commit()
        print("Payment recorded successfully.")
    except ValidationError as err:
        print("Error recording payment:")
        print(err.messages)

def main():
    start()

if __name__ == "__main__":
    main()