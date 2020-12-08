from elasticsearch import Elasticsearch
import json

def get_query(userInput):
    query = {
        "query":{
            "bool":{
                "must":[
                    {
                        "match":{
                            "composer":"Beethoven Piano Concerto"
                        }
                    },
                    {
                        "match":{
                            "title":"Beethoven Piano Concerto"
                        }
                    }
                ]
            }
        },
        "from":0,
        "size":50,
        "sort":[],
        "aggs":{}
    }
    return query

if __name__ == "__main__":
    userInput = input("Search for works and composers: ")
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    query = get_query(userInput)
    result = es.search(index='imslp', body=query)
    print(json.dumps(result, ensure_ascii=False))