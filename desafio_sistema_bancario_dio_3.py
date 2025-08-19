###
########### TO DO:
#### - Terminar Caminho CLiente
# [ ] Saque
# [ ] Deposito
# [ ] Extrato
#### - Opcional
# [ ] Criar um Selecionar Conta


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
# [ok]      - Armazenar os usuários em uma LISTA
# [ok]      - Usuário composto por : NOME , DATA DE NASCIMENTO, CPF e ENDEREÇO
# [ok]      - Endereço é uma string com o formato: logradouro, numero, bairro, cidade/siga, estado.
# [ok]      - Deve ser armazenado somente os números do CPF.
# [ok]      - Não podemos cadastrar 2 usuários com o mesmo CPF.
# [ok]      - Verificar se é um CPF válido
#   2) CRIAR CONTA CORRENTE
# [ok]      - Armazenar contas em uma lista;
# [ok]      - Conta composta por: Agência, Número da Conta e Usuário.
# [ok]      - O número da conta é sequencial, iniciando em 1;
# [ok]      - O Número da agência é fixo: 0001
# [ok]      - O usuário pode ter mais de uma conta, mas uma conta pertencente apenas a um usuario.
#
# DICA:
# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado
# para cada usuário da lista.
#
# Adicionar mais funções;
# [ok]  3) LISTAR CONTAS
# [ok]  3a ) LISTAR TODOS OS USUARIOS COM CONTAS
# [ok]  3b ) LISTAR TODOS OS USUARIOS CADASTRADOS
#
#
from datetime import datetime
import calendar
import sys

#############################################################################################
##############################      INICIALIZADORES      ####################################
#
# Define o perfil do admin
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
lista_usuario = ['1','25836914700', '74692538170', '10348795211','59123647806','82051463993','47268130584']
#### CPFS VALIDOS: 01234567890 ;
lista_dicionario = [
    {'CPF': '1', 'NOME': 'USUARIO SENHA RAPIDA', 'DATA DE NASCIMENTO': '1', 'ENDERECO': 'LETS GOOOOO'},
    {'CPF': '25836914700', 'NOME': 'ADD EEE', 'DATA DE NASCIMENTO': '03/03/1922', 'ENDERECO': 'e r f d RJ'},
    {'CPF': '74692538170', 'NOME': 'BBBBBB BBBBBB', 'DATA DE NASCIMENTO': '26/07/1910','ENDERECO': 'PPP, ,01, ,EREA, ,OANC, ,RJ'},
    {'CPF': '10348795211', 'NOME': 'CCCCCC BBBBBB', 'DATA DE NASCIMENTO': '26/07/1923','ENDERECO': 'PPP, ,01, ,EREA, ,OANC, ,RJ'},
    {'CPF': '59123647806', 'NOME': 'Orba Lambo', 'DATA DE NASCIMENTO': '12/12/1922','ENDERECO': 'Liberdade 99 Santa Casa RJ RJ'},
    {'CPF': '82051463993', 'NOME': 'Maria Silva', 'DATA DE NASCIMENTO': '05/05/1985','ENDERECO': 'Rua das Flores 123 São Paulo SP'},
    {'CPF': '47268130584', 'NOME': 'João Pereira', 'DATA DE NASCIMENTO': '18/11/1972','ENDERECO': 'Av. Brasil 456 Rio de Janeiro RJ'}
]
#lista_contas = []
lista_contas = [{'agencia': '0001', 'conta': 1, 'cpf': '47268130584'}, {'agencia': '0001', 'conta': 2, 'cpf': '47268130584'},{'agencia': '0001', 'conta': 3, 'cpf': '82051463993'},
                {'agencia': '0001', 'conta': 4, 'cpf': '59123647806'},{'agencia': '0001', 'conta': 5, 'cpf': '59123647806'},{'agencia': '0001', 'conta': 6, 'cpf': '74692538170'},
                {'agencia': '0001', 'conta': 7, 'cpf': '1'}]



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

############################## TELA INICAL #################################################
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


