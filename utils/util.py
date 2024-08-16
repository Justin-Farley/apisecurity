import os
import jwt
import datetime

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret_key')

def encode_token(user_id, role):
    """
    Generate a JWT token with an expiration time, user ID, and role as the payload.
    
    Args:
        user_id (int): The ID of the user.
        role (str): The role of the user.

    Returns:
        str: The generated JWT token.
    """
    try:
        payload = {
            'user_id': user_id,
            'role': role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    except Exception as e:
        print(f"Error encoding token: {e}")
        return None

def decode_token(token):
    """
    Decode a JWT token and return the payload if the token is valid.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The payload if the token is valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None
