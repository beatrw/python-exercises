#Brincnado com métodos e atributos

class Circ():
    pi = 3.14

    def __init__(self, raio = 5):
        self.raio = raio
    
    def area(self):
        are = (self.raio * self.raio) * Circ.pi
        return are
    
    def setRaio(self, novoRaio):
        self.raio = novoRaio
    
    def getRaio(self):
        return self.raio

    #Chama em string
    def __str__(self):
        return f'Cículo com raio: {self.raio}'


circ1 = Circ(8)

print(circ1.getRaio())
print(circ1.area())
circ1.setRaio(10)
print(circ1)
print(f'O círculo tem raio {circ1.getRaio()} e área {circ1.area()}')


