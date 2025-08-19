from pydantic import BaseModel, EmailStr

# For creating a new user
class User(BaseModel):
    f_name: str
    s_name: str
    email: EmailStr
    password: str

# For login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# For sending user data back (without password)
class UserOut(BaseModel):
    id: int
    f_name: str
    s_name: str
    email: EmailStr

    class Config:
        orm_mode = True
