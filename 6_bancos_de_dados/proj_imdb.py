#Projeto analisando dados IMDB

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
sns.set_theme(style="whitegrid")

