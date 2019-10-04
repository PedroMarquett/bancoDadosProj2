import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["linha"]

myquery = { "codigo": 1 }
newvalues = { "$set": { "nome": "Linha1" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)