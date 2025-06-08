# app/routes/phones.py
from flask import Blueprint, request, jsonify
from app.models import Phone
from app import db

phone_bp = Blueprint('phones', __name__)

# GET all phones
@phone_bp.route('/', methods=['GET'])
def get_phones():
    phones = Phone.query.all()
    return jsonify([
        {
            "id": p.id,
            "brand": p.brand,
            "model": p.model,
            "price": p.price,
            "stock_quantity": p.stock_quantity
        }
        for p in phones
    ])

# POST add new phone
@phone_bp.route('/', methods=['POST'])
def add_phone():
    data = request.get_json()
    phone = Phone(
        brand=data.get('brand'),
        model=data.get('model'),
        price=data.get('price'),
        stock_quantity=data.get('stock_quantity')
    )
    db.session.add(phone)
    db.session.commit()
    return jsonify({"message": "Phone added", "phone_id": phone.id}), 201

# PUT update phone stock or price
@phone_bp.route('/<int:phone_id>', methods=['PUT'])
def update_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if not phone:
        return jsonify({"error": "Phone not found."}), 404

    data = request.get_json()
    phone.price = data.get('price', phone.price)
    phone.stock_quantity = data.get('stock_quantity', phone.stock_quantity)

    db.session.commit()
    return jsonify({"message": "Phone updated", "phone_id": phone.id})

# DELETE phone
@phone_bp.route('/<int:phone_id>', methods=['DELETE'])
def delete_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if not phone:
        return jsonify({"error": "Phone not found."}), 404

    db.session.delete(phone)
    db.session.commit()
    return jsonify({"message": "Phone deleted", "phone_id": phone.id})
