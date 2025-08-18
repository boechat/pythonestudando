####################################### DESAFIO:
##################### SISTEMA BANCÁRIO PARTE 3 - OTIMIZANDO O SISTEMA BANCÁRIO COM FUNÇÕES PYTHON ############################
# Continuar o desafio do Sistema Bancário, adicionando

### OBJETIVO GERAL 
# Separar as funções existentes de Saque, Depósito e Extrato em Funções;
# Criar duas novas funções: Cadastrar Usuário (Cliente) e Cadastrar Conta Bancária

### DESAFIO
# Deixar o código mais modularizado, para isso criar funções para as operações Existintes: 
# Sacar, Depositar e Extrato. Além disso, precisamos criar duas novas funções: Criar Usuário e 
# Criar Conta Corrente (Vincular com Usuario)

### Separação em funções
# Para exercitar, cada função VAI TER UMA REGRA NA PASSAGEM de argumentos. 

########
## FUNÇÃO SAQUE
# Deve receber os argumentos APENAS  POR NOME (keyword only)
# Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
# Sugestão de retorno: saldo e extrato

## FUNÇÃO DEPÓSITO
# Deve receber o argumentos APENAS POR POSIÇÃO (position only);
# Sugestão de argumentos: saldo, valor, extrato
# Sugestão de retorno: saldo e extrato

## FUNÇÃO EXTRATO
# Deve receber os argumentos por posição e nome (postional only e keyword only)
# Argumentos posicionais: saldo
# Argumentos nomeados: extrato

## NOVAS FUNÇÕES
# Precisamos criar novas funções: 
#   1) CRIAR USUARIO 
#       - Armazenar os usuários em uma LISTA 
#       - Usuário composto por : NOME , DATA DE NASCIMENTO, CPF e ENDEREÇO
#       - Endereço é uma string com o formato: logradouro, numero, bairro, cidade/siga, estado.
#       - Deve ser armazenado somente os números do CPF.
#       - Não podemos cadastrar 2 usuários com o mesmo CPF.
#       - Verificar se é um CPF válido 
#   2) CRIAR CONTA CORRENTE
#       - Armazenar contas em uma lista;
#       - Conta composta por: Agência, Número da Conta e Usuário. 
#       - O número da conta é sequencial, iniciando em 1; 
#       - O Número da agência é fixo: 0001
#       - O usuário pode ter mais de uma conta, mas uma conta pertencente apenas a um usuario.
#
# DICA:
# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado
# para cada usuário da lista.
#
# Adicionar mais funções;
#   3) LISTAR CONTAS 
#   4) ATUALIZAR INFORMAÇÕES DO USUARIO
#   5) TROCAR SENHA

##############################################################################################################
from datetime import datetime
import sys


# Define Limite de Transações diárias para Uma Conta
limite_diario = 10

# Define Limite de Saques diarios
qtd_saques = 3 

# Define o saldo d Conta Teste do Sistema 
saldo_conta_teste = 6700.45

# Listas
lista_data_transacao = []
lista_valor_transacao = []
lista_tipo_transacao = []

# Busca Dia Atual
def dia_atual():
    hoje = datetime.now().strftime("%d/%m/%Y")
    return(hoje)

# Conta dia atual
def contar_dia():
    # Verifica a lista que contem as datas de transações e conta quantos equivalem ao dia atual
    qtd_transacoes_hoje = lista_data_transacao.count(dia_atual())
    # Retorna quantidade de transações de hoje
    return(qtd_transacoes_hoje)
    
# Interface do SIstema
def interface(data_hoje):
    global limite_diario
    print(f'''
====================BEM-VINDO!======================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                 =
= Quantidade de Transações Diárias: {(limite_diario -contar_dia())}             =
=**************************************************=                                                 
= DIGITE PARA INICIAR SEU ATENDIMENTO              =
= [1] - Extrato Bancário                           =
= [2] - Deposito                                   =
= [3] - Saques                                     =
= [q] - Sair                                       =
====================================================
    ''')

