import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["empresa"]

myquery = { "nome": "Empresa um" }

mycol.delete_one(myquery)