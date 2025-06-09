from flask import Blueprint, request, jsonify
from app.models import Sale, Customer, Phone
from app import db
from app.schemas import SaleSchema
from flask_jwt_extended  import jwt_required
from app.decorators import role_required

sale_bp = Blueprint('sales', __name__)
sale_schema = SaleSchema()


@sale_bp.route('/', methods=['GET'])
@jwt_required()
def get_sales():
    sales = Sale.query.all()
    return jsonify(sale_schema.dump(sales, many=True))


@sale_bp.route('/<int:sale_id>', methods=['GET'])
@jwt_required()
def get_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found."}), 404

    return sale_schema.dump(sale)


@sale_bp.route('/', methods=['POST'])
@jwt_required()
def create_sale():
    data = sale_schema.load(request.get_json())
    customer = Customer.query.get(data['customer_id'])
    phone = Phone.query.get(data['phone_id'])

    if not customer or not phone:
        return jsonify({"error": "Invalid customer_id or phone_id."}), 400

    if phone.stock_quantity <= 0:
        return jsonify({"error": "Phone is out of stock."}), 400

    total_price = phone.price
    deposit_paid = data['deposit_paid']
    balance_due = total_price - deposit_paid

    sale = Sale(
        total_price=total_price,
        deposit_paid=deposit_paid,
        balance_due=balance_due,
        installment_amount=data['installment_amount'],
        status='Ongoing',
        customer_id=customer.id,
        phone_id=phone.id
    )

    phone.stock_quantity -= 1

    db.session.add(sale)
    db.session.commit()

    return sale_schema.dump(sale), 201


@sale_bp.route('/<int:sale_id>', methods=['PUT'])
@jwt_required()
def update_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found."}), 404

    data = request.get_json()
    sale.status = data.get('status', sale.status)
    sale.balance_due = data.get('balance_due', sale.balance_due)

    db.session.commit()
    return sale_schema.dump(sale)


@sale_bp.route('/<int:sale_id>', methods=['DELETE'])
@role_required('admin')
def delete_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found."}), 404

    db.session.delete(sale)
    db.session.commit()
    return jsonify({"message": "Sale deleted", "sale_id": sale.id})
