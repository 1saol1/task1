import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or os.getenv(
        "SQLALCHEMY_DATABASE_URI"
    )