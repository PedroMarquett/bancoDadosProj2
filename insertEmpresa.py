import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]
mycol = mydb["empresa"]

myobj = {
    "nome": "Empresa 1",
    "endereco": "Avenida , 900",
    "telefone": "16 3333 2222",
    "site": "http://www.siteempresaum.com.br/",
    "linhas": [
        {
            "codigo": 1,
            "nome": "Linha1",
            "itinerario": [
                {
                    "codigo": 2,
                    "descricao": "Logradouro2"
                },
                {
                    "codigo": 3,
                    "descricao": "Logradouro1"
                }
            ],
            "quadroHorarios": {
                "diasUteis": ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"],
                "sabados": ["09:00", "11:00", "14:00", "17:00"],
                "domingos": ["08:00", "15:00", "22:00"],
                "feriados": ["08:30", "13:30", "18:30"]
            }
        },
        {
            "codigo": 3,
            "nome": "Linha1",
            "itinerario": [
                {
                    "codigo": 22,
                    "descricao": "Logradouro1"
                },
                {
                    "codigo": 15,
                    "descricao": "Log Ra Douro"
                }
            ],
            "quadroHorarios": {
                "diasUteis": ["06:00", "10:00", "12:00", "14:00", "16:00", "18:00"],
                "sabados": ["06:00", "11:00", "14:00", "17:00"],
                "domingos": ["06:00", "15:00", "22:00"],
                "feriados": ["06:30", "13:30", "18:30"]
            }
        }
    ]
}

x = mycol.insert_one(myobj)

print(x.inserted_id)