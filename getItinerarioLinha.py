import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["linha"]

myquery = { "nome": "Linha1" }

mydoc = mycol.find(myquery)

for x in mycol.find({},{ "_id": 0, "itinerario": 1 }):
    print(x)