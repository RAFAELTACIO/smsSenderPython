from pprint import pp
import pandas as pd
from twilio.rest import Client

account_sid = 'AC2f2ae973efd32b1ba4a96cb04de052e2'
auth_token = 'd53c1a1364706aa0977698b8814537c9'
client = Client(account_sid, auth_token)

#passo a passo de solução
# abrir os 6 arquivos em excel

#para cada arquivo:
# verificar se algum valor na coluna vendas daquele arquivos é 55000
#se for maior do que 55000 - > envia um SMS com o Nome, o mes e as vendas do vendedor
#se nao for maior que 55000, não fazer nada

lista_meses = ['janeiro','fevereiro','março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to = "+5516988507278",
            from_ = "+19403534738",
            body = f'No mês {mes} alguem bateu a meta . Vendedor: {vendedor}, Vendas: {vendas}.Encontrou alguem com mais de 55000')
