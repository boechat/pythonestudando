### OBJETIVO GERAL ###

# Iniciar a modelagem do sistema bancário em POO.
# Adicionar CLASSES para cliente e as operações bancárias: DEPÓSITO e SAQUE
# Atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
# Código deve seguir o modelo de classes UML:

# Classe Conta:
## precisa ter privados:
# saldo - float
# numero - int
# agencia - str
# cliente : Cliente
# historico : Historico
## 4 Métodos:
# saldo() : float
# nova_conta(cliente: Cliente, numero : int) : Conta
# sacar (valor: float) : bool
# depositar (valor : float) : bool

# Classe ContaCorrente (filha de Classe Conta)
# possui atributos privados:
# limite : float
# limite_saques : int

# Classe Historico            -> Toda conta tem um historico
# método adicionar_transacao(transaco : Transacao)

# Classe Transacao ->           Abstrata Interface

# Classe Deposito
# implementa Interface
# valor : float

# Classe Saque
# implementa Interface
# valor : float

# Classe Cliente
# endereço : str
# contas : list
## 2 METODOS
# realizar_transacao(conta: Conta, transacao : Transacao)
# adicionar_conta (conta : Conta)

# Classe PessoaFisica
# cpf :str
# nome : str
# data_nascimento : date

### ### ### ### ### ### ### ### ### DESAFIO EXTRA: ### ### ### ### ### ### ### ### ### ###
# Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que
# tratam as opções do menu, para funcionarem com as classes modeladas

###################################

# Incorporado elementos do desenvolvimento do Desafio 1 ; 2 e 3 !

########################################################################################################################

###################################################################### IMPORTS ######################################################################
import calendar
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

###################################################################### CLASSES ######################################################################

class Cliente:
    # ATRIBUTOS :     endereco : str ;   contas : list ;
    def __init__(self, endereco):
        self.endereco = endereco
        self. contas = []
    # METODOS   :     realizar_transacao(conta : Conta, transacao : Transacao)  ;   adicionar_conta(conta : Conta)

    def realizar_transacao(self, conta, transacao):
        # chama interface ; registrar(conta : Conta)
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    # cpf : str ; # nome : str ;  # data_nascimento : date
    def __init__(self, nome, data_nascimento, cpf, endereco, data_criado):
        super().__init__(endereco)          #puxa de Cliente
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.data_criado = data_criado

class Conta:
    # Atributos: saldo - float  ; # numero - int ; # agencia - str  ;  # cliente : Cliente ; # historico : Historico
    ## Métodos:  # saldo() : float ;  # nova_conta(cliente: Cliente, numero : int) : Conta   # sacar (valor: float) : bool   # depositar (valor : float) : bool
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()       # Puxa a Classe Historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        limite_do_saldo = valor > saldo

        if limite_do_saldo:
            print(f'''
--------------------- FALHA DE SAQUE -----------------------
            
Saldo insuficiente para o saque de R$ {valor}
Valor disponível para Saque é de R$ {saldo}
            
------------------------------------------------------------
''')

        elif valor > 0:
            self._saldo = self._saldo - valor
            print(f'''
--------------------- SAQUE REALIZDO -----------------------
            
Saque Realizdo no Valor de R$ {valor}
            
 ------------------------------------------------------------
''')
            return True
        else:
            print(f'''
--------------------- FALHA DE SAQUE  -----------------------

Falha ao realizar o Saque Pretendido.
Valor de R$ "{valor}" não é suportado.
Verifique e tente novamente

------------------------------------------------------------
''')
            return False

    def depositar(self,valor):
        if valor > 0:
            self._saldo = self._saldo + valor
            saldo_atual = self._saldo
            print(f'''
------------------ DEPÓSITO REALIZADO  --------------------

Depósito de R$ {valor} realizado!
Saldo Atual de R$ {saldo_atual}

-----------------------------------------------------------
''')
            return True
        else:
            print(f'''
------------------ FALHA NO DEPÓSITO  ---------------------

Erro ao Depositar Quantia! Verifique os valores e 
tente novamente!

----------------------------------------------------------
''')
            return False

class ContaCorrente(Conta):
    # limite : float    ;   # limite_saques: int
    def __init__(self, numero, cliente, limite = 500, limite_saques =3 ):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self,valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print(f'''
--------------------- FALHA DE SAQUE CC ---------------------

       Falha ao realizar o Saque Pretendido.
       Valor de R$ "{valor}" ultrapassou o Limite Permitido
       Verifique e tente novamente.

------------------------------------------------------------            
''')
        elif excedeu_saques:
            print(f'''
--------------------- FALHA DE SAQUE CC ---------------------

        Falha ao realizar o Saque Pretendido.
        Valor de R$ "{valor}" Excedeu a Quantidade de
        Saques Diárias.
        Tente Novamente Amanhã.

------------------------------------------------------------            
''')
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''
--------------------- SISTEMA BANCÁRIO ------------------

 AGENCIA:    {self.agencia}
 C.C.:       {self._numero}
 TITULAR:    {self.cliente.nome}

