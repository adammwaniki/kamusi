# scripts/create_indexes.py
from elasticsearch import Elasticsearch
from config import Config
from services.search_service import SearchService

def create_es_index():
    es = Elasticsearch(Config.ELASTICSEARCH_URL)
    search_service = SearchService(es)
    
    if not es.indices.exists(index=search_service.index_name):
        es.indices.create(
            index=search_service.index_name,
            body=search_service.get_index_definition()
        )
        print("Elasticsearch index created!")
    else:
        print("Index already exists")

if __name__ == '__main__':
    create_es_index()