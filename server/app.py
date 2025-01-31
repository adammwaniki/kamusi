from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from config import Config
from services.search_service import SearchService

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
es = Elasticsearch(app.config['ELASTICSEARCH_URL'])
search_service = SearchService(es)

# Import routes after initializing to avoid circular imports
from routes import api

app.register_blueprint(api, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()