from elasticsearch import Elasticsearch
import json

def get_query():
    query = {
        "query": { 
            "match": {
                "composer": "Beethoven"
            }    
        }
    }
    return query

if __name__ == "__main__":
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    query = get_query()
    result = es.search(index='imslp', body=query)
    print(json.dumps(result, ensure_ascii=False))