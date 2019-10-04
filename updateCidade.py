import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["cidade"]

myquery = { "nome": "Araraquara" }
newvalues = { "$set": { "nome": "araraquara" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)