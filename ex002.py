#Concatenando uma msg que pergunte e mostre o nome do usuário
nome = input('Qual é o seu nome? ')
print(f'Seja bem vindo, {nome} !')

#Dissecando uma variável
algo = input("Digite algo: ")
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É tudo minúscilo? {algo.islower()}')
print(f'É apenas números? {algo.isnumeric()}')
print(f'É tudo maiúscilo? {algo.isupper()}')

#Somando números com variáveis
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print(f'A soma entre {n1} e {n2} vale {s}') #o f aqui faz a função do .format

