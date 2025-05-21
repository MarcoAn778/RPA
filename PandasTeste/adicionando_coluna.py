import pandas as pd
from IPython.display import display

# a partir de uma coluna que existe
vendas_df = pd.read_excel('Vendas.xlsx')
vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
gerente_df = pd.read_excel('Gerentes.xlsx')

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05

# criar uma coluna com valor padrão
vendas_df.loc[ :, 'Imposto'] = 0  # : significa todas as linhas
#display(vendas_df)

#Adicionar um arquivo em outro
vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True)
#display(vendas_df)

#Excluir linhas e colunas
vendas_df = vendas_df.drop('Imposto', axis= 1)  # axis = 0 é a linha axis = 1 é coluna
#display(vendas_df)

#vendas_df = vendas_df.drop(0, axis= 0)
#display(vendas_df)

#Deletar linhas e colunas completamente vazias
#vendas_df = vendas_df.dropna(how='all', axis= 1)
#display(vendas_df)

#deletar linhas que possuem pelo menos 1 valor vazio
#vendas_df = vendas_df.dropna()

#Preencher valores vazios
#Preencher com a média da coluna
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
#display(vendas_df)

#Preencher com o ultimo valor
#vendas_df = vendas_df.ffill()

#Calcular Indicadores
#display(transacoes_loja)

#Grup by
#faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum(numeric_only=True)
#display(faturamento_produto)

#Mesclar 2 dataFrames
#display(gerente_df)

vendas_df = vendas_df.merge(gerente_df)
display(vendas_df)
