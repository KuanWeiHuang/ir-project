from imslp import client
import sys



# create a instance of ImslpClient
IC = client.ImslpClient

# get all works
results = IC.search_works(intersect = False)



# create a file imslp.txt to store data
sys.stdout = open("works.txt", "w")


# skip id, type and parent later
not_include = set(['id', 'type', 'parent'])

# results is of type "set"
for val in results:
    l = list()
    for key, value in val.items():
        if key in not_include:
            continue
        if key == "intvals":
            for k, v in value.items():
                if k == 'icatno' or k == 'pageid':
                    continue
                if k == 'composer':
                    v = v.replace(",", "")
                l.append(v)
        else:
            l.append(value)
    print(" ; ".join(l))

# close works.txt 
sys.stdout.close()

# Fasch Johann Friedrich ; Gloria in Excelsis Deo ; https://imslp.org/wiki/Gloria_in_Excelsis_Deo_(Fasch,_Johann_Friedrich)