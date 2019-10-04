import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["logradouro"]

myquery = { "codigo": 37 }
newvalues = { "$set": { "descricao": "Logradouro1" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)