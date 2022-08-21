"""Programa que lê o nome completo de alguém e mostra:
- o nome com todas as letras maiúsculas,
- o nome com todas as letras minúsculas,
- quantas letras ao todo, sem considerar espaços
- quantas letras tem o primeiro nome
"""
nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')

tam = (len(nome) - nome.count(' '))
print(f'Total de letras: {tam}')

esp1 = nome.find(' ')
print(f'Primeiro nome "{(nome[:esp1])}" possui {len(nome[:esp1])} letras')


