import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["empresa"]

myquery = { "nome": "Empresa 1" }
newvalues = { "$set": { "nome": "Empresa1" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)