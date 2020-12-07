from elasticsearch import Elasticsearch
import json

def get_query():
    query = {
        "query": {
            "bool": {
                "must": {
                    "term": {
                        "age": 20
                    }
                }
            }
        }
    }
    return query

if __name__ == "__main__":
    es = Elasticsearch(hosts='192.168.1.59', port=9200)
    query = get_query()
    result = es.search(index='school', body=query)
    print(json.dumps(result, ensure_ascii=False))