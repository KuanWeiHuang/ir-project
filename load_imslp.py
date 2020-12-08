from elasticsearch import Elasticsearch

def load_datas():
    datas = list()
    with open('imslp.txt', 'r') as f:
        for data in f.readlines():
            composer, title, titlelink, composerlink = data.replace('\n', '').split(' ; ')
            datas.append(
                {
                    "composer": composer,
                    "composerlink": composerlink,
                    "title": title,
                    "titlelink": titlelink
                }
            )
    return datas

def create_data(es, datas):
    counter = 0
    for data in datas:
        counter += 1
        es.index(index='imslp', body=data)  
        print(counter)

if __name__ == "__main__":
    es = Elasticsearch(hosts='127.0.0.1', port=9200)
    datas = load_datas()
    create_data(es, datas)