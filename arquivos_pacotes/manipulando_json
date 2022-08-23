#Estudando manipulação de arquivos json
#Módulo json
import json

dic = {'Nome': 'Bibi', 'Linguagem': 'Python', 'Nota:': 10}
for i,j in dic.items():
    print(i,j)

#Convertendo o dicionário p jason
json.dumps(dic)

#Criando arquivo json
with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dic))

#Lendo arquivo json
with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)
print(data['Nome'])

#Json da net
"""
from urllib.request import urlopen
response = urlopen(URL AQUI).read().decode('utf8')
data = json.load(response)[0]
"""

#Copiando conteúdo json p txt
import os
fonte = 'arquivos/dados.json'
destino = 'arquivos/json_data.txt'

with open(fonte, 'r') as infile:
    text = infile.read()
    with open(destino, 'w') as outfile:
        outfile.write(text)

#open(destino, 'w').write(open(fonte, 'r').read())

with open('arquivos/json_data.txt', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)