############################## TELA LOGIN #################################################
#
#
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
    print(lista_usuario, '---------------\n')
    print(lista_dicionario, '---------------\n')
    if (login == 'admin' and senha == 'admin'):
        print('BEM VINDO, TESTER!')
        return login

    # PARA CLIENTES, PEDE CPF E VERIFICA NA LISTA_USUARIO e DEPOIS na LISTA_DICIONARIO
    elif (login in lista_usuario):  # Verifica o CPF na lista_usuario
        # print('login = ',login,'  |  lista_usuario= ',lista_usuario)
        login_encontrado = False

        for usuario in lista_dicionario:
            # print(usuario['CPF'])
            if login == usuario['CPF']:  # Verifica que o Login da Lista CPF é o mesmo do Dicionario
                login_encontrado = usuario  # guarda o dicionario inteiro
                break
                # print('ITERADOR \n',iterador,'SENHA',senha,'\nITEM',item['DATA DE NASCIMENTO'])
        if login_encontrado:
            if senha == login_encontrado['DATA DE NASCIMENTO']:
                print('DATA DE NASCIMENTO ', senha)
                print('MATCH!')
                return login
            else:
                print('SENHA INCORRETA', senha, '---', login_encontrado['DATA DE NASCIMENTO'])
            return False
        else:
            print('CPF NAO ENCONTRADO')
            return False

    else:
        print('Credenciais Incorretas')
        return False
    # return input(inicio)


############################## TELA DO CLIENTE #################################################
#
#
def menu_cliente(data_hoje,login_cpf):
    global limite_diario
    menu = f"""
------------------ MENU ------------------
= - BEM VINDO !                          =
=   Data: {data_hoje}                     =
=   CPF: {login_cpf}                     =
=   Agencia: 0001                        =
=   Quantidade de Transações Diárias: {(limite_diario -contar_dia())}=
==========================================-
=                                        =
=    [d] Depositar                       =
=    [s] Sacar                           =
=    [e] Extrato                         =
=    [q] Sair                            =
--------------------------------------------
    =>"""
    return input(menu)


############################## TELA DO FUNCIONARIO #################################################
#
#
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
#                                                                                           #
######################################   FUNCOES    #########################################
#                                                                                           #
############################## FUNCOES CLIENTE ##############################################
#                                                                                           #
#
########################

#
#
#
#

