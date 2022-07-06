from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
COMMON_DB=os.getenv('COMMON_DB')

class Config(object):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_BINDS = {
        'common_db' : COMMON_DB
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
