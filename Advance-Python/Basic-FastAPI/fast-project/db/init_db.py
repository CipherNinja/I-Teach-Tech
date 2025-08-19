# init_db.py
from db.database import create_tables
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    create_tables()
    print("✅ Tables created.")
