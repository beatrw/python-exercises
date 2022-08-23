# Trabalhando com bibliotecas
#Pacote de matemática
import math
from sqlite3 import Date
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é igual a {round(raiz, 2)}')
print(dir(math))

#Pacote de funções randômicas
import random
aleat = random.random()
print(aleat)

"""
#Emoji kkk
import emoji
print(emoji.emojize("Olá :thumbs_up:"))
"""

#Pacote para operações estatísticas
import statistics
list = [8, 5, 7]
#Média
print(statistics.mean(list))
print(statistics.median(list))

#Pacote para manipulação de datas
import datetime
agr = datetime.datetime.now()
print(agr)

