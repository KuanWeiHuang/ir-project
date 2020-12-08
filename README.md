# ir-project

Difference between text and keyword:
    text can be matched by substring
    keyword must be matched as a whole string


Create virtual environment: python3 -m venv venv
Change to virtual environment: source ./venv/bin/activate

* Run ElasticSearch
1. go to slasticsearch-7.10.0/bin and click on elasticsearch to run it
2. go to http://127.0.0.1:9200/ in browser to check if ES is working

* Create index of composers
1. run create_mapping.py to create mapping and setting
2. run load_composer.py to load data from composers.txt to index imslp

* Delete index
1. run: [curl "http://localhost:9200/_cat/indices?v&h=i"] to get all existing indexes
2. run: [curl -XDELETE "http://localhost:9200/imslp"] to delete index imslp

