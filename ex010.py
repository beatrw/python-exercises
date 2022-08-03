#Programa que calcula quantas latas de tinta são necessárias para pintar uma parede

print('='*20, 'Pinte sua parede!', '='*20)

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura*largura
tinta = area/2
print(f'A área da sua parede corresponde a {area}m².')
print(f'Você precisará de {tinta}l de tinta para pintá-la.')