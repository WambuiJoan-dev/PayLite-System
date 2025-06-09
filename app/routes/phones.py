from flask import Blueprint, request, jsonify
from app.models import Phone
from app import db
from app.schemas import PhoneSchema
from flask_jwt_extended import jwt_required
from app.decorators import role_required

phone_bp = Blueprint('phones', __name__)
phone_schema = PhoneSchema()


@phone_bp.route('/', methods=['GET'])
@jwt_required()
def get_phones():
    phones = Phone.query.all()
    return jsonify(phone_schema.dump(phones, many=True))


@phone_bp.route('/<int:phone_id>', methods=['GET'])
@jwt_required()
def get_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if not phone:
        return jsonify({"error": "Phone not found."}), 404

    return phone_schema.dump(phone)

@phone_bp.route('/', methods=['POST'])
@jwt_required()
def add_phone():
    data = phone_schema.load(request.get_json())
    phone = Phone(**data)
    db.session.add(phone)
    db.session.commit()
    return phone_schema.dump(phone), 201


@phone_bp.route('/<int:phone_id>', methods=['PUT'])
@jwt_required()
def update_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if not phone:
        return jsonify({"error": "Phone not found."}), 404

    data = request.get_json()
    phone.price = data.get('price', phone.price)
    phone.stock_quantity = data.get('stock_quantity', phone.stock_quantity)

    db.session.commit()
    return phone_schema.dump(phone)


@phone_bp.route('/<int:phone_id>', methods=['DELETE'])
@role_required('admin')
def delete_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if not phone:
        return jsonify({"error": "Phone not found."}), 404

    db.session.delete(phone)
    db.session.commit()
    return jsonify({"message": "Phone deleted", "phone_id": phone.id})
