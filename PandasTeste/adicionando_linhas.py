import pandas as pd
from IPython.display import display
vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
#display(vendas_dez_df)
vendas_df = pd.read_excel('Vendas.xlsx')
#display(vendas_df)
vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True)
display(vendas_df)