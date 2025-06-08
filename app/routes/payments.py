# app/routes/payments.py
from flask import Blueprint, request, jsonify
from app.models import Payment, Sale
from app import db
from app.schemas import PaymentSchema
from datetime import datetime, timedelta

payment_bp = Blueprint('payments', __name__)
payment_schema = PaymentSchema()


@payment_bp.route('/', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify(payment_schema.dump(payments, many=True))


@payment_bp.route('/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({"error": "Payment not found."}), 404

    return payment_schema.dump(payment)


@payment_bp.route('/sale/<int:sale_id>', methods=['GET'])
def get_payments_for_sale(sale_id):
    payments = Payment.query.filter_by(sale_id=sale_id).all()
    return jsonify(payment_schema.dump(payments, many=True))


@payment_bp.route('/', methods=['POST'])
def record_payment():
    data = payment_schema.load(request.get_json())
    sale = Sale.query.get(data['sale_id'])

    if not sale:
        return jsonify({"error": "Invalid sale_id."}), 400

    payment = Payment(
        amount_paid=data['amount_paid'],
        date_paid=datetime.utcnow(),
        next_due_date=datetime.utcnow() + timedelta(days=30),
        sale_id=sale.id
    )

    sale.balance_due -= payment.amount_paid
    if sale.balance_due <= 0:
        sale.balance_due = 0
        sale.status = 'Completed'

    db.session.add(payment)
    db.session.commit()

    return payment_schema.dump(payment), 201


@payment_bp.route('/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({"error": "Payment not found."}), 404

    sale = payment.sale
    sale.balance_due += payment.amount_paid
    if sale.status == 'Completed':
        sale.status = 'Ongoing'

    db.session.delete(payment)
    db.session.commit()
    return jsonify({"message": "Payment deleted", "payment_id": payment.id})
