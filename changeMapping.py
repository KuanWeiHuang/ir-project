from elasticsearch import Elasticsearch

def change_mappings(es):
    body = get_composers_mappings()
    es.indices.put_mapping(index='imslp', body=body)

def get_works_mappings():
    mappings = {
        "properties": {
            "title": {
                "type": "text"
            },
            "category": {
                "type": "text"
            },
            "composer": {
                "type": "text"
            },
            "worktitle": {
                "type": "text"
            },
            "link": {
                "type": "text"
            }
        }
    }
    return mappings

def get_composers_mappings():
    mappings = {
        "properties": {
            "cid": {
                "type": "text"
            },
            "link": {
                "type": "text"
            }
        }
    }

    return mappings

if __name__ == "__main__":
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    change_mappings(es)
    result = es.indices.get(index = 'imslp')
    print(result)
    result2 = es.indices.exists(index = 'imslp')
    print(result2)