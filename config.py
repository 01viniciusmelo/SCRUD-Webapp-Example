import os
basedir = os.path.abspath(os.path.dirname(__file__))

# see iBooks Flask Web Development page 75 for source of this setup
#
# 'dev' uses db = investments_dev
# 'master' uses db = investments_dev
# 'production' uses db = investments
# master branch is the master of the development processs
# dev branch is the WIP development

class Config:
    # see ProgrammingNotes/terminal notes.txt for instructions to set environment variable
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
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


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_FILE = 'scrud_dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.\
        format(Config.DB_USERNAME, Config.DB_PASSWORD, 'localhost', DATABASE_FILE)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Set this to config['key'].  It sets the configuration in manage.py and app/__init__.py
conf = config['development']
