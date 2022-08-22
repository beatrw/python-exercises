#Estudando manipulação de arquivos txt
#Módulo de sistema operacional e tal
import os

text = input('Digite seu texto: ')
#Criando o arquivo
arquivo = open(os.path.join('arquivos/aa.txt'), 'w')
#Gravando os dados
for palavra in text.split():
    arquivo.write(palavra + ' ')
arquivo.close

#Lendo o arquivo
arquivo = open('arquivos/aa.txt', 'r')
conteudo = arquivo.read()
arquivo.close
print(conteudo)

#Usando o with(método close é feito automaticamente)
with open ('arquivos/aa.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)