#Programa que lê o nome de uma cidade e mostra se começa ou não com Santo

cidade = input(str('Informe o nome da sua cidade: ')).strip()
esp1 = cidade.find(' ')
print('santo' in cidade[:esp1].lower())
