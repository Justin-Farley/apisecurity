from models import User, engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def create_user(username, password, role):
    user = User(username=username, role=role)
    user.set_password(password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(username):
    return db.query(User).filter(User.username == username).first()


if __name__ == "__main__":
   
    new_user = create_user('john_doe', 'secure_password123', 'admin')
    print(new_user)

   
    user = get_user_by_username('john_doe')
    if user and user.check_password('secure_password123'):
        print("Password is correct.")
    else:
        print("Invalid password.")
