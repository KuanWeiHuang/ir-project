from elasticsearch import Elasticsearch
from music import Music
import json

def get_query(userInput):
    query = {
        "query":{
            "bool":{
                "should":[
                    {
                        "simple_query_string":{
                            "query": userInput,
                            "fields": [
                                "composer^2",
                                "title^1"
                            ]
                        }
                    }
                ]
            }
        },
        "from":0,
        "size":100,
        "sort":[],
        "aggs":{}
    } 
    return query

def search_query(userInput):
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    query = get_query(userInput)
    result = es.search(index='imslp', body=query)
    count = result["hits"]["total"]["value"]
    resultlist = []
    for entry in result["hits"]["hits"]:
        data = entry["_source"]
        resultlist.append(Music(data["composer"], data["composerlink"], data["title"], data["titlelink"]))
    return count, resultlist


if __name__ == "__main__":
    userInput = input("Search for works and composers: ")
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    query = get_query(userInput)
    result = es.search(index='imslp', body=query)
    count = result["hits"]["total"]["value"]
    print("count", count)
    resultlist = []
    for entry in result["hits"]["hits"]:
        data = entry["_source"]
        resultlist.append(Music(data["composer"], data["composerlink"], data["title"], data["titlelink"]))
    # return resultlist