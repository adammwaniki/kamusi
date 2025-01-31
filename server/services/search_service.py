class SearchService:
    def __init__(self, es_client):
        self.es = es_client
        self.index_name = 'swahili-dictionary'
    
    def search(self, query):
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["word^3", "translation^2", "examples"],
                    "fuzziness": "AUTO"
                }
            },
            "suggest": {
                "word_suggest": {
                    "prefix": query,
                    "completion": {
                        "field": "suggest",
                        "skip_duplicates": True
                    }
                }
            }
        }
        return self.es.search(index=self.index_name, body=body)