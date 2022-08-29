#Usando funções para manipulação de banco de dados

import sqlite3
import os
import random
import time
import datetime
#Pacote para trabalhar com gráficos
import matplotlib.pyplot as plt

os.remove('arquivos/prt.db') if os.path.exists('arquivos/pdt.db') else None

conex = sqlite3.connect('arquivos/prt.db')

curs = conex.cursor()

#Usando função p criar tabela
def cria_tabl():
    curs.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')

#Usando função pra inserir um dado(linha)
def inser_dados():
    curs.execute("INSERT INTO produtos VALUES(9, '24-08-22', 'mouse', 150)")
    curs.execute("INSERT INTO produtos VALUES(10, '25-08-22', 'teclado', 60)")
    curs.execute("INSERT INTO produtos VALUES(11, '25-08-22', 'carregador', 80)")
    conex.commit()
    
#Inserindo dados com variáveis ** Nao ta rodando esse ** 
def inser_dados_var():
    novaData = datetime.datetime.now()
    novoNomeProd = 'Teclado'
    novoValor = random.randrange(50, 100)
    curs.execute("INSERT INTO produtos VALUES(?,?,?,?)", (5, novaData, novoNomeProd, novoValor))
    conex.commit()

#Leitura de todos os dados
def mostrar_tudo():
    curs.execute("SELECT * FROM produtos")
    for linha in curs.fetchall():
        print(linha)

#Leitura de registros específicos
def leit_valor():
    curs.execute("SELECT * FROM produtos WHERE valor > 60.0")
    for linha in curs.fetchall():
        print(linha)

#Leitura de colunas específicas
def leit_col():
    curs.execute("SELECT * FROM produtos")
    for linha in curs.fetchall():
        print(linha[3])

#Atualizando um valor
def update():
    curs.execute("UPDATE produtos SET valor = 70.00 WHERE valor = 150.00")
    conex.commit()

#Removendo um valor - Nesse caso removendo tudo
def remov():
    curs.execute("DELETE FROM produtos")
    conex.commit()

#Gerando um gráfico
#Crio listas vazias para armazenar os valores das células
def graf():
    curs.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = curs.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
    #Criando um gráfico de barras - ele só n vai mostrar aqui(n sei pq tbkk)
    plt.bar(ids, valores)
    plt.show


#Fechando a conexão
def fech_conex():
    curs.close()
    conex.close()


#Executando as funções
cria_tabl()
remov()
inser_dados()

#Mostrando dados
mostrar_tudo()

update()
mostrar_tudo()
graf()

#Encerrando conexão
fech_conex()
