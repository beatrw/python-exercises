
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números    
def ex1():
    for i in range(2,21,2):
        print(i)
ex1()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def ex2(strng):
    print(strng.upper())
ex2('aaa')


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
lis = [1,2,3,4]
def ex3(lis):
    lis.append(5)
    lis.append(6)
    print(lis)
ex3(lis)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def ex4(arg1, *vartuple):
    print(f'Item: {arg1}')
    for i in vartuple:
        print(f'Item: {i}')
ex4('aa')
ex4(1,'bb',3,4)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda x,y: x+y
print(soma(3,5))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
Celsius = [39.2, 36.5, 37.3, 37.8]
fr = map(lambda x: 1.8*x+32, Celsius)
print(list(fr))


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
dic = {1,2,3,4}
print(dir(dic))

print('-'*10)

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
import pandas as pd
print(dir(pd))

