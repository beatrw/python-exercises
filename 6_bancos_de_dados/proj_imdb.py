#Projeto analisando dados do IMDB

from ctypes.wintypes import PLARGE_INTEGER
from email import header
import imp
import re
import time
import sqlite3
#Pycountry pra transformar de iso pra normal o nome de países
import pycountry
#Pack lindo da análise da dados kk
import numpy as np
import pandas as pd
#---------
#Para visualização de dados
import matplotlib as plt
import seaborn as sns
#----------
from matplotlib import cm
#Pacote machine learning
from sklearn.feature_extraction.text import CountVectorizer
import warnings
#Ignorando warnings e definindo estilo dos gráficos
warnings.filterwarnings("ignore")
#Fundo branco com linha
sns.set_theme(style="whitegrid")

#Conectando com o banco
conex = sqlite3.connect("arquivos/imdb.db")

#Extraindo lista de tabelas
tabelas = pd.read_sql_query("SELECT NAME AS 'table_name' FROM sqlite_master WHERE type = 'table'", conex)

print(type(tabelas))

print(tabelas.head())

#Convertendo o datafram numa lista pra percorrer dps
tabelas = tabelas["table_name"].values.tolist()

#Agr percorrendo pra pegar o esquema de cada tbela
#Até pra saber o que procurar
for tabela in tabelas:
    consulta = "PRAGMA TABLE_INFO({})".format(tabela)
    resultado = pd.read_sql_query(consulta, conex)
    print('Esquema da tabela:', tabela)
    print(resultado)
    print('-'*100)
    print('/n')


#Pquena análise exploratória

#---------------------1 - Categorias de fimles mais comuns no IMDB---------------------------

#Consulta
consulta1 = '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type'''

#Pegando o resultado
resultado1 = pd.read_sql_query(consulta1, conex)

#Visualizando o resultado
print(resultado1)

#Calculando o percentual de cada tipo
#Cda elemento dividido pelo total, mult por 100
resultado1['percentual'] = (resultado1['COUNT'] / resultado1['COUNT']. sum()) * 100

#Visualizando resultado calculado
print(resultado1)


#Criando gráfico(4 categorias)
#Categorias com mais títulos e categoria com o resto

#Criando dicionário vazio
outros = {}

#Filtrando percent em 5% e somando total
outros['COUNT'] = resultado1[resultado1['percentual'] < 5]['COUNT'].sum()

#Gravando percentual
outros['percentual'] = resultado1[resultado1['percentual'] < 5]['percentual'].sum()

#Ajustando o nome
outros['type'] = 'outros'

print(outros)


#Filtrando o dataframe d resultado
resultado1 = resultado1[resultado1['percentual'] < 5]

#Append com o dataframe das outras categorias
resultado1 = resultado1.append(outros, ignore_index= True)

#Ordenando o resultado
resultado1 = resultado1.sort_values(by = 'COUNT', ascending= False)

print(resultado1.head)

#Ajustando os labels 
labels = [str(resultado1['type'][i])+' '+'['+str(round(resultado1['percentual'][i],2)) +'%'+']' for i in resultado1.index]

#Criando gráfico
#Mapa de cores
cs = cm.Set3(np.arange(100))

#Cria a figura
f = plt.figure()

#Gráfico de pizza(rosca)
plt.pie(resultado1['COUNT'], labeldistance = 1, radius = 3, colors = cs, wedgeprops = dict(width = 0.8))
plt.legend(labels = labels, loc = 'center', prop = {'size':12})
plt.title("Distribuição de Títulos", loc = 'Center', fontdict = {'fontsize':20,'fontweight':20})
plt.show()



#-----------------------------------------------------------------------------------------
