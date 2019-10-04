import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["linha"]

myquery = { "nome": "HorarioLinha" }

mydoc = mycol.find(myquery)

for x in mycol.find({},{ "_id": 0, "quadroHorarios": 1 }):
    print(x)