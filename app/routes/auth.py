from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User
from app import db
from marshmallow import Schema, fields, validate, ValidationError

auth_bp = Blueprint('auth', __name__)
login_schema = LoginSchema()

@auth_bp.route('/login', methods= ['POST'])
def login():
    try:
       
        data = login_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
       
        access_token = create_access_token(identity={"id": user.id, "role": user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401