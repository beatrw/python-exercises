#Programa que calcula aluguel de um carro

print('='*20, 'Aluguel de carro', '='*20)
dias = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos km rodados? '))
preco = dias*60+km*0.15
print(f'O valor total a pagar pelo aluguel é: R$ {preco}')