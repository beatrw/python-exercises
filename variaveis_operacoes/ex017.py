#Programa que calcula seno, cosseno e tangente de um ângulo

import math
print('='*20, 'Seno, cosseno e tangente', '='*20)
ang = float(input('Informe o ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O SENO de {ang}° é: {round(sen,2)}.')
print(f'O COSSENO de {ang}° é: {round(cos,2)}.')
print(f'A TANGENTE de {ang}° é: {round(tan,2)}.')