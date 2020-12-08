from elasticsearch import Elasticsearch
import json


def create_index(es):
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_imslp_mappings() # mapping can be changed according to the data 
    print(json.dumps(body))
    es.indices.create(index='imslp', body=body)


def get_setting():
    settings = {
        "index": {
            "number_of_shards": 3,
            "number_of_replicas": 1
        }
    }

    return settings

def get_composers_mappings():
    mappings = {
        "properties": {
            "name": {
                "type": "text"
            },
            "link": {
                "type": "text"
            }
        }
    }
    return mappings

def get_imslp_mappings():
    mappings = {
        "properties": {
            "composer": {
                "type": "text"
            },
            "composerlink": {
                "type": "text"
            },
            "title": {
                "type": "text"
            },
            "titlelink": {
                "type": "text"
            }
        }
    }
    return mappings


if __name__ == "__main__":
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    create_index(es)
    result = es.indices.get(index = 'imslp')
    print(result)
    result2 = es.indices.exists(index = 'imslp')
    print(result2)