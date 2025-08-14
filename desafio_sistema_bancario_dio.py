#### DESAFIO:
##################### CRIANDO UM SISTEMA BANCARIO COM PYTHON ############################
# Criar um sistema bancária com as operações: sacar, depositar e visualizar extrato
## OBJETIVO:
# Fomos contratados por um banco para desenvolver um sistema.
# Precisamos implementar 3 operações: Deposito, Saque e Extrato

# DEPOSITO)
# Deve ser possivel depositar valores positivos para a conta bancaria. 
# A V1 do projeto trabalha com apenas 1 usuario, nao precisando identificar numero da agencia e conta bancária.
# Todos os depositos devem ser amarzenados em uma variavel e exibidos na operação extrato

# SAQUE)
# O Sistema deve permitir realizar 3 saques diarios com limite máximo de 500,00 por saque. 
# Caso o usuario nao tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao será possivel sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variavel e exibidos na operaço de extrato 

#EXTRATO)
# Deve listar TODOS os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Valores devem ser exibidos no formato R$ xxx.x 

##############################################################################################################
from datetime import datetime

# Define Limite de Saques diarios
qtd_saques = 3 
# Define o saldo d Conta Teste do Sistema 
saldo_conta_teste = 6700.45

lista_op = []
lista_no = []

# Busca Dia Atual
def dia_atual():
    hoje = datetime.now().strftime("%d/%m/%Y")
    return(hoje)

# Interface do SIstema
def interface(data_hoje):
    print(f'''
====================BEM-VINDO!======================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
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
        else:
            return escolha

# EXTRATO 
def extrato(lista_tipo,lista_valor):
    global saldo_conta_teste
    msg = (f'''
====================EXTRATO=========================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
= Quantidade de Saques Diarios: {qtd_saques}       =
''')
    print(msg)
    for i in range(len(lista_tipo)):
        print(f'''
=  DATA: {data_hoje}                               =
=  TIPO OPERACAO : {lista_tipo[i]}
        ''')
        if lista_tipo[i][0] == 'Saque':
            print(f'''
=   VALOR : --- R$ {lista_valor[i][0]:.2f}
'''.replace('.', ','))
        elif lista_tipo[i][0] == 'Depósito':
            print(f'''
=   VALOR : +++ R$ {lista_valor[i][0]:.2f}
'''.replace('.', ','))
    print(f'''
=                                                  =
=--------------------------------------------------=
= SALDO FINAL: R$ {saldo_conta_teste}              =
=                                                  =
=================FIM DO EXTRATO=====================
    ''')    
    return(0)


# SAQUES !
def saque():
    global qtd_saques, saldo_conta_teste
    print(f'''
====================SAQUES==========================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
= Quantidade de Saques Diarios: {qtd_saques}       =
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
                    lista_op.append([valor_saca])
                    # Coloca o tipo de ação realizada em uma lista
                    lista_no.append(['Saque'])
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
                    if escolha_tenta == 's':
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



# DEPOSITOS!
def deposito():
    global saldo_conta_teste
    print(f'''
====================DEPOSITOS=======================
= Cliente: Teste01                                 =
= Agencia: 001                                     =
= Banco: 3201                                      =
= DATA: {data_hoje}                                =
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
            lista_op.append([valor_dep])
            # Coloca o tipo de ação realizada em uma lista
            lista_no.append(['Depósito'])
            print('Operação Realizada com Sucesso')
            print('Valor Depositado: ',valor_dep,'| Total: ',saldo_conta_teste)
                    
            escolha_tenta = input('Deseja Tentar um novo Valor? [s]/[n]')
            if escolha_tenta == 's':
                print('-------------------------')
            else:
                print('-----------VOLTANDO-------')
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
                break
                #sys.exit()    
            elif escolha_sair.lower() == 'n':
                break 
            else:
                print('\n-----------------------------------------\nInput nao Reconhecido\n-----------------------------------------\n')
    # Chamar Saque
    elif escolha == "3":
        while True:
            print('Chamar Saque')
            retorno_saque = saque()
            if retorno_saque == '0' or retorno_saque == 0:
                print('Voltando Ao Menu')
                #print(lista_no,'\n',lista_op)
                break
            print(lista_no,'\n',lista_op)
            
    # Chamar Depósitos
    elif escolha == "2":
        while True:
            print('Chamar Depósitos')
            retorno_deposito = deposito()
            if retorno_deposito == '0' or retorno_deposito == 0:
                print('Voltando Ao Menu')
                #print(lista_no,'\n',lista_op)
                break
            print(lista_no,'\n',lista_op)

    # Chamar Extrato
    elif escolha == "1":
        while True:
            print('Chamar Extrato')
            retorno_extrato = extrato(lista_no,lista_op)
            if retorno_extrato == '0' or retorno_extrato == 0:
                print('Voltando Ao Menu')
                #print(lista_no,'\n',lista_op)
                break
