# app/routes/customers.py
from flask import Blueprint, request, jsonify
from app.models import Customer
from app import db

customer_bp = Blueprint('customers', __name__)

@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([
        {"id": c.id, "name": c.name, "national_id": c.national_id, "credit_status": c.credit_status}
        for c in customers
    ])

@customer_bp.route('/', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer = Customer(
        name=data.get('name'),
        national_id=data.get('national_id'),
        credit_status=data.get('credit_status')
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify({"message": "Customer added", "id": customer.id}), 201
