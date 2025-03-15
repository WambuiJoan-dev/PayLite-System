PayLIte-System
This is a Cli based A Mobile Phone Credit (Lipa Mdogo-Mdogo) System which will be used for tracking phone sales, installment payments, and customer records to ensure smooth credit management.
The CLI provides the following functionality:

 Customer Management:
   - Create new customers
   - View all customers
   - Update customer information
   - Delete customers

 Phone Management:
   - Create new phones
   - View all phones
   - Update phone information
   - Delete phones

  Sale Management:
   - Create new sales
   - View all sales
   - Update sale information
   - Delete sales

Data Model
Uses SQLAlchemy ORM to define a relational database with the following models:

Customer:

Fields=> id, name, national_id, credit_status

Relationships: One-to-many with Sales.

Phone:

Fields => id, brand, model, price, stock_quantity

Relationships: One-to-many with Sales.

Sale:

Fields => id, total_price, deposit_paid, balance_due, installment_amount, status, customer_id, phone_id

Relationships: One-to-many with Payments.

Payment:

Fields => id, amount_paid, date_paid, next_due_date, sale_id


File Structure:

- `cli.py`: The main entry point for the CLI, containing the menu and function definitions.
- `models.py`: Defines the database models for customers, phones, sales, and payments.