------------------------------------------------------------   
'''

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    # valor : float
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    # valor : float
   def __init__(self,valor):
        self._valor = valor

   @property
   def valor(self):
       return self._valor

   def registrar(self,conta):
      sucesso_transacao = conta.depositar(self.valor)
      if sucesso_transacao:
          conta.historico.adicionar_transacao(self)

###################################################################### FUNÇÔES ######################################################################



######################################################################  DATA  #####################################################################

# Busca Dia Atual
def dia_atual():
    hoje = datetime.now().strftime("%d/%m/%Y")
    return (hoje)

def ano_atual():
    hoje = dia_atual()
    ano = int(hoje.split("/")[2])
    return ano

###################################################################### CPF ######################################################################
def validar_cpf(cpf):
    # FUNCAO PRA VERIFICAR SE É OU NAO UM CPF VALIDO
    ### Verificacoes primarias
    # Verifica 11 dígitos, pegando o Tamanho
    if len(cpf) != 11:
        return False
    # Verifica se todos os Digitos sao iguais
    if cpf == cpf[0] * 11:
        return False

    ### Verificacoes especificas
    # Calcula o primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10
    # Calcula o segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10
    # Compara com os dígitos originais
    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

########################################################################################################################

def menu(data_hoje):
    menu = f"""
------------------ MENU ------------------
= - BEM VINDO !                          =
=   Data: {data_hoje}                    =
=   Agencia: 0001                        =
==========================================
=                                        =
=    [d]  Depositar                      =
=    [s]  Sacar                          =
=    [e]  Extrato                        =
=    [nc] Nova Conta                     =
=    [lc] Listar Contas                  =
=    [le] Listar Clientes                =
=    [nu] Novo Usuario                   =
=    [q]  Sair                           =
------------------------------------------
    =>"""
    return input(menu)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(f'''
--------------------- FALHA DE CONTA -----------------------

        Cliente Não Possui Conta no Sistema!
        Tente Outra ou Crie!

------------------------------------------------------------            
''')
    return cliente.contas[0]

def depositar(clientes):
    cpf = input(f'''
-------------------------- DEPOSITO -------------------------

ENTRE COM O CPF DO CLIENTE:

------------------------------------------------------------   
''')
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print(f'''
--------------------- FALHA - DEPOSITO ---------------------

FALHA AO ENCONTRAR CLIENTE:
Cliente não encontrado no sistema!

------------------------------------------------------------   
''')
        return

    valor = float(input(f'''
-------------------------- DEPOSITO ----------------------

Por Favor, Entre Com o valor a ser depositado:

------------------------------------------------------------   
'''))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input(f'''
-------------------------- SAQUE ---------------------------

    ENTRE COM O CPF DO CLIENTE:

------------------------------------------------------------   
''')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'''
--------------------- FALHA - SAQUE ------------------------

FALHA AO ENCONTRAR CLIENTE:
Cliente não encontrado no sistema!

------------------------------------------------------------   
''')
        return

    valor = float(input(f'''
---------------------------- SAQUE -------------------------

Por Favor, Entre Com o valor a ser Sacado:

------------------------------------------------------------   
'''))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input(f'''
-------------------------- EXTRATO -------------------------

ENTRE COM O CPF DO CLIENTE:

------------------------------------------------------------   
    ''')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'''
--------------------- FALHA - EXTRATO ------------------------

FALHA AO ENCONTRAR CLIENTE:
Cliente não encontrado no sistema!

------------------------------------------------------------   
''')
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print(f'''
------------------ EXTRATO BANCÁRIO ------------------------

''')
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = 'Nenhuma Transação Registrada no Período.'
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}:\n R$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\n SALDO :\n R$ {conta.saldo:.2f}")
    print('------------------------------------------------------------')

def criar_cliente(clientes):
    cpf = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O CPF DO CLIENTE:

------------------------------------------------------------   
''')
    cpf_validado = validar_cpf(cpf)
    cliente = filtrar_cliente(cpf_validado, clientes)

    if cliente:
        print(f'''
------------------ FALHA - CRIAR CLIENTE ---------------------

CLIENTE JÁ EXISTE NO SISTEMA! CPF DUPLICADO!

------------------------------------------------------------   
''')
        return

    usuario_nome = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O PRIMEIRO NOME DO CLIENTE:

