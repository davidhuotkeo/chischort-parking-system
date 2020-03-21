from datetime import timedelta

class Config:
    SECRET_KEY = b"4\x12\x19\x80\xf9\x16\xea\xb9G\x91\t\xd8S\x83\x16\x16"
    SQLALCHEMY_DATABASE_URI = "mysql://root:Davidhuotkeo123@localhost/chischort"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=365)

class DevConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = "development"

class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    ENV = "production"
    SQLALCHEMY_POOL_RECYCLE = 299
