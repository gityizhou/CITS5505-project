import os
from datetime import timedelta

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'


class TestingConfig(Config):
    SECRET_KEY = "zxc47POI"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'unittest.db')
                                             + '?check_same_thread=False')


class DevelopmentConfig(Config):
    SECRET_KEY = "zxc47POI"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'animevote.db')
                                             + '?check_same_thread=False')


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
}