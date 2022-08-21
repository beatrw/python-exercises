#Programa que calcula reajuste salarial

print('='*20, 'Calcule reajuste salarial!', '='*20)
salario = float(input('Quanto você ganha? R$'))
novo = float(input('Qanto será o reajuste? '))
reajuste = salario*novo/100
print(f'O valor do reajuste é de R${round(reajuste)} e o seu salário passará a valer R${round(salario+reajuste)}.')
