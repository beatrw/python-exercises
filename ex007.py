#Programa que faz conversão de medidas

print('='*20, 'Conversor de medidas', '='*20)

valorm = float(input('Informe um valor em metros: '))
valorcm = valorm*100
valormm = valorm*1000
print(f'{valorm} metros equivale a {valorcm} centímetros e {valormm} milímetros.')

#ou:
#print(f'{valorm} metros equivale a {valorm*100} centímetros e {valorm*1000} milímetros.')