#                                                                                           #
############################## FUNCOES FUNCIONARIO ##########################################
#                                                                                           #
#
#
###############################  CADASTRAR USUARIO
#                                                                          #
def cadastrar_usuario():
    # Pega o dia da Criação
    hoje = dia_atual()
    # Pega o Ano Atual
    ano = int(hoje.split("/")[2])
    # Estabelece a Lista possível de Estados
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
               "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
               "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    # Define um Dicionario
    dic_usuario = {}

    # Pega CPF
    usuario_cpf = input('Digite o CPF : ')
    # Filtrando por apenas Numeros
    usuario_cpf = "".join([letra for letra in usuario_cpf if letra.isdigit()])
    print('VALIDANDO CPF: ', usuario_cpf)

    # Chama Função pra Validar CPF
    cpf_validado = validar_cpf(usuario_cpf)

    ## Trata CPF
    if cpf_validado == False:
        print('CPF Não é Válido')
        return (False)
    else:
        print('CPF Válido, Verificando se Existe No Sistema ... :\n')

    print(usuario_cpf,lista_usuario)
    if usuario_cpf in lista_usuario:
        print('Usuario já cadastrado no Sistema')
        # Para caso queira depois alterar Usuario
        return (False)
    else:
        # Adiciona na lista
        lista_usuario.append(usuario_cpf)
        # Adiciona no dicionario
        dic_usuario['CPF'] = usuario_cpf
        print(f'CPF: {usuario_cpf} cadastrado na Lista!')

    ### Preenche As Demais Informações do Dicionario###########

    usuario_nome = input('Digite o Nome : ')
    usuario_sobrenome = input('Digite o Sobrenome: ')
    usuario_nome_completo = (f'{usuario_nome} {usuario_sobrenome}')

    # Adiciona ao Dicionario
    dic_usuario['NOME'] = usuario_nome_completo

    usuario_dia_nascimento = input('Digite o Dia em que Nasceu : ')
    if int(usuario_dia_nascimento) < 10 and int(usuario_dia_nascimento) > 0 and len(usuario_dia_nascimento) != 2:
        usuario_dia_nascimento = (f'0{usuario_dia_nascimento}')
    if not usuario_dia_nascimento.isdigit() or int(usuario_dia_nascimento) <= 0 or int(usuario_dia_nascimento) >= 32:
        print('Dados Invalidos, Intervalo informado não corresponde.')
        return (False)

    usuario_mes_nascimento = input('Digite o Mes em que Nasceu : ')
    if int(usuario_mes_nascimento) < 10 and int(usuario_mes_nascimento) > 0 and len(usuario_mes_nascimento) != 2:
        usuario_mes_nascimento = (f'0{usuario_mes_nascimento}')
    if not usuario_mes_nascimento.isdigit() or int(usuario_mes_nascimento) <= 0 or int(usuario_mes_nascimento) >= 13:
        print('Dados Invalidos, Intervalo informado não corresponde.')
        return (False)

    usuario_ano_nascimento = input('Digite o Ano em que Nasceu : ')
    if not usuario_ano_nascimento.isdigit() or int(usuario_ano_nascimento) <= 1900 or int(
            usuario_ano_nascimento) >= ano:
        print('Dados Invalidos, Intervalo informado não corresponde.')
        return (False)

    # Verifica se o dia de Nascimento está correto, verificando também ano bissexto
    qtd_dias = calendar.monthrange(int(usuario_ano_nascimento), int(usuario_mes_nascimento))[1]
    if int(usuario_dia_nascimento) > int(qtd_dias):
        print('Dados Invalidos, Intervalo informado não corresponde.')
        return (False)
    usuario_data_nascimento = (f'{usuario_dia_nascimento}/{usuario_mes_nascimento}/{usuario_ano_nascimento}')
    print(usuario_data_nascimento)
    # Adiciona ao Dicionario
    dic_usuario['DATA DE NASCIMENTO'] = usuario_data_nascimento

    print('-' * 50)
    usuario_logradouro = input('Digite o Logradouro : ')
    usuario_numero_casa = input('Digite o Número da Casa : ')
    usuario_bairro = input('Digite o Bairro : ')
    usuario_cidade = input('Digite a Cidade : ')
    usuario_estado = input('Digite o Estado, usando apenas a sigla : ')
    # VERSAO DICIONARIO : [inativada]
    # usuario_endereco = {'Logradouro': usuario_logradouro,'Numero': usuario_numero_casa,'Bairro': usuario_bairro, 'Cidade': usuario_cidade, 'Estado': usuario_estado}

    # VERSAO STRING:
    usuario_endereco = (
        f'{usuario_logradouro} {usuario_numero_casa} {usuario_bairro} {usuario_cidade} {usuario_estado}')
    # Adiciona ao Dicionario
    print(usuario_endereco)
    print(usuario_data_nascimento)
    dic_usuario['ENDERECO'] = usuario_endereco

    # print(dic_usuario)
    # lista_dicionario.append(usuario_cpf)
    lista_dicionario.append(dic_usuario)
    print('---------------- USUARIO CRIADO -------------')
    print('---------------------------------------------')

    print(usuario_cpf)

    # Converter lista em dicionário (CPF - resto dos dados)
    usuarios = {}
    for usuario in lista_dicionario:
        cpf = usuario['CPF']
        usuarios[cpf] = usuario
    ## Em Forma de Compreensão:
    # usuarios = {usuario['CPF']: usuario for usuario in lista_dicionario}
    print(usuarios)
    print(usuarios[usuario_cpf])
    print('---------------------------------------------')
    return ()

#
#
##################### CADASTRAR CONTA CORRENTE
#
#
def cadastrar_conta(agencia, conta):
    cpf = input("Coloque o CPF do Usuario: ")
    # print(lista_dicionario)
    for usuario in lista_dicionario:
        if cpf == usuario["CPF"]:
            print("USUARIO ENCONTRADO NO SISTEMA, CRIANDO CONTA:")

            # Como achou, Vamos incrementar o nmero da Conta!
            conta = len(lista_contas)+1
            # Vai criar a lista com o dicionario!
            lista_contas.append({"agencia": agencia, "conta": conta, "cpf": cpf})
            print(f"CONTA DE NUMERO {conta} CRIADA NA agencia {agencia} PARA O USUARIO DE CPF {cpf}")
            print('---------------------------------------------')
            print('---------------- CONTA CRIADA ---------------')
            print('---------------------------------------------')
            print(lista_contas)
            return True

    print("Conta Não Pôde ser Criada. Usuário Não Existe nao Banco")
    return False
