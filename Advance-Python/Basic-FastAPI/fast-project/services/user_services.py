from sqlalchemy.orm import Session
from models.users import User
from schema.user_schema import User as UserSchema, UserLogin
from utils.hash import hash_password, verify_password
from utils.jwt import create_access_token
from fastapi import HTTPException
from utils.hash import hash_password, verify_password
from utils.jwt import create_access_token
from fastapi import HTTPException

def register_user(user: UserSchema, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        f_name=user.f_name,
        s_name=user.s_name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# Create
def create_user(db: Session, user: UserSchema):
    new_user = User(
        f_name=User.f_name,
        s_name=User.s_name,
        email=User.email,
        password=User.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
def get_users(db: Session):
    return db.query(User).all()

# Get by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Delete
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

# Update
def update_user(db: Session, user_id: int, user_data: UserSchema):
    user = get_user_by_id(db, user_id)
    if user:
        user.f_name = user_data.f_name
        user.s_name = user_data.s_name
        user.email = user_data.email
        user.password = user_data.password
        db.commit()
        db.refresh(user)
    return user
