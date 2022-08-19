#Programa que lê os valores dos catetos de um triângulo e calcula a hipotenusa

import math
print('='*20, 'Calcule a sua hipotenusa', '='*20)
oposto = float(input('Quanto vale o cateto oposto? '))
adjacente = float(input('Quanto vale o cateto adjacente? '))
hipotenusa = math.hypot(oposto, adjacente)
print(f"A hipotenusa vale {round(hipotenusa, 2)}")
