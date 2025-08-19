from sqlalchemy import Column, Integer, String
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,index=True, primary_key=True)
    f_name = Column(String,nullable=False)
    s_name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)