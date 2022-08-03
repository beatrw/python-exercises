#Programa que converte temperatura

print('='*20, 'Conversor de temperatura', '='*20)
gc = int(input('Quantos graus celsius está fazendo? '))
fr = gc*1.8+32
kv = gc+273
print(f'{gc}°C equivale a {fr}°F e {kv}K')
