import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    DEBUG = True
    SQLALCHEMY_ECHO = True
class Product(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False