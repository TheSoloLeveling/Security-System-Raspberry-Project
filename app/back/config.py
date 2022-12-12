from decouple import config
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS',cast=bool)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///dev.db"  # + os.path.join(BASE_DIR, 'dev.db')
    DEBUG=True

    #for developing
    SQLALCHEMY_ECHO=True


class ProdConfig(Config):
    pass
    #SQLALCHEMY_DATABASE_URI="sqlite:///dev.db"
    #DEBUG=config('DEBUG',cast=bool)
    #SQLALCHEMY_ECHO=config('ECHO',cast=bool)
    #SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS',cast=bool)

class TestConfig(Config):
    pass
    #SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
    #SQLALCHEMY_ECHO=False
    #TESTING=True