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

########################################################################################################################

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    # ATRIBUTOS :     endereco : str ;   contas : list ;
    def __init__(self, endereco):
        self.endereco = endereco
        self. contas = []
    # METODOS   :     realizar_transacao(conta : Conta, transacao : Transacao)  ;   adicionar_conta(conta : Conta)

    def realizar_trasacao(self, conta, transacao):
        # chama interface ; registrar(conta : Conta)
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    # cpf : str ; # nome : str ;  # data_nascimento : date
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)          #puxa de Cliente
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

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

                         -----------------------------------------------------------
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
               --------------------- SISTEMA BANCÁRIO ---------------------

                AGENCIA:    {self.agencia}
                C.C.:       {self.numero}
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
                'data': datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
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
        self._valor = valor\
   @property
   def valor(self):
       return self._valor

   def registrar(self,conta):
      sucesso_transacao = conta.depositar(self.valor)
      if sucesso_transacao:
          conta.historico.adicionar_transacao(self)
