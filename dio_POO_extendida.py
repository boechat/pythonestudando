############         Variaveis de Classe e de Instancia

class Estudante:
    escola = 'DIO'                      # esse atributo é combartilhado, portanto variavel de Classe

    def __init__(self,nome,numero):
        self.nome = nome                # Variavel de Isntancia
        self.numero = numero

    def __str__(self):
        return f'{self.nome} - {self.numero} - {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

gui = Estudante('Guilherme', 56451)
gio = Estudante('Giovanna', 172323)
print(gui)
print(gio)
gui.numero = 3
print('\n Depois de trocar os Valores\n')
mostrar_valores(gui,gio)
aluno_3 = Estudante('Chaps',4)
print('\n Depois de adicionr Chaps \n')
mostrar_valores(gui,gio,aluno_3)

print('====================\n METODOS DE CLASSE E METODOS ESTATICOS \n====================')

############         Métodos de Classe e Métodos Estáticos
#
# Métodos de Classe estão ligados à classe e não ao objeto. Tem acesso ao estado da classe pois recebem um parametro que aponta para a classe e nao para a instancia do objeto
# Métodos Estáticos não recebem um primeiro argumento explicito. É um metodo vinculado à classe e não ao objeto da classe. Esse método não pode acessar ou modificar o estado da classe.
# Está Presente em uma classe porque faz sentido.

# Método de Classe recebe um primeiro parametro que aponta para a classe, enquanto um método Estitaco nao
# Metodo de Classe pode acessar ou modificar o estado da classe enquanto um metodo estatico não.

# Quando utilizar?
# Classe -> pra criar métodos de fábrica (Retornam instancias da classe)
# Estatico -> criar Funções utilitárias  (Validação por exemplo)

#EXEMPLO:

class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nasc(cls,ano,mes,dia,nome):
        print(cls)
        idade = 2025 - ano
        return cls(nome,idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa('Guilherme',28)
print(p.nome, p.idade)

a = Pessoa.criar_apartir_data_nasc(1945,4,21,'Bruna')

print(a.nome, a.idade)

print(a.e_maior_idade(a.idade))
print(Pessoa.e_maior_idade(10))



############         INTERFACES / CLASSES ABSTRATAS
print('====================\n INTERFACES / CLASSES ABSTRATAS \n====================')

## O que São INTERFACES ?
# Definem o que uma classe deve FAZER e não como
#
## Classes Abstrata
#
# Criando Classes Abstratas usando o Modulo ABC
# ABC = funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata.
# Um método se torna abstrato quando decorado com @abstractmethod

from abc import ABC, abstractmethod, abstractproperty  # pra usar o modulo ABC


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    # Por ser abstract, me obriga a fazer os mesmos metodos
    def ligar(self):
        print('Ligando')

    def desligar(self):
        print('DESLigando')

    @property
    def marca(self):
        return 'LG'

controle = ControleTV()
controle.ligar()
print(controle.marca())
