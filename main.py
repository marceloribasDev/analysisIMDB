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

# ================================================================================

# Connect db
conn = sqlite3.connect("imdb.db")

# Extract table in db
tabelas = pd.read_sql_query(
    "SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'", conn)

tabelas.head()
