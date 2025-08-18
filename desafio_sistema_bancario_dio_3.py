###
########### FAZER:
# Terminar Caminho CLiente
# Terminar Caminho Funcionario

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
from datetime import datetime
import calendar
import sys
#############################################################################################
##############################      INICIALIZADORES      ####################################
#
#Define o perfil do admin
perfil_adm = 'admin'
# Define Limite de Transações diárias para Uma Conta
limite_diario = 10
# Define Limite de Saques diarios
qtd_saques = 3
# Define o saldo d Conta Teste do Sistema
saldo_conta_teste = 6700.45
# Listas Cliente
lista_data_transacao = []
lista_valor_transacao = []
lista_tipo_transacao = []
# Listas Usuario
lista_usuario = ['24859637040','36581420906','52790163480']
lista_dicionario = [{'CPF': '24859637040', 'NOME': 'ADD EEE', 'DATA DE NASCIMENTO': '03/03/1922', 'ENDERECO': 'e r f d RJ'},
    {'CPF': '52790163480', 'NOME': 'BBBBBB BBBBBB', 'DATA DE NASCIMENTO': '26/07/1910','ENDERECO': 'PPP, ,01, ,EREA, ,OANC, ,RJ'},
    {'CPF': '52790163482', 'NOME': 'CCCCCC BBBBBB', 'DATA DE NASCIMENTO': '26/07/1923','ENDERECO': 'PPP, ,01, ,EREA, ,OANC, ,RJ'}
]
lista_contas = []
#############################################################################################
###################################      FUNCOES     ########################################
#############################################################################################
# 
#########################################  DATA     ######################################## 
#
# Busca Dia Atual
def dia_atual():
    hoje = datetime.now().strftime("%d/%m/%Y")
    return (hoje)
    
# Conta dia atual
def contar_dia():
    # Verifica a lista que contem as datas de transações e conta quantos equivalem ao dia atual
    qtd_transacoes_hoje = lista_data_transacao.count(dia_atual())
    # Retorna quantidade de transações de hoje
    return (qtd_transacoes_hoje)

#########################################       CPF     ##################################### 
def validar_cpf(cpf):
    # Verifica 11 dígitos
    if len(cpf) != 11:
        return False
# Verifica se todos os Digitos sao iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula o 1º dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    # Calcula o 2º dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    # Compara com os dígitos originais
    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

#############################################################################################
#                                                                                           #
######################################   TELAS    ###########################################
#
#

def tela_start():
    inicio = """
------------------ BANCO ------------------

    [1] LOGIN
    [q] Sair
--------------------------------------------
    =>"""
    return input(inicio)

######


def tela_login():
    inicio = """
------------------ LOGIN ------------------
ENTRE COM SEU LOGIN 
--------------------------------------------
    =>"""
    print(inicio)
    login = input('ENTRE COM SEU LOGIN OU CPF: \n')
    senha = input('ENTRE COM SUA SENHA OU DATA DE NASCIMENTO: \n')
    # PARA FUNCIONARIO, ENTRAR COM LOGIN e SENHA como admin 
    print(lista_usuario,'---------------\n')
    print(lista_dicionario,'---------------\n')
    if(login == 'admin' and senha == 'admin'):
        print('BEM VINDO, TESTER!')
        return login
    
    # PARA CLIENTES, PEDE CPF E VERIFICA NA LISTA_USUARIO e DEPOIS na LISTA_DICIONARIO    
    elif(login in lista_usuario):  # Verifica o CPF na lista_usuario
        #print('login = ',login,'  |  lista_usuario= ',lista_usuario)
        login_encontrado = False
        
        for usuario in lista_dicionario:
            #print(usuario['CPF'])
            if login == usuario['CPF']:  # Verifica que o Login da Lista CPF é o mesmo do Dicionario
               login_encontrado = usuario  # guarda o dicionario inteiro
               break
               # print('ITERADOR \n',iterador,'SENHA',senha,'\nITEM',item['DATA DE NASCIMENTO'])
        if login_encontrado:
            if senha == login_encontrado['DATA DE NASCIMENTO']:
                print('DATA DE NASCIMENTO ',senha)
                print('MATCH!')
                return login
            else:
                print('SENHA INCORRETA',senha,'---',login_encontrado['DATA DE NASCIMENTO'])
            return False
        else:
            print('CPF NAO ENCONTRADO')
            return False
 
    else:
        print('Credenciais Incorretas')
        return False
    #return input(inicio)

######

def menu_cliente():
    menu = """
------------------ MENU ------------------

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
--------------------------------------------
    =>"""
    return input(menu)

#####

def menu_funcionario():
    menu = """
------------- SISTEMA INTERNO ---------------

    [u] Criar Novo Usuario
    [c] Criar Conta Corrente
    [l] Listagem de Usuários
    [q] Sair
--------------------------------------------
    =>"""
    return input(menu)
#############################################################################################

#############################################################################################

def main():
    
    # Inicializadores #
    saldo = 0
    limite = 500
    extrato = ""
    qtd_saques = 0
    limite_saque = 3
    lista_clientes = []
    lista_contas = []
    AGENCIA = "0001"
    
    while True:
        escolha = tela_start()
        
        if(escolha == '1'):
            print('-Chama Tela de Login-')
            login_realizado = tela_login()
            if login_realizado != False:
                print('LOGOU!',login_realizado,'|',perfil_adm)
                if login_realizado == perfil_adm:
                    menu_funcionario()
                else:
                    menu_cliente(login_realizado)
            else:
                print('Deu Erro no Login...')
            # Caso Escolha seja = 1, Vai pedir login e senha ; 
            
        elif(escolha == 'q'):
            print('-Encerrando Atendimento, Desligando Terminal')
            sys.exit()
        else:
            print('Tecla Não Suportada, Insira Novamente')


############

main()
