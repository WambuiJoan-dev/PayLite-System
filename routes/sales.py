# app/routes/sales.py
from flask import Blueprint, request, jsonify
from app.models import Sale, Customer, Phone
from app import db

sale_bp = Blueprint('sales', __name__)

# GET all sales
@sale_bp.route('/', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    return jsonify([
        {
            "id": s.id,
            "total_price": s.total_price,
            "deposit_paid": s.deposit_paid,
            "balance_due": s.balance_due,
            "installment_amount": s.installment_amount,
            "status": s.status,
            "customer_id": s.customer_id,
            "phone_id": s.phone_id
        }
        for s in sales
    ])

# POST create new sale
@sale_bp.route('/', methods=['POST'])
def create_sale():
    data = request.get_json()

    # Validate customer and phone exist
    customer = Customer.query.get(data.get('customer_id'))
    phone = Phone.query.get(data.get('phone_id'))

    if not customer or not phone:
        return jsonify({"error": "Invalid customer_id or phone_id."}), 400

    # Check stock
    if phone.stock_quantity <= 0:
        return jsonify({"error": "Phone is out of stock."}), 400

    # Create sale
    total_price = phone.price
    deposit_paid = data.get('deposit_paid')
    balance_due = total_price - deposit_paid

    sale = Sale(
        total_price=total_price,
        deposit_paid=deposit_paid,
        balance_due=balance_due,
        installment_amount=data.get('installment_amount'),
        status='Ongoing',
        customer_id=customer.id,
        phone_id=phone.id
    )

    # Reduce stock
    phone.stock_quantity -= 1

    db.session.add(sale)
    db.session.commit()

    return jsonify({"message": "Sale created", "sale_id": sale.id}), 201
