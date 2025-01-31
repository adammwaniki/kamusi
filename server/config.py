import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    SQLALCHEMY_TRACK_MODIFICATIONS = False