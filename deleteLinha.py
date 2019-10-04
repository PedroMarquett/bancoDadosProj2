import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["linha"]

myquery = { "codigo": 1 }

mycol.delete_one(myquery)