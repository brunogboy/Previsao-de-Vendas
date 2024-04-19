#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[2]:


# Caminho para o arquivo Excel
caminho_arquivo = 'downloads/planilha_varejo.xlsx'

# Carregar o arquivo Excel em um DataFrame do Pandas
dados_vendas = pd.read_excel(caminho_arquivo)


# In[4]:


dados_vendas.head()


# In[5]:


dados_vendas['InvoiceDate'] = pd.to_datetime(dados_vendas['InvoiceDate'])


# In[6]:


dados_vendas['Ano'] = dados_vendas['InvoiceDate'].dt.year
dados_vendas['Mês'] = dados_vendas['InvoiceDate'].dt.month


# In[7]:


dados_2011 = dados_vendas[dados_vendas['Ano'] == 2011]


# In[8]:


vendas_por_mes_2011 = dados_2011.groupby('Mês')['Quantity'].sum()


# In[10]:



vendas_por_mes_2011.describe()


# In[11]:


# Transformar o índice em uma matriz de recursos (reshape) para a regressão linear
X = vendas_por_mes_2011.index.values.reshape(-1, 1)
y = vendas_por_mes_2011.values


# In[12]:


# Ajustar um modelo de regressão linear aos dados
modelo_regressao = LinearRegression()
modelo_regressao.fit(X, y)


# In[13]:


# Fazer previsões para janeiro de 2012
previsao_jan_2012 = modelo_regressao.predict([[13]])


# In[14]:


# Plotar as vendas históricas e a linha de tendência
plt.scatter(vendas_por_mes_2011.index, vendas_por_mes_2011.values, color='white', label='Vendas em 2011', s=90)
plt.plot([13], previsao_jan_2012, marker='o', color='gold', label='Previsão para Janeiro de 2012', markersize=13)
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.title('Vendas Históricas de 2011 e Previsão para Janeiro de 2012')
plt.legend()
plt.grid(color = 'black', linestyle = '--', linewidth = 0.09)
plt.gca().set_facecolor('#B7D1FF')
plt.show()


# In[15]:


print("Previsão de Vendas para Janeiro de 2012:", round (previsao_jan_2012[0], 2))


# In[ ]:




