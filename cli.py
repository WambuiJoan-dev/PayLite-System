from models import Base, Customer, Phone, Sale, PayLite_engine, sessionmaker
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
        print("3. Sale Menu")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            customer_menu()
        elif choice == "2":
            phone_menu()
        elif choice == "3":
            sale_menu()
        elif choice == "4":
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

# Customer-related functions (create_customer, view_customers, update_customer, delete_customer)

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

# Phone-related functions (create_phone, view_phones, update_phone, delete_phone)

def sale_menu():
    while True:
        print("Sale Menu:")
        print("1. Create a new sale")
        print("2. View all sales")
        print("3. Update a sale")
        print("4. Delete a sale")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            update_sale()
        elif choice == "4":
            delete_sale()
        elif choice == "5":
            print("Exiting sale menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def create_sale():
    print("Creating a new sale:")
    total_price = int(input("Enter the total price: "))
    deposit_paid = int(input("Enter the deposit paid: "))
    balance_due = int(input("Enter the balance due: "))
    installment_amount = int(input("Enter the installment amount: "))
    status = input("Enter the status: ")
    customer_id = int(input("Enter the customer ID: "))
    phone_id = int(input("Enter the phone ID: "))

    customer = session.query(Customer).get(customer_id)
    phone = session.query(Phone).get(phone_id)

    if not customer or not phone:
        print("Customer or phone not found.")
        return

    sale = Sale(total_price=total_price, deposit_paid=deposit_paid, balance_due=balance_due,
                installment_amount=installment_amount, status=status, customer=customer, phone=phone)
    session.add(sale)
    session.commit()
    print("Sale created successfully.")

def view_sales():
    sales = session.query(Sale).all()
    if not sales:
        print("No sales found.")
    else:
        print("All sales:")
        for sale in sales:
            print(f"ID: {sale.id}, Total Price: {sale.total_price}, Deposit Paid: {sale.deposit_paid}, "
                  f"Balance Due: {sale.balance_due}, Installment Amount: {sale.installment_amount}, "
                  f"Status: {sale.status}, Customer: {sale.customer.name}, Phone: {sale.phone.brand} {sale.phone.model}")

def update_sale():
    view_sales()
    sale_id = int(input("Enter the ID of the sale you want to update: "))
    sale = session.query(Sale).get(sale_id)
    if not sale:
        print("Sale not found.")
        return

    total_price = int(input(f"Enter the new total price (current: {sale.total_price}): "))
    deposit_paid = int(input(f"Enter the new deposit paid (current: {sale.deposit_paid}): "))
    balance_due = int(input(f"Enter the new balance due (current: {sale.balance_due}): "))
    installment_amount = int(input(f"Enter the new installment amount (current: {sale.installment_amount}): "))
    status = input(f"Enter the new status (current: {sale.status}): ")

    sale.total_price = total_price
    sale.deposit_paid = deposit_paid
    sale.balance_due = balance_due
    sale.installment_amount = installment_amount
    sale.status = status
    session.commit()
    print("Sale updated successfully.")

def delete_sale():
    view_sales()
    sale_id = int(input("Enter the ID of the sale you want to delete: "))
    sale = session.query(Sale).get(sale_id)
    if not sale:
        print("Sale not found.")
        return

    session.delete(sale)
    session.commit()
    print("Sale deleted successfully.")

def main():
    main_menu()

if __name__ == "__main__":
    main()
