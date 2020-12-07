from imslp import client
import sys



# create a instance of ImslpClient
IC = client.ImslpClient

# get all composers in IMSLP
results = IC.search_people(name = None)


# create a file imslp.txt to store data
sys.stdout = open("imslp.txt", "w")

# results is of type "set"
for val in results:
    l = list()
    for key, value in val.items():
        if key == "intvals":
            continue
        l.append(key + ": " + value)
    print(l)

# close imslp.txt 
sys.stdout.close()