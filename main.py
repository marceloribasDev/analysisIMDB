# Imports
#  Pacote para expressoes regulares
import re
from select import select
from sys import displayhook

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


# =========================================================================
# Starting the exploratory analysis.
# =========================================================================

print('1- What are the most common movie categories on IMDB?')

# 1ª Query
select1 = '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type'''

# Extract result 1ª query
result1 = pd.read_sql_query(select1, conn)

# Show result
# print(result1)
display(result1)

# Calculating the percentage of each type
result1['percentual'] = (result1['COUNT'] / result1['COUNT'].sum()) * 100

display(result1)

# We're going to create a chart with just 4 categories:
# The 3 categories with the most titles and 1 category with all the rest

others = {}

# Filter the percentage at 5% and add up the total
others['COUNT'] = result1[result1['percentual'] < 5]['COUNT'].sum()

# Saves the percentage
others['percentual'] = result1[result1['percentual'] < 5]['percentual'].sum()

# Adjust the name
others['type'] = 'others'

# Show
others

# Filters the result dataframe
result1 = result1[result1['percentual'] > 5]

# Append com o dataframe de outras categorias
result1 = result1.append(others, ignore_index=True)

# Ordena o resultado
result1 = result1.sort_values(by='COUNT', ascending=False)

# Show
result1.head()

# Ajusta os labels
labels = [str(result1['type'][i])+' '+'[' +
          str(round(result1['percentual'][i], 2)) + '%'+']' for i in result1.index]

# Plot

# Mapa de cores
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
cs = cm.Set3(np.arange(100))

# Cria a figura
f = plt.figure()

# Pie Plot
plt.pie(result1['COUNT'], labeldistance=1, radius=3,
        colors=cs, wedgeprops=dict(width=0.8))
plt.legend(labels=labels, loc='center', prop={'size': 12})
plt.title("Distribuição de Títulos", loc='Center',
          fontdict={'fontsize': 20, 'fontweight': 20})
plt.show()
