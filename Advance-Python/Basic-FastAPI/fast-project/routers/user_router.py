from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.dependency import get_db
from schema.user_schema import User as UserSchema, UserLogin, UserOut
import services.user_services as service

router = APIRouter(prefix="/users", tags=['Users'])

# ✅ Register
@router.post("/register", response_model=UserOut)
def register(user: UserSchema, db: Session = Depends(get_db)):
    return service.register_user(user, db)

# ✅ Login
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return service.login_user(user, db)

@router.post("/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return service.creater_user(db,user)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return service.get_users(db)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "User deleted"}

@router.put("/{user_id}")
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    updated_user = service.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
