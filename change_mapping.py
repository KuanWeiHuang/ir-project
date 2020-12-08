from elasticsearch import Elasticsearch

def change_mappings(es):
    body = get_works_mappings()
    es.indices.put_mapping(index='imslp', body=body)

def get_works_mappings():
    mappings = {
        "properties": {
            "composer": {
                "type": "text"
            },
            "title": {
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
            "name": {
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