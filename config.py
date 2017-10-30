import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #WTF_CSRF_ENABLED = True
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_FILE = 'scrud_dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.\
        format(Config.DB_USERNAME, Config.DB_PASSWORD, 'localhost', DATABASE_FILE)


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_FILE = 'scrud_dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.\
        format(Config.DB_USERNAME, Config.DB_PASSWORD, 'localhost', DATABASE_FILE)

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Set this to config['key'].  It sets the configuration in manage.py and app/__init__.py
conf = config['development']
