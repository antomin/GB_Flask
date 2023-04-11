class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://blog_db_user:blog_db_pass@pg:5432/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '54af6d270e2324ef7c21b1b7692af0297c3693867cff66307fbc7468205ae907'
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/docs'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///geekblog.db'


class TestingConfig(BaseConfig):
    TESTING = True
