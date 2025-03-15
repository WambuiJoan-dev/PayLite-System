import click
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, PayLite_engine

Session = sessionmaker(bind=PayLite_engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Customer Name", help="Name of the customer")
@click.option("--national-id", prompt="National ID", type=int, help="National ID of the customer")
@click.option("--credit-status", prompt="Credit Status", type=click.Choice(['Active', 'Completed', 'Defaulted']), help="Credit status of the customer")
def add_customer(name, national_id, credit_status):
    """Add a new customer"""
    customer = Customer(name=name, national_id=national_id, credit_status=credit_status)
    session.add(customer)
    session.commit()
    click.echo(f"Customer '{name}' added successfully.")

if __name__ == "__main__":
    cli()
