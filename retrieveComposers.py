from imslp import client
import sys



# create a instance of ImslpClient
IC = client.ImslpClient

# get all composers in IMSLP
results = IC.search_people(name = None)


# create a file imslp.txt to store data
sys.stdout = open("composers.txt", "w")

# results is of type "set"
for val in results:
    l = []
    for key, value in val.items():
        if key != "id" and key != "permlink":
            continue
        # Eliminate "Category:" and "," in id
        if key == "id":
            value = value[value.find(":") + 1:].replace(",", "")
        l.append(value)
    print(";".join(l))

# close composers.txt 
sys.stdout.close()