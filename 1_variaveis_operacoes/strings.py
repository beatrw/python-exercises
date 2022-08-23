#Trabalhando com strings

nome = 'Beatriz Aquino'
print(nome)
#Para escolher apenas uma letra:
print(nome[7])

#Para usar um intervalo:
print(nome[2:6])

#Pulando posições:
print(nome[0:7:2])

#Para começar do início sem precisar indicar:
print(nome[:7])

#Para ir até o final sem precisar indicar:
print(nome[8:])

#Para ir até o final pulando posições:
print(nome[8::2])

#----------------------------------------------------------------------
#Analisando a string:
#Tamanho:
print(len(nome))

#Para contar quantas vezes uma letra aparece:
print(nome.count('a'))

#Para contar quantas vezes uma letra aparece dentro de um intervalo:
print(nome.count('a', 0, 7))

#Para encontrar a posição(que começa) algo específico:
print(nome.find('triz'))

#Para saber se há algo específico (true/false):
print('Beatriz' in nome)

#----------------------------------------------------------------------
#Transformação com string:
#Mudando algo:
print(nome.replace('Beatriz', 'Bárbara'))

#Tornando tudo maiúsculo:
print(nome.upper())

#Tornando tudo minúsculo:
print(nome.lower())

#Apenas primeira letra maiúscula:
print(nome.capitalize())

#Cada palavra com inicial maiúscula:
print(nome.title())

#Remoção de espaços excedentes no início e final:
print(nome.strip())
#só no início ou no final usa a variação lstrip(left) ou rstrip(right)

#----------------------------------------------------------------------
#Divisão na string:
print(nome.split())

#Junção na string:
print('-'.join(nome))


#----------------------------------------------------------------------
#Outros
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pharetra sagittis mi ac maximus.
Nam facilisis posuere ante at congue. Etiam vitae fringilla nisi. 
Duis accumsan augue venenatis sem blandit, eu mollis ante hendrerit. 
Praesent pellentesque, urna eu congue tincidunt, nunc nisi blandit elit, non auctor purus leo non enim.
Integer et tortor vel metus sagittis consectetur.""")

#Como mudar de fato a string
nome2 = 'Beatriz Thiana'
nome2 = nome2.replace('Beatriz', 'Bárbara')
print(nome2)

#Busca ajustada
print(nome.lower().find('aquino'))

