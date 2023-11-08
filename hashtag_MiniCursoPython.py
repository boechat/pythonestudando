import pandas as pd
import win32com.client as win32

endereco = r"C:\Users\User\Desktop\RPA\\"
arquivo = 'Vendas.xlsx'
arquivo_end = endereco+arquivo


#### 1)  Importar a base de dados
tabela_vendas = pd.read_excel(arquivo_end)

#### 2)  Visualizar a base de dados
#Usando display.max_columns para mostrar tudo
pd.set_option('display.max_columns', None)
#print(tabela_vendas)

#### 3) Calcular o Faturamento por Loja
tabela_soma = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
#print(tabela_soma)

#### 4) Quantidade de Produtos Vendidos Por Loja
tabela_qtd = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
#print(tabela_qtd)

### 5) Ticket Médio por Produto em cada Loja
ticket_med = (tabela_soma['Valor Final']/tabela_qtd['Quantidade']).to_frame() #to_frame transforma em uma tabela
#Mudar o Nome da Coluna com o .Rename
ticket_med = ticket_med.rename(columns={0: 'Ticket Médio'})
#print(ticket_med)

### 6) enviar um email com o relatório
# Com outlook: instalar pywin32

#import win32com.client as win32
outlook = win32.Dispatch('outlook.application')  #Se Conecta ao Outlook do PC
mail = outlook.CreateItem(0)        #Cria email (Item do Outlook)
mail.To = 'To address'         #Colocar o seu email que você tem acesso
mail.Subject = 'Message subject'          #Assunto do email
mail.HTMLBody = f'''                                
<p>Teste de Email</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{tabela_soma.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p> 
{tabela_qtd.to_html()}

<p>Ticket Médio dos Produtos em Cada Loja:</p>
{ticket_med.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}


'''

mail.Send()