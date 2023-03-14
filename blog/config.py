class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '54af6d270e2324ef7c21b1b7692af0297c3693867cff66307fbc7468205ae907'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///geekblog.db'


class TestingConfig(BaseConfig):
    TESTING = True
