from models import User, engine
from sqlalchemy.orm import sessionmaker
from utils.util import encode_token

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def login(username, password):
    """
    Authenticate a user and return a JWT token if credentials are valid.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        dict: A dictionary with a success message and token if authentication is successful, else an error message.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and user.check_password(password):
            token = encode_token(user.id, user.role)  
            return {"message": "Login successful", "token": token}
        else:
            return {"message": "Invalid username or password"}
    except Exception as e:
        return {"message": f"An error occurred: {e}"}
    finally:
        db.close()
