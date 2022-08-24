#Estudando poo em python: classes e objetoss

class Dog():
    def __init__(self):
        self.raca = 'Viralat'
        self.cor = 'Caramelo'
    
    def imprime(self):
        print(f'Olha um dog: {self.raca}, {self.cor}')
    
dog1 = Dog()
dog1.imprime()

class Dog():
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor
    
    def imprime(self):
        print(f'Olha um dog: {self.raca}, {self.cor}')

dog2 = Dog('Puddle', 'branco')
dog2.imprime()

#Mudando um atributo
setattr(dog2, 'cor', 'rosa')
dog2.imprime()

#Buscando um atributo
print(getattr(dog2, 'cor'))

#Deletando atributo
print(delattr(dog2, 'cor'))
#dog2.imprime()

