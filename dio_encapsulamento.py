######### Encapsulamento
#
### O que é?
# Proteção de Acesso; Agrupar dados e os métodos que manipulam em uma unidade. Impõe restrições ao acesso direto a variaveis e métodos;
# Evita modificaçõ acidental.
# Assim, a variavel de um objeto só pode ser alterada pelo método desse objeto.
#
# Ex: Dentro da classe conta eu tenho atributo saldo e metodo depositar e sacar; só consigo mexer em saldo atrvés dos métodos.
#
### RECURSOS PUBLICOS E PRIVADOS
# Em C++ e Java, existem palavras reservadas para definir o nivel de acesso aos atributos.
# Em PYTHON NÃO temos palavras reservadas, porem usamos CONVENÇÕES no nome do recurso para definir se a var é public ou private
# Publico -> pode ser acessado fora da classe
# Private -> só pode ser acessado pela classe
#
# Todos os recursos são públicos em python, a menos que o nome inicie com Underline
# Ex:
class Conta:
    def __init__(self, numero_da_agencia, saldo = 0):
        self._saldo = saldo   # _saldo é privado!
        self.numero_da_agencia = numero_da_agencia
    def deposita(self,valor):
        self._saldo += valor
        print(f'Depósito de : R$ {self._saldo:,.2f}')
        print(f'Saldo Atual: R$ {self._saldo:,.2f}')

    def saca(self,valor):
        self._saldo -= valor
        print(f'Saque de : R$ {self._saldo:,.2f}')
        print(f'Saldo Atual: R$ {self._saldo:,.2f}')

    def mostra_saldo(self,):
        print('Mostrando Saldo...')
        return self._saldo

conta_user =Conta('0001',10)
print(conta_user.numero_da_agencia)
print(conta_user._saldo) # Dessa forma não deve ser acessado, apesar de podermos!

conta_user.deposita(545.50)
print('-----')
conta_user.saca(320.23)
print(conta_user.mostra_saldo())

print('\n----------------------------------------\n')
#
### PROPRIEDADES
#
## Para que Servem?
# Com o property() você pode criar ATRIBUTOS GERENCIADOS em suas classes; Você pode usar propriedades quando precisar
# modificar sua implementação interna sem alterar a API publica da Classe
#
#
class Foo:
    def __init__(self, x= None):
        self._x = x

    @property                   # Decorador , função que executa antes da função
    def x(self):
        return self._x or 0

    @x.setter                    # Atribuição da MODIFICAÇÃO (SETTER)
    def x(self,value):
        _x = self._x or 0
        _value = value or 0
        # Retornar soma do valor + x
        self._x = _x + _value

    @x.deleter                  # Delete
    def x(self):
        self._x = -1

#######################
foo = Foo(10)
print('x ',foo.x)
foo.x = 10
print('x ',foo.x)
del foo.x
print('x ',foo.x)

######################################### EXEMPLO PESSOA
print('\n-----------------------\n')

class Pessoa:
    def __init__(self,nome,ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome


    @property
    def idade(self):
        _ano_atual = 2025
        _idade = _ano_atual - self._ano_nasc
        return _idade

haroldo = Pessoa('Haroldo',1985)
print(haroldo.nome,'---',haroldo.idade)

print(haroldo.nome)
