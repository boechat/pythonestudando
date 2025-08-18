#### Solução mais clean do Desafio.
## Para a minha solução (em andamento) mais complexa, checar pythonestudado/desafio_sistema_bancario_dio_3.py
#
####################################### DESAFIO:
##################### SISTEMA BANCÁRIO PARTE 2 - OTIMIZANDO O SISTEMA BANCÁRIO COM FUNÇÕES PYTHON ############################
# Continuar o desafio do Sistema Bancário, adicionando
#
### OBJETIVO GERAL 
# Separar as funções existentes de Saque, Depósito e Extrato em Funções;
# Criar duas novas funções: Cadastrar Usuário (Cliente) e Cadastrar Conta Bancária
#
### DESAFIO
# Deixar o código mais modularizado, para isso criar funções para as operações Existintes: 
# Sacar, Depositar e Extrato. Além disso, precisamos criar duas novas funções: Criar Usuário e 
# Criar Conta Corrente (Vincular com Usuario)
#
### Separação em funções
# Para exercitar, cada função VAI TER UMA REGRA NA PASSAGEM de argumentos. 
#
########
## FUNÇÃO SAQUE
# Deve receber os argumentos APENAS  POR NOME (keyword only)
# Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
# Sugestão de retorno: saldo e extrato
#
## FUNÇÃO DEPÓSITO
# Deve receber o argumentos APENAS POR POSIÇÃO (position only);
# Sugestão de argumentos: saldo, valor, extrato
# Sugestão de retorno: saldo e extrato
#
## FUNÇÃO EXTRATO
# Deve receber os argumentos por posição e nome (postional only e keyword only)
# Argumentos posicionais: saldo
# Argumentos nomeados: extrato
#
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
###########################################################################################################################
############ LISTAS
lista_usuarios = [] #lista de usuarios
lista_contas = []

############ FUNÇÃO SAQUE  (* ARGS)
def saque(*, saldo, valor_saque, extrato, limite, qtd_saques, limite_saq):

    # VERIFICA QTD SAQUES E VALOR SAQUE
    if (qtd_saques < 3 and valor_saque <= 500):
        if (saldo - valor_saque >=0):
            saldo = saldo - valor_saque
            qtd_saques = qtd_saques + 1
          
            extrato += f"Saque    R${valor_saque:.2f}\n"
            print(f"Saque realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
          
        else:
            print("Saldo insuficiente. Operação não realizada.")
    else:
        if (qtd_saques >= 3):
            print(f"Numero de {limite_saq} Saques ultrapassou o Limite. Encerrar Operação.")
        elif (qtd_saques > 500):
            print(f"Valor Limite  R${limite:.2f} de Saque Excedido. Encerrar Operação.")     

    return saldo, extrato, qtd_saques


############ FUNÇÃO DEPOSITO  (Positional)
def deposito(saldo, deposito, extrato, /):
    
    if (deposito > 0):
        saldo = saldo + deposito
        extrato = extrato + f"Depósito R${deposito:.2f}\n"
        print(f"Depósito Feito!\n Saldo Atual: R${saldo:.2f}")
    else:
        print("Valor de deposito não permitido. Operação não realizada.")
    return saldo, extrato

########## FUNCAO EXTRATO (posicao e keyword)
def func_extrato(saldo, /, *, extrato):
    print("Extrato\n",extrato)
    print(f"Saldo: R${saldo:.2f}")

########## FUNCAO CADASTRO DE USUARIOS
def cadastrar_usuario(lista_usuarios):
    cpf = input("Coloque o CPF a ser Cadastrado : ")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            print("Usuario já consta, não pode haver duplicatas no sistema. Prosseguir sem Cadastrar.")
            return
    nome = input("NOME: ")
    data_nascimento = input("DATA DE NASCIMENTO: ")
    endereco = input("ENDEREÇO: ")
    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\\---------------------\nUsuário Criado\n---------------------\\")

########## FUNCAO CADASTRO DE CONTAS
def cadastrar_conta(agencia, conta, lista_usuarios, lista_contas):
    cpf = input("Coloque o CPF do Usuario: ")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            print("USUARIO ENCONTRADO NO SISTEMA, CRIANDO CONTA:")
            lista_contas.append({"agencia": agencia, "conta": conta, "cpf": cpf})
            print(f"CONTA DE NUMERO {conta} CRIADA NA agencia {agencia} PARA O USUARIO DE CPF {cpf}")
            return lista_contas
        else:
            print("Conta Não Pôde ser Criada. Usuário Não Existe nao Banco")
            return lista_contas


menu = """
===== OPERACOES DE USUARIO =====
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair
=====  OPERACOES DE ADMIN ======
[nu] Novo Usuário
[lu] Listar Usuários
[nc] Nova Conta
[lc] Listar Contas
[q]  Sair

=> """

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
limite_saq = 3
agencia = "0001"

while True:

    opcao = input(menu)

    if opcao == "d":
        print("==== DEPOSITAR ====")
        valor_deposito = float(input("Qual o valor a ser depositado?: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)
    
    elif opcao == "s":
        print("==== SACAR ====")
        valor_saque = float(input("ENTRE COM O VALOR A SER SACADO: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, qtd_saques=qtd_saques, limite_saq=limite_saq)  

    elif opcao == "e":
        func_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        print("==== Cadastrar Novo Usuário ====")
        cadastrar_usuario(lista_usuarios)
    
    elif opcao == "lu":
        print("==== Listar Usuários ====")
        print(lista_usuarios)
    

    elif opcao == "nc":
        print("==== Cadastrar nova conta ====")
        conta = len(lista_contas) + 1
        cadastrar_conta(agencia, conta, lista_usuarios, lista_contas)

    elif opcao == "lc":
        print("==== Listar Contas ====")
        print(lista_contas)

    elif opcao == "q":
        break