# Interacao do Usuario com o Sistema
def interacao_interface():
    while True:
        escolha = input('\n-----------------------------------------\nEntre com o que deseja acessar\n-----------------------------------------\n')
        if(escolha not in ('1', '2', '3', "q")):
            print('\n-----------------------------------------\nValor inválido, tente novamente\n-----------------------------------------\n')
        elif(escolha in ('1', "q") and (contar_dia() >= limite_diario)):
             print('Número de Transações Diárias Encerradas. \n\n Por favor, tente novamente amanhã ou entre em contato com a Gerência!\n-----------------------------------------\n')
             return(0)
        elif(escolha in ('1','2','3',"q",) and (contar_dia() < limite_diario)):         
            #print('elif')
            return escolha

########################################### EXTRATO 

def extrato(lista_tipo,lista_valor,lista_data_transacao):
    global saldo_conta_teste
    global limite_diario
    msg = (f'''
====================EXTRATO=========================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
= Quantidade de Saques Diarios: {qtd_saques}       =
= Quantidade de Transações Diárias: {(limite_diario -contar_dia())}             =
====================================================
====================================================
''')
    print(msg)
    for i in range(len(lista_tipo)):
        print(f'''
=  DATA: {lista_data_transacao[i]}                               
=  TIPO OPERACAO : {lista_tipo[i][0]}                           ''')
        if lista_tipo[i][0] == 'Saque':
            print(f'''=   VALOR : --- R$ {lista_valor[i][0]:.2f}\n'''.replace('.', ','))
        elif lista_tipo[i][0] == 'Depósito':
            print(f'''=   VALOR : +++ R$ {lista_valor[i][0]:.2f}\n'''.replace('.', ','))
    print(f'''
=                                                  =
=--------------------------------------------------=
=                                                  =
=                                                  =
= SALDO FINAL: R$ {saldo_conta_teste}              =
=                                                  =
=                                                  =
=================FIM DO EXTRATO=====================
    ''')    
    return(0)


########################################################### SAQUES !

def saque():
    global qtd_saques, saldo_conta_teste,limite_diario
    print(f'''
====================SAQUES==========================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                 =
= Quantidade de Transações Diárias: {(limite_diario -contar_dia())}             =
= Quantidade de Saques Diarios: {qtd_saques}                  =
=**************************************************=  
''')

    while True:
        if (qtd_saques > 0):
            escolha_saq = input('''
= DIGITE PARA INICIAR SEU ATENDIMENTO              =
= [1] - SACAR                                      =
= [q] - Sair                                       =
====================================================
    ''')
            if escolha_saq == '1':
#                print('Entrou')
                valor_saca = float(input('''
====================================================
=       QUANTO GOSTARIA DE SACAR?                  =
=Digite o valor em numeros no formato R$ x.xx      =
====================================================
'''))
                if float(valor_saca) <= 500.00 and float(saldo_conta_teste) > 0 and float(saldo_conta_teste) >= float(valor_saca):
                    saldo_restante = float(saldo_conta_teste) - float(valor_saca)
                    # Coloca o valor em uma lista
                    lista_valor_transacao.append([valor_saca])
                    # Coloca o tipo de ação realizada em uma lista
                    lista_tipo_transacao.append(['Saque'])
                    # Coloca a Data Realizada em uma lista
                    lista_data_transacao.append(dia_atual())
                    
                    print('Operação Realizada com Sucesso')
                    qtd_saques = qtd_saques - 1
                    print('#             SAQUES RESTANTES: ',qtd_saques,'             #')


                elif(saldo_conta_teste <= 0):
                    print('Saldo Insuficiente!')
                elif(valor_saca >= 500):
                    print('Limite de Saque Atingindo, precisa ser menos de 500 reais')
                elif(saldo_conta_teste < valor_saca):
                    print('Valor a ser Sacado é Maior do que o Saldo da Conta')
                    escolha_tenta = input('Deseja Tentar um novo Valor? [s]/[n]')
                    if escolha_tenta == 's' and contar_dia() < 10:
                        print('-------------------------')
                    else:
                        print('-----------VOLTANDO-------')
                        return 0
            elif(escolha_saq == 'q'):
                print('-----------VOLTANDO-------')
                return 0
        else:
            print('LIMITE DE SAQUES ATINGINDO, SEU LIMITE SERÁ LIBERADO NO DIA SEGUINTE A ESSA OPERAÇÃO')
            return 0



