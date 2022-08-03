#Programa que faz conversão de moedas

print('='*20, 'Conversor de moedas :)', '='*20)

valor = float(input('Insira um valor em real para conversão: R$'))
dolar = valor/5.30
euro = valor/5.37
print(f'Valor em dólar: ${round(dolar,2)}.')
print(f'Valor em euro: €{round(euro,2)}.')

#Ainda não sei como restringir a quantidade de casas decimais nesse formato de print