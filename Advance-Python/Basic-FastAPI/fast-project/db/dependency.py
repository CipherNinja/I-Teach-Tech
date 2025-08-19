from db.database import sessionLocal
from fastapi import Depends
from sqlalchemy.orm import session

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()