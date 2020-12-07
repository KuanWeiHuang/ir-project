from elasticsearch import Elasticsearch

def load_datas():
    datas = list()
    with open('composers.txt', 'r') as f:
        for data in f.readlines():
            cid, link = data.replace('\n', '').split(';')
            datas.append(
                {
                    "cid": cid,
                    "link": link
                }
            )
    return datas

def create_data(es, datas):
    for data in datas:
        es.index(index='imslp', body=data)  

if __name__ == "__main__":
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    datas = load_datas()
    create_data(es, datas)