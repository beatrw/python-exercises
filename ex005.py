#Programa que recebe um número e mostra seu dobro, triplo e raiz quadrada

import math

print('='*20, 'Dobro, triplo e raiz quadrada', '='*20)

num = int(input('Digite um número: '))
print(f'O dobro de {num} é {num*2}.')
print(f'O triplo de {num} é {num*3}.')
print(f'A raiz quadrade de {num} é {round(math.sqrt(num),2)}.')
