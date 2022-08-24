import sqlite3
import os

#Remoção do db
os.remove('arquivos/escol.db') if os.path.exists('arquivos/escol.db') else None

#Criando conexão com bd (caso db não exista, será criado)
conex = sqlite3.connect('arquivos/escol.db')
print(type(conex))

#Cursor(para percorrer os registros no db)
curs = conex.cursor()
print(type(curs))

#Instruções SQL(criando a tabela)
com_sql = 'create table testes ' \
    '(id integer primary key, '\
    'nome varchar(100), '\
    'idade integer(2))'

#Executando a instrução:
curs.execute(com_sql)

#Inserindo registros
inser_sql = 'insert into testes values(?, ?, ?)'

#Dados p inserir
dads = [(1, 'Bibi', 22), 
        (2, 'Lala', 25), 
        (3, 'Papa', 37)]

#Inserindo os registros anteriores através do loop
for i in dads:
    curs.execute(inser_sql, i)

#Gravando/salvando a operação
conex.commit()

#Selecionando e mostrando os dados
selec_sql = 'select * from testes'

curs.execute(selec_sql)
#ou curs.execute ('select * from cursos')
dads = curs.fetchall() #Salvando todos os registros em dads

for linha in dads:
    print(linha)

#Fechando a conexão
conex.close()