#
#
##################### CADASTRAR CONTA CORRENTE
#
#
def listar_usuarios():
    print('----------------------LISTAR USUARIOS COM CONTAS---------------------------------------')
    #print(lista_dicionario)
    #print(lista_contas)
    for usuario in lista_dicionario:
        for conta in lista_contas:
            if(conta['cpf'] == usuario['CPF']):
                print('CPF =',usuario["CPF"], ' - TITULAR =', usuario["NOME"], ' - AGENCIA =', conta['agencia'],' - CONTA = ', conta['conta'])
            #print(conta['cpf'])
        #print(usuario["CPF"],' - ',usuario["NOME"])

    print('--------------------------------------------------------------------------------------')
    escolha_listar = input('--- DESEJA VISUALIZAR TODOS OS USUÁRIOS DO SISTEMA?   [s]/[n]---')
    if escolha_listar == 's':
        print('----------------------LISTAR TODOS OS USUARIOS---------------------------------------')
        for usuario in lista_dicionario:
            print('CPF =', usuario["CPF"], ' - TITULAR =', usuario["NOME"])
        print('----------------------------------------------------------------------------------')

#
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
    numero_agencia = "0001"
    inicia_conta = 0
    data_hoje = dia_atual()

    while True:
        escolha = tela_start()
        if (escolha == '1'):
            print('-Chama Tela de Login-')
            login_realizado = tela_login()
            if login_realizado != False:
                print('LOGOU!', login_realizado, '|', perfil_adm)

                # Sair é a Boolean para quebrar o loop de Logado
                sair = False

                while True and sair == False:
                    ################## SE ESTIVER NO PERFIL DE ADMIN


                    if login_realizado == perfil_adm:
                        escolha_func = menu_funcionario()

                        if escolha_func == 'u':
                            # [u] = Cadastrar Novo Usuario
                            cadastrar_usuario()
                            ############

                        elif escolha_func == 'c':
                            # [c] = Criar Conta Corrente
                            conta = len(lista_contas) + 1
                            # print('CONTA ====',conta)
                            cadastrar_conta(numero_agencia,conta)
                            print('Lista Contas',lista_contas)

                        elif escolha_func == 'l':
                            # [l] = Listagem de Usuários
                            listar_usuarios()

                        elif escolha_func == 'q':
                            # [q] = Volta pra Tela Principal
                            print('-------------SAINDO PARA TELA PRINCIPAL ------------')
                            sair = True
                        else:
                            print('-------ESCOLHA FORA DO ESCOPO! TENTE NOVAMENTE! ----------')


                    ################## SE ESTIVER NO PERFIL DE CLIENTE
                    else:
                        while True and sair == False:
                            escolha_cliente = menu_cliente(data_hoje,login_realizado)
                            if escolha_cliente == 'd':
                                # [d] = DEPOSITAR
                                print('')
                                ############

                            elif escolha_cliente == 's':
                                # [s] = SACAR
                                print('')

                            elif escolha_cliente == 'e':
                                # [e] = EXTRATO BANCÁRIO
                                print('')

                            elif escolha_cliente == 'q':
                                # [q] = Volta pra Tela Principal
                                print('-------------SAINDO PARA TELA PRINCIPAL ------------')
                                sair = True
                            else:
                                print('-------ESCOLHA FORA DO ESCOPO! TENTE NOVAMENTE! ----------')
            else:
                print('Deu Erro no Login...')
            # Caso Escolha seja = 1, Vai pedir login e senha ;

        elif (escolha == 'q'):
            print('-Encerrando Atendimento, Desligando Terminal')
            sys.exit()
        else:
            print('Tecla Não Suportada, Insira Novamente')


############

main()
