# Imports
#  Pacote para expressoes regulares
import re

#  Mede o tempo de execucao e ou trabalhar com datas
import time

# Baanco de dados SQLite
import sqlite3

# Converte o nome dos pais
import pycountry

# Utilizado para manipulacao de dados
import numpy as np

# Utilizado para manipulacao de dados
import pandas as pd


# Utilizado para visualizacao de dados em python
import matplotlib.pyplot as plt

# Utilizado para visualizacao de dados em python
import seaborn as sns

# Utilizado para visualizacao de dados em python
from matplotlib import cm

# Pacote para Machine Leaning
from sklearn.feature_extraction.text import CountVectorizer

# Filtra Warnings
import warnings
warnings.filterwarnings("ignore")

# Configurado o grid dos graficos
sns.set_theme(style="whitegrid")

# =========================================================================
# Preparing the environment and connection tests with the db
# =========================================================================

# Connect db
conn = sqlite3.connect("imdb.db")

# Extract table in db
tabelas = pd.read_sql_query(
    "SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'", conn)

tabelas.head()


# Vamos converter o dataframe em uma lista
tabelas = tabelas["Table_Name"].values.tolist()

# Vamos percorrer a lista de tabelas no banco de dados e extrair o esquema de cada uma
for tabela in tabelas:
    consulta = "PRAGMA TABLE_INFO({})".format(tabela)
    resultado = pd.read_sql_query(consulta, conn)
    print("Esquema da tabela:", tabela)
    display(resultado)
    print("-"*100)
    print("\n")