###########################################################  DEPOSITOS!
def deposito():
    global saldo_conta_teste, limite_diario
    print(f'''
====================DEPOSITOS=======================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
= Quantidade de Transações Diárias: {(limite_diario -contar_dia())}             =
=**************************************************=  
''')

    while True:
        escolha_dep = input('''
= DIGITE PARA INICIAR SEU ATENDIMENTO              =
= [1] - DEPOSITOS                                      =
= [q] - Sair                                       =
====================================================
    ''')
        if escolha_dep == '1':
#           print('Entrou')
            valor_dep = float(input('''
====================================================
=       QUANTO GOSTARIA DE DEPOSITAR?              =
=Digite o valor em numeros no formato R$ x.xx      =
====================================================
'''))
            saldo_conta_teste = float(valor_dep) + float(saldo_conta_teste)
            # Coloca o valor em uma lista
            lista_valor_transacao.append([valor_dep])
            # Coloca o tipo de ação realizada em uma lista
            lista_tipo_transacao.append(['Depósito'])
            # Coloca a Data Realizada em uma lista
            lista_data_transacao.append(dia_atual())
            
            print('Operação Realizada com Sucesso')
            print('Valor Depositado: ',valor_dep,'| Total: ',saldo_conta_teste)
                    
            escolha_tenta = input('Deseja Tentar um novo Valor? [s]/[n]')
            if escolha_tenta == 's' and contar_dia() < limite_diario:          
                print('-------------------------')
            elif escolha_tenta == 'n' and contar_dia() < limite_diario:
                print('-----------VOLTANDO-------')
                return 0
            elif contar_dia() >= limite_diario :
                print('-----------Operação Cancelada: Limite de Transações Diárias-------')
                return 0
 
        elif(escolha_dep == 'q'):
            print('-----------VOLTANDO-------')
            return 0
        


    
############################################################### Principal       ###########################################################

data_hoje = dia_atual()

while True:
    interface(data_hoje)
    escolha = interacao_interface()
    
    # Para Sair
    if escolha == 'q':
        while True:
            escolha_sair = input('\n-----------------------------------------\nTem Certeza Que Deseja Sair? [s]\[n]\n-----------------------------------------\n')
            if escolha_sair.lower() == 's':
                print('\n-----------------------------------------\nVolte Sempre!\n-----------------------------------------\n')
                #break
                sys.exit()    
            elif escolha_sair.lower() == 'n':
                break 
            else:
                print('\n-----------------------------------------\nInput nao Reconhecido\n-----------------------------------------\n')
    
    # Caso Limite de Transações Diárias tenha sido Atingidas
    elif escolha == '0' or escolha == 0:
        print('\n-----------------------------------------\nVolte Sempre!\n-----------------------------------------\n')
        
        sys.exit()  
        
    # Chamar Saque
    elif escolha == "3":
        while True:
            print('Chamar Saque')
            retorno_saque = saque()
            if retorno_saque == '0' or retorno_saque == 0:
                print('Voltando Ao Menu')
                #print(lista_tipo_transacao,'\n',lista_valor_transacao)
                break
            print(lista_tipo_transacao,'\n',lista_valor_transacao)
            
    # Chamar Depósitos
    elif escolha == "2":
        while True:
            print('Chamar Depósitos')
            retorno_deposito = deposito()
            if retorno_deposito == '0' or retorno_deposito == 0:
                print('\n\n\nVoltando Ao Menu\n\n\n')
                #print(lista_tipo_transacao,'\n',lista_valor_transacao)
                break
            print(lista_tipo_transacao,'\n',lista_valor_transacao)

    # Chamar Extrato
    elif escolha == "1":
        while True:
            print('Chamar Extrato')
            retorno_extrato = extrato(lista_tipo_transacao,lista_valor_transacao,lista_data_transacao)
            if retorno_extrato == '0' or retorno_extrato == 0:
                print('Voltando Ao Menu')
                #print(lista_tipo_transacao,'\n',lista_valor_transacao)
                break

