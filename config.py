import os

basedir = os.path.join(os.path.dirname(__file__))

##Condiguracion
class Config(object):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')or \
    'postgresql://postgres:76427740@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False