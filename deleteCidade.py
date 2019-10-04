import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["cidade"]

myquery = { "nome": "araraquara" }

mycol.delete_one(myquery)