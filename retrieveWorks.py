from imslp import client
import sys



# create a instance of ImslpClient
IC = client.ImslpClient

# get all works
results = IC.search_works(intersect = False)



# create a file imslp.txt to store data
sys.stdout = open("works.txt", "w")

# print(results)

# results is of type "set"
for val in results:
    l = list()
    for key, value in val.items():
        if key == "intvals":
            for k, v in value.items():
                l.append(k + ": " + v)
        else:
            l.append(key + ": " + value)
    print(l)

# close imslp.txt 
sys.stdout.close()