#Programa que lê um número real e mostra só a parte inteira

import math
num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e sua parte inteira é {math.trunc(num)}')

''' ou 
print(f'O valor digitado foi {num} e sua parte inteira é {int(num)}')
'''
