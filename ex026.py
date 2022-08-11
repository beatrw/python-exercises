#Programa que recebe um nome completo e informa o primeiro e último nome

nome = str(input('Informe seu nome completo: ')).strip()
esp1 = nome.find(' ')
ultesp = nome.rfind(' ')
print(f'Primeiro nome: {(nome[:esp1])}')
print(f'Último nome:{(nome[ultesp:])}')

"""
outra forma:
n = nome.split
print(f'Primeiro nome: '{(nome[0])})
print(f'Último nome: {nome[len(nome)-1]}')
"""
