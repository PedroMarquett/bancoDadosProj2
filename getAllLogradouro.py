import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["logradouro"]

mydoc = mycol.find()

for x in mydoc:
    print(x)