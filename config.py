class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '54af6d270e2324ef7c21b1b7692af0297c3693867cff66307fbc7468205ae907'


class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///geekblog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False