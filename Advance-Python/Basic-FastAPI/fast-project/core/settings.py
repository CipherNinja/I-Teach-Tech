from dotenv import load_dotenv
import os
load_dotenv()

class Setting:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

settings = Setting()