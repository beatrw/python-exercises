"""Programa que lê algo e mostra:
- quantas vezes a letra A aparece
- em que posição aparece pela primeira vez
- em que posição aparece pela última vez
"""

algo = str(input('Digite algo: ')).upper().strip()
print(f'A letra A aparece {algo.count("A")} vezes na frase')
print(f'A primeira letra A está na posição: {algo.find("A")+1}')
print(f'A última letra A está na posição: {algo.rfind("A")+1}')

