import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["logradouro"]

myquery = { "codigo": 37 }

mycol.delete_one(myquery)