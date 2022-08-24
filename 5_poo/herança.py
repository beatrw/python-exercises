

#Super-classe
class Colaboradores():
    def __init__(self):
        print('Colaborador(a) cadastrado(a)')
    
    def identidade(self):
        print('Colaborador(a)')

#Sub-classe
class Vendedor():
    def __init__(self, nome, id):
        #Chamada da herança
        Colaboradores.__init__(self)
        self.nome = nome
        self.id = id
    
    def identidade(self):
        print('Vendedor(a)')

    def identificar(self):
        print(f'Vendendor(a): {self.nome} | ID: {self.id}')


ana = Vendedor('Ana', 334)
ana.identificar()
ana.identidade()
