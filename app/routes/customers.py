from flask import Blueprint, request, jsonify
from app.models import Customer
from app import db
from app.schemas import CustomerSchema
from flask_jwt_extended import jwt_required
from app.decorators import role_required

customer_bp = Blueprint('customers', __name__)
customer_schema = CustomerSchema()


@customer_bp.route('/', methods=['GET'])
@jwt_required()
def get_customers():
    customers = Customer.query.all()
    return jsonify(customer_schema.dump(customers, many=True))


@customer_bp.route('/<int:customer_id>', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found."}), 404

    return customer_schema.dump(customer)


@customer_bp.route('/', methods=['POST'])
@jwt_required()
def add_customer():
    data = customer_schema.load(request.get_json())
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return customer_schema.dump(customer), 201


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found."}), 404

    data = request.get_json()
    customer.name = data.get('name', customer.name)
    customer.national_id = data.get('national_id', customer.national_id)
    customer.credit_status = data.get('credit_status', customer.credit_status)

    db.session.commit()
    return customer_schema.dump(customer)


@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
@role_required('admin')
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found."}), 404

    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted", "customer_id": customer.id})
