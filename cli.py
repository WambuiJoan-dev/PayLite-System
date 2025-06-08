from app.models import Base, Customer, Phone, Payment, Sale, PayLite_engine, sessionmaker
from sqlalchemy.orm import configure_mappers
from datetime import datetime

# Configure the mappers
configure_mappers()

# Create the engine and session

Session = sessionmaker(bind=PayLite_engine)
session = Session()

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Customer Menu")
        print("2. Phone Menu")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            customer_menu()
        elif choice == "2":
            phone_menu()
        elif choice == "3":
            print("Exiting PayLite system...")
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu():
    while True:
        print("Customer Menu:")
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
            print("Byee...")
            break
        else:
            print("Invalid choice. Jaribu tena!.")

def create_customer():
    print("Creating a new customer:")
    name = input("Enter the name: ")
    national_id = int(input("Enter the national ID: "))
    credit_status = input("Enter the credit status (Active, Completed, Ongoing): ")

    customer = Customer(name=name, national_id=national_id, credit_status=credit_status)
    session.add(customer)
    session.commit()
    print("Customer created successfully.")

def view_customers():
    customers = session.query(Customer).all()
    if not customers:
        print("No customers found.")
    else:
        print("All customers:")
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, National ID: {customer.national_id}, Credit Status: {customer.credit_status}")

def update_customer():
    view_customers()
    customer_id = int(input("Enter the ID of the customer you want to update: "))
    customer = session.query(Customer).get(customer_id)
    if not customer:
        print("Customer not found.")
        return

    name = input(f"Enter the new name (current: {customer.name}): ")
    national_id = int(input(f"Enter the new national ID (current: {customer.national_id}): "))
    credit_status = input(f"Enter the new credit status (current: {customer.credit_status}): ")

    customer.name = name
    customer.national_id = national_id
    customer.credit_status = credit_status
    session.commit()
    print("Customer updated successfully.")

def delete_customer():
    view_customers()
    customer_id = int(input("Enter the ID of the customer you want to delete: "))
    customer = session.query(Customer).get(customer_id)
    if not customer:
        print("Customer not found.")
        return

    session.delete(customer)
    session.commit()
    print("Customer deleted successfully.")

def phone_menu():
    while True:
        print("Phone Menu:")
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
            print("Exiting phone menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def create_phone():
    print("Creating a new phone:")
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    price = int(input("Enter the price: "))
    stock_quantity = int(input("Enter the stock quantity: "))

    phone = Phone(brand=brand, model=model, price=price, stock_quantity=stock_quantity)
    session.add(phone)
    session.commit()
    print("Phone created successfully.")

def view_phones():
    phones = session.query(Phone).all()
    if not phones:
        print("No phones found.")
    else:
        print("All phones:")
        for phone in phones:
            print(f"ID: {phone.id}, Brand: {phone.brand}, Model: {phone.model}, Price: {phone.price}, Stock: {phone.stock_quantity}")

def update_phone():
    view_phones()
    phone_id = int(input("Enter the ID of the phone you want to update: "))
    phone = session.query(Phone).get(phone_id)
    if not phone:
        print("Phone not found.")
        return

    brand = input(f"Enter the new brand (current: {phone.brand}): ")
    model = input(f"Enter the new model (current: {phone.model}): ")
    price = int(input(f"Enter the new price (current: {phone.price}): "))
    stock_quantity = int(input(f"Enter the new stock quantity (current: {phone.stock_quantity}): "))

    phone.brand = brand
    phone.model = model
    phone.price = price
    phone.stock_quantity = stock_quantity
    session.commit()
    print("Phone updated successfully.")

def delete_phone():
    view_phones()
    phone_id = int(input("Enter the ID of the phone you want to delete: "))
    phone = session.query(Phone).get(phone_id)
    if not phone:
        print("Phone not found.")
        return

    session.delete(phone)
    session.commit()
    print("Phone deleted successfully.")

def main():
    main_menu()

if __name__ == "__main__":
    main()
