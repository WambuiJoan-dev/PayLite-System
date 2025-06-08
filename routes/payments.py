# app/routes/payments.py
from flask import Blueprint, request, jsonify
from app.models import Payment, Sale
from app import db
from datetime import datetime, timedelta

payment_bp = Blueprint('payments', __name__)

# GET all payments
@payment_bp.route('/', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([
        {
            "id": p.id,
            "amount_paid": p.amount_paid,
            "date_paid": p.date_paid.isoformat(),
            "next_due_date": p.next_due_date.isoformat() if p.next_due_date else None,
            "sale_id": p.sale_id
        }
        for p in payments
    ])

# GET payments for a sale
@payment_bp.route('/sale/<int:sale_id>', methods=['GET'])
def get_payments_for_sale(sale_id):
    payments = Payment.query.filter_by(sale_id=sale_id).all()
    return jsonify([
        {
            "id": p.id,
            "amount_paid": p.amount_paid,
            "date_paid": p.date_paid.isoformat(),
            "next_due_date": p.next_due_date.isoformat() if p.next_due_date else None
        }
        for p in payments
    ])

# POST record payment
@payment_bp.route('/', methods=['POST'])
def record_payment():
    data = request.get_json()
    sale = Sale.query.get(data.get('sale_id'))

    if not sale:
        return jsonify({"error": "Invalid sale_id."}), 400

    # Create payment
    payment = Payment(
        amount_paid=data.get('amount_paid'),
        date_paid=datetime.utcnow(),
        next_due_date=datetime.utcnow() + timedelta(days=30),
        sale_id=sale.id
    )

    # Update sale balance_due and status
    sale.balance_due -= payment.amount_paid
    if sale.balance_due <= 0:
        sale.balance_due = 0
        sale.status = 'Completed'

    db.session.add(payment)
    db.session.commit()

    return jsonify({"message": "Payment recorded", "payment_id": payment.id}), 201
