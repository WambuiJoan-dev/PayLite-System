from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_user = get_jwt_identity()
            if current_user['role'] != required_role:
                return jsonify({"error": f"Forbidden: {required_role} role required"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
