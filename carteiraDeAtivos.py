import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

carteira_ativos = pd.read_excel("Ativos.xlsx")
print(carteira_ativos)

# Criando o dataframe de cotaçoes da carteira

cotacoes_carteira_ativos = pd.DataFrame()

for Ativos in carteira_ativos['Ativos']:
    cotacoes_carteira_ativos[Ativos] = web.DataReader('{}.SA'.format(Ativos), data_source='yahoo', start='2022-01-01',end='2022-06-08')['Adj Close']
    print(cotacoes_carteira_ativos)