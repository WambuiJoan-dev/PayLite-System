import os
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Phone, Payment, Sale, PayLite_engine

Session = sessionmaker(bind=PayLite_engine)
session = Session()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("Welcome to the PayLite System CLI!")
    print("Please select an option:")
    print("1. Customers")
    print("2. Phones")
    print("3. Payments")
    print("4. Sales")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def customer_menu():
    while True:
        clear_screen()
        print("Customer Menu:")
        print("1. Create Customer")
        print("2. Delete Customer")
        print("3. View All Customers")
        print("4. View Customer Sales")
        print("5. Find Customer by National ID")
        print("6. Back to Main Menu")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            view_all_customers()
        elif choice == "4":
            view_customer_sales()
        elif choice == "5":
            find_customer_by_national_id()
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def create_customer():
    clear_screen()
    print("Create a new customer:")
    name = input("Enter customer name: ")
    national_id = int(input("Enter national ID: "))
    credit_status = input("Enter credit status (Active, Completed, Ongoing): ")

    if credit_status not in ['Active', 'Completed', 'Ongoing']:
        print("Invalid credit status. Please try again.")
        input("Press Enter to continue...")
        return

    customer = Customer(name=name, national_id=national_id, credit_status=credit_status)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' created successfully.")
    input("Press Enter to continue...")

def delete_customer():
    clear_screen()
    print("Delete a customer:")
    national_id = int(input("Enter national ID of the customer to delete: "))

    customer = session.query(Customer).filter_by(national_id=national_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer '{customer.name}' deleted successfully.")
    else:
        print(f"No customer found with national ID {national_id}.")
    input("Press Enter to continue...")

def view_all_customers():
    clear_screen()
    print("All Customers:")
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"Name: {customer.name}, National ID: {customer.national_id}, Credit Status: {customer.credit_status}")
    input("Press Enter to continue...")

def view_customer_sales():
    clear_screen()
    print("View Customer Sales:")
    national_id = int(input("Enter national ID of the customer: "))
    customer = session.query(Customer).filter_by(national_id=national_id).first()
    if customer:
        print(f"Customer: {customer.name}")
        for sale in customer.sales:
            print(f"Sale ID: {sale.id}, Total Price: {sale.total_price}, Deposit Paid: {sale.deposit_paid}, Balance Due: {sale.balance_due}, Installment Amount: {sale.installment_amount}, Status: {sale.status}")
    else:
        print(f"No customer found with national ID {national_id}.")
    input("Press Enter to continue...")

def find_customer_by_national_id():
    clear_screen()
    print("Find Customer by National ID:")
    national_id = int(input("Enter national ID: "))
    customer = session.query(Customer).filter_by(national_id=national_id).first()
    if customer:
        print(f"Name: {customer.name}, National ID: {customer.national_id}, Credit Status: {customer.credit_status}")
    else:
        print(f"No customer found with national ID {national_id}.")
    input("Press Enter to continue...")

def main():
    while True:
        choice = display_menu()
        if choice == "1":
            customer_menu()
        elif choice == "2":
            # Implement phone-related functionality
            pass
        elif choice == "3":
            # Implement payment-related functionality
            pass
        elif choice == "4":
            # Implement sale-related functionality
            pass
        elif choice == "5":
            print("Exiting PayLite System CLI...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
