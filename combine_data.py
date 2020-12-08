import sys

def load_composers(d):
    with open('composers.txt', 'r') as f:
        for data in f.readlines():
            name, link = data.replace('\n', '').split(';')
            d[name] = link

def combine(d):
    datas = []
    with open('works.txt', 'r') as f:
        for data in f.readlines():
            print(data)
            composer, title, link = data.replace('\n', '').split(' ; ')
            composer_link = "N/A"
            if composer in d:
                composer_link = d[composer]
            datas.append(" ; ".join([composer, title, link, composer_link]))
    return datas

def output(datas):
    sys.stdout = open("imslp.txt", "w")
    for data in datas:
        print(data)
    sys.stdout.close()


if __name__ == "__main__":
    dictionary = {}
    load_composers(dictionary)
    datas = combine(dictionary)
    output(datas)