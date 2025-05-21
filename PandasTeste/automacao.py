import pandas as pd
from IPython.display import display
vendas_df = pd.read_excel('Vendas.xlsx')
#display(vendas_df)
#display(vendas_df.head(10)) #Mostra quantas linhas eu quero ver
#print(vendas_df.shape) # para mostrar quantas linhas e colunas tem o arquivo
#display(vendas_df.describe()) #Para dara uma descrição sobre media por exemplo
produtos = vendas_df[['Produto', 'ID Loja']]
#display(produtos)

#Pegar uma linha
display(vendas_df.loc[1 : 5]) #Pegar linha de index 1 ate a 5

#Pegar linhas que correspondem a uma condição
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']
#display(vendas_norteshopping_df)

#Pegar varias linhas e colunas usando o loc
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping',['ID Loja', 'Produto', 'Quantidade']]
#display(vendas_norteshopping_df)

#Pegar 1 valor especifico
print(vendas_df.loc[1, 'Produto'])
