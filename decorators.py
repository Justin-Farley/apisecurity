from functools import wraps
from flask import request, jsonify
import jwt
from utils.util import decode_token

def role_required(required_role):
    """
    Decorator to check if the user has the required role.
    
    Args:
        required_role (str): The role required to access the resource.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"message": "Token is missing"}), 401
            
            try:
                payload = decode_token(token)
                if payload is None:
                    return jsonify({"message": "Invalid or expired token"}), 401
                
                user_role = payload.get('role')
                if user_role != required_role:
                    return jsonify({"message": "Access denied"}), 403

                return f(*args, **kwargs)
            except Exception as e:
                return jsonify({"message": f"An error occurred: {e}"}), 500

        return decorated_function

    return decorator
