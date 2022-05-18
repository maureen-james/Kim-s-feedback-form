import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:maureen@localhost/feedback'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}