#Programa que ordena randomicamente uma lista

import random
print('='*20, 'Ordenação randômica de alunos', '='*20)
aluno1 = input('Informe o nome do aluno 1: ')
aluno2 = input('Informe o nome do aluno 2: ')
aluno3 = input('Informe o nome do aluno 3: ')
aluno4 = input('Informe o nome do aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
ordenacao = random.shuffle(lista)
print(f'A ordenação será: {lista}')