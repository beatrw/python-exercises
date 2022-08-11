#Programa que lê um número e mostra suas unidades, dezenas e centenas

numero = int(input('Digite um número: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cent = numero // 100 % 10
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')

