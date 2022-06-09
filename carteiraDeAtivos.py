import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

carteira_ativos = pd.read_excel("ativos.xlsx")
print(carteira_ativos)

# Criando o dataframe de cotaçoes da carteira