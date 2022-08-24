import sqlite3
import os

os.remove('arquivos/prt.db') if os.path.exists('arquivos/pdt.db') else None

conex = sqlite3.connect('arquivos/prt.db')

curs = conex.cursor()

#Usando função p criar tabela
def cria_tabl():
    curs.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,' \
        'prod_name TEXT, valor REAL)')

#Usando função pra inserir um dado(linha)
def inser_dados():
    curs.execute("INSERT INTO produtos VALUES(1,'24-08-22', 'mouse', 150)")
    conex.commit()
    curs.close()
    conex.close()

#Executando as funções
cria_tabl()
inser_dados()