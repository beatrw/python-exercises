
#Estudando tratamento de arquivos

#Abrindo o arquivo
arqv = open('arquivos/arq1.txt', 'r')

#Para ler o arquivo
print(arqv.read())

#Contar o número de caracteres
print(arqv.tell())

#Retornar para o início ou parte específica
print(arqv.seek(0,0))

#Para ler até x caractere
print(arqv.read(5))

#Gravando arquivos
#Abrindo arqv para gravação
arqv = open('arquivos/arq1.txt', 'w')

#Gravando no arquivo
arqv.write('Oioioioio')

#Para acrescentar conteúdo
arqv = open('arquivos/arq1.txt', 'a')
arqv.write('Acrescentanto')

#Fechando
arqv.close


arqv = open('arquivos/arq1.txt', 'r')
print(arqv.read())

"""
#Automatizando as gravações e tal
nomearq = input('Defina o nome do arquivo: ')
nomearq = nomearq + '.txt'

arq2 = open(nomearq, 'w')
arq2.write('Testando aq')

arq2.close

arq2 = open(nomearq, 'r')
print(arq2.read())
arq2.close
"""

"""
#Abrindo um dataset separado por linha (\n)
hein = open('arquivos/salarios.csv', 'r')
data = hein.read()
ln = data.split('\n')
print(ln)
"""

"""
#Abrindo dataset separado por colunas(,)
f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_roll = row.split(',')
    full_data.append(split_roll)
print(full_data)
"""

#Importando datasets com Pandas
import pandas as pd
file_name = "arquivos/binary.csv"
df = pd.read_csv(file_name)
print(df.head())

file_name2 = "arquivos/salarios.csv"
df2 = pd.read_csv(file_name2)
print(df2.head())

