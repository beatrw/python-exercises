#Algumas funções úteis

#Map faz operação da função em cada elemento de uma lista(?)
Celsius = [39.2, 36.5, 37.3, 37.8]
fr = map(lambda x: 1.8*x+32, Celsius)
print(list(fr))

#Somando 2 listas c map
l1 = [1,5,3,9]
l2 = [2,5,2,1]
sm = list(map(lambda x,y: x+y, l1, l2))
print(sm)


#Reduce faz operações entre elementos de uma lista até que sobre apenas um
from functools import reduce
lis = [1,4,7]
def som(a,b):
    x = a+b
    return(x)
print(reduce(som, lis))

#Em lambda
smlm = reduce(lambda x,y: x+y, lis)
print(smlm)


#Filtro que retorna os valores verdadeiros
def verPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(list(filter(verPar, lis)))

print(list(filter(lambda x: x%2==0, lis)))


#List comprehention - função dentro de uma lista(?)
lister = [x for x in range(11) if x%2==0]
print(list)

#Incrível hein:
fh = [(1.8*temp+32) for temp in Celsius]
print(fh)

#Aninhadas
lc = [x**2 for x in[x**2 for x in range(11)]]
print(lc)

#Zip - unir duas sequências e retorna tuplas considerando apenas o menor resultado
a = [1,2,3]
b = [4,5,6,7]
print(list(zip(a,b)))

#Enumerate - enumera uma sequência, atribui índices
sequencia = [1,2,3,4]
print(list(enumerate(sequencia)))
sequencia2 = ['Inglês', 'Espanhol', 'Francês']
for i, item in enumerate(sequencia2):
    print(i, item)