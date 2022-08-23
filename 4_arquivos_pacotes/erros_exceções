#Tratamento de erros e exceções

#Try e except
#Posso mudar a msg de erro etc(necessário saber o tipo do erro)
try:
    'a'+1
except TypeError:
    print('Não permitido')

#Usando o else e finally(que é sempre executado)
try: 
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('blbalba')
except IOError:
    print('Arquivo não encontrado e tal')
else:
    print('Contteúdo gravado')
    f.close()
finally:
    print('Finally hein!')
