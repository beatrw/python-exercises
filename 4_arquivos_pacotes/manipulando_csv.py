#Estudando manipulação de arquivos csv

#Módulo csv
import csv

#Criando/escrevendo
with open('arquivos/numeros.csv', 'w') as arquivo:
   writer = csv.writer(arquivo)
   writer.writerow(('Primeria', 'Segunda', 'Terceira'))
   writer.writerow((11,22,33))
   writer.writerow((55,66,77))

#Lendo os arquivos
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for i in leitor:
        print('Colunas:', len(i))
        print(i)

#Gerando uma lista com dados do arquivo
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
print(dados)

#Imprimir a partir de uma linha específica
for linha in dados[1:]:
    print(linha)