------------------------------------------------------------   
''')
    usuario_sobrenome = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O SOBRENOME COMPLETO DO CLIENTE:

------------------------------------------------------------   
''')
    nome = (f'{usuario_nome} {usuario_sobrenome}')


    usuario_dia_nascimento = input(f'''
--------------------- CRIAR CLIENTE ------------------------

Digite o DIA em que Nasceu 

------------------------------------------------------------   
''')
    if int(usuario_dia_nascimento) < 10 and int(usuario_dia_nascimento) > 0 and len(usuario_dia_nascimento) != 2:
        usuario_dia_nascimento = (f'0{usuario_dia_nascimento}')
    if not usuario_dia_nascimento.isdigit() or int(usuario_dia_nascimento) <= 0 or int(usuario_dia_nascimento) >= 32:
        print(f'''
-------------- FALHA AO CRIAR CLIENTE ----------------------

Dados Invalidos, Intervalo informado não corresponde.

------------------------------------------------------------   
''')
        return False

    usuario_mes_nascimento = input(f'''
--------------------- CRIAR CLIENTE ------------------------

Digite o MÊS em que Nasceu 

------------------------------------------------------------   
''')
    if int(usuario_mes_nascimento) < 10 and int(usuario_mes_nascimento) > 0 and len(usuario_mes_nascimento) != 2:
        usuario_mes_nascimento = (f'0{usuario_mes_nascimento}')
    if not usuario_mes_nascimento.isdigit() or int(usuario_mes_nascimento) <= 0 or int(usuario_mes_nascimento) >= 13:
        print(f'''
        -------------- FALHA AO CRIAR CLIENTE ----------------------

        Dados Invalidos, Intervalo informado não corresponde.

        ------------------------------------------------------------   
        ''')
        return False

    usuario_ano_nascimento = input(f'''
--------------------- CRIAR CLIENTE ------------------------

Digite o ANO em que Nasceu 

------------------------------------------------------------   
''')
    ano = ano_atual()

    if not usuario_ano_nascimento.isdigit() or int(usuario_ano_nascimento) <= 1900 or int(
            usuario_ano_nascimento) >= ano:
        print(f'''
-------------- FALHA AO CRIAR CLIENTE ----------------------

Dados Invalidos, Intervalo informado não corresponde.

------------------------------------------------------------   
''')
        return False

    # Verifica se o dia de Nascimento está correto, verificando também ano bissexto
    qtd_dias = calendar.monthrange(int(usuario_ano_nascimento), int(usuario_mes_nascimento))[1]
    if int(usuario_dia_nascimento) > int(qtd_dias):
        print(f'''
-------------- FALHA AO CRIAR CLIENTE ----------------------

Dados Invalidos, Intervalo informado não corresponde.

------------------------------------------------------------   
''')
        return (False)
    data_nascimento = (f'{usuario_dia_nascimento}/{usuario_mes_nascimento}/{usuario_ano_nascimento}')

    usuario_logradouro = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O LOGRADOURO :

------------------------------------------------------------   
''')
    usuario_numero_casa = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O NÚMERO DO ENDEREÇO:

------------------------------------------------------------   
''')
    usuario_bairro = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM O BAIRRO:

------------------------------------------------------------   
''')
    usuario_cidade = input(f'''
--------------------- CRIAR CLIENTE ------------------------

ENTRE COM A CIDADE:

------------------------------------------------------------   
''')
    usuario_estado = input(f'''
--------------------- CRIAR CLIENTE ------------------------

DIGITE A SIGLA DO ESTADO:

------------------------------------------------------------   
''')
    endereco = (f'{usuario_logradouro} {usuario_numero_casa} {usuario_bairro} {usuario_cidade} {usuario_estado}')

    data_criado = dia_atual()

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento,cpf=cpf,endereco=endereco,data_criado = data_criado)
    clientes.append(cliente)

    print(f'''
--------------------- CRIAR CLIENTE ------------------------

                 CLIENTE CRIADO COM SUCESSO!
                 NOME: {cliente.nome}
                 DATA NASCIMENTO: {cliente.data_nascimento}
                 CPF: {cliente.cpf}
                 ENDERECO: {cliente.endereco}
                 DATA DE CRIAÇÃO DA CONTA: {cliente.data_criado}
                 
------------------------------------------------------------   
''')

def criar_conta(numero_conta, clientes, contas):
    cpf = input(f'''
--------------------- CRIAR CONTA ---------------------------

ENTRE COM O CPF DO CLIENTE:

------------------------------------------------------------   
''')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'''
------------------ FALHA - CRIAR CONTA ---------------------

FALHA AO ENCONTRAR CLIENTE:
Cliente não encontrado no sistema!

------------------------------------------------------------   
''')
        return

    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f'''
--------------------- CRIAR CONTA ---------------------------

                CONTA CRIADA CON SUCESSO!

------------------------------------------------------------   
''')

def listar_contas(contas):
    print('------------------- LISTAGEM DE CONTAS ---------------------------')
    achou = 0
    for conta in contas:
        achou += 1
        print('='*50)
        print(textwrap.dedent(str(conta)))
    if achou == 0:
        print('\n                          LISTA VAZIA !\n')
    print('------------------------------------------------------------------')

def listar_clientes(clientes):
    print('------------------- LISTAGEM DE USUARIOS ---------------------------')
    achou = 0
    for cliente in clientes:
        achou += 1
        print('CPF DO CLIENTE : ',cliente.cpf)
        print('NOME DO CLIENTE :',cliente.nome)
    if achou == 0:
        print('\n                          LISTA VAZIA !\n')
    print('------------------------------------------------------------------')

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu(data_hoje=dia_atual())

        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'le':
            listar_clientes(clientes)
        elif opcao == 'q':
            break



###################################################################### INICIA ######################################################################

main()
