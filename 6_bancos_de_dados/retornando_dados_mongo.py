from itertools import count
import pymongo

#Conectando
conex = pymongo.MongoClient()

#Verificando as tabelas
print(conex.list_database_names())

#Defino a tabela que quero usar, de acordo com a lista que veio
db = conex.cadastrodb

#Listo as coleções disponíveis nessa database
print(db.list_collection_names())

"""
#Crio uma coleção
db.create_collection("newcoll")
print(db.list_collection_names())
"""

"""
#Inserindo doc na nova coleção
db.newcoll.insert_one({
    "Nome": "Bibi", 
    "Idade": "pouca",
    "XP": "20000",})
"""
print(db.newcoll.find_one())

#Conectando direto a uma coleção
col = db["newcoll"]

#Imprimindo umas coisas
print(type(col))
print(col.count_documents)

#Pegando um único doc
doc1 = col.find_one()
print(doc1)
