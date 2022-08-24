# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
from functools import reduce

lista = [3,5,7]
pot = map(lambda x: x**3, lista)
print(list(pot))

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'Bla ble bli blo blu'.split()
resultado = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print (i)

# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
lista2 = [0, 1, 2, 3, 4]
qdr = map(lambda x: x**2, lista2)
cb = map(lambda x: x**3, lista2)
print(list(qdr))
print(list(cb))

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]
smlm = map(pow, listaA, listaB)
print(list(smlm))


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
print(list(filter((lambda x: x < 0), range(-5,5))))

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))

# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
listain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, item in enumerate(listain):
    if i > 5:
        print(i, item)