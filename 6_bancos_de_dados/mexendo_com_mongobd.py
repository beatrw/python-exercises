#MongoDB = JSON | Pymongo = Dicionários
import imp
from turtle import pos
from pymongo import MongoClient
import datetime

#Conectando com banco
conex = MongoClient('localhost', 27017)

print(type(conex))

#Criando database
db = conex.cadastrodb

#Criando collection(que é tipo tabela)
collection = db.cadastrodb

#Inserindo elementos
post1 = {"codigo": "ID- 123", 
        "prod_name": "Mouse",
        "marca": "logitech",
        "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id

print(post_id)

post2 = {"codigo": "ID-553", 
        "prod_name": "Monitor",
        "marca": "acer",
        "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post2)
post_id.inserted_id

#Imprimindo - usando cursor
collection.find_one({"prod_name": "Monitor"})

for post in collection.find():
    print(post)

#Verificando o nome do banco 
print(db.name)

#Verificando as coleções(tabelas?) disponíveis
print(db.list_collection_names())
