#Programa que calcula descontos

print('='*20, 'Calcule o desconto de um produto!', '='*20)
valor = float(input('Informe o preço do produto: R$'))
desconto = float(input('Informe o desconto do produto: '))
valordesconto = valor*desconto/100
print(f'O valor do desconto é R${round(valordesconto)} e o produto passará a valer R${round(valor-valordesconto)}.')