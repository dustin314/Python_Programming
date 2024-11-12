import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '73cdcb13b533e923f8e32a7586971c3f'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/dbbook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False