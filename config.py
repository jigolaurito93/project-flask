import os

# os is the module system that we are on
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # It checks the environment and use the SECRET_KEY if not, use the alternative string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-random-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False