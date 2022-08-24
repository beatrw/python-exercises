#Calculadora bem simples

def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

print('-'*20,'Calculadora Python', '-'*20)

print('Informe qual operação deseja realizar:')
operacao = int(input('Soma - 1 | Subtração - 2 | Multiplicação - 3 | Divisão - 4\n'))
if operacao > 4:
    print('Opção inválida!')    
else:
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))

if operacao == 1:
    print(f'Soma = {soma(num1, num2)}')
elif operacao == 2:
    print(f'Subtração = {sub(num1, num2)}')
elif operacao == 3:
    print(f'Multiplicação = {mult(num1, num2)}')
elif operacao == 4:
    print(f'Divisão = {div(num1, num2)}')

