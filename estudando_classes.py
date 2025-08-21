### O Paradigma de programação orientada a objetos estrutura o código abstaraindo problemas em objetos do mundo real,
### facilitando o entendimento do código e tornando-o mais MODULAR e EXTENSIVEL.
### CONCEITOS CHAVES:  CLASSES E OBJETOS
### Repositorio de consulta: https://github.com/digitalinnovationone/trilha-python-dio



### CONCEITOS DE CLASSES E OBJETOS ###

##
class Cachorro:
    def __init__(self,nome,cor,acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print('Au au')

    def dormir(self):
        self.acordado = False
        print('ZZZZZZZZZZZZZ')

caozinho = Cachorro('Bolt','branco')
caozao = Cachorro('Azazel','vermelho',acordado = False)
print(caozinho.nome)
caozinho.latir()
print(caozao.nome,caozao.cor)
caozao.dormir()


#########################
# JOAO TEM UMA BICICLETARIA E GOSTARIA DE REGISTRAR AS VENDAS DE SUAS BICICLETAS.
# CRIE UM PROGRAMA ONDE JOAO INFORME:
# COR , MODELO, ANO e VALOR da bicicleta vendida.
# UMA BICICLETA PODE:
# BUZINAR, PARAR e CORRER; adicione esses comportamentos!

print('-----------------------------------------------------------------------\n')
class Bicicleta:
    def __init__(self, cor, modelo,ano,valor,movimento = False,marcha = 1):
        self.cor = cor
        self.modelo = modelo
        self.ano = int(ano)
        self.valor = float(valor)
        self.movimento = False
        self.marcha = marcha
    def buzinar(self):
        print('blimblimblim')

    def parar(self):
        print('Freios em dia! Prrrrrrrrr')
        movimento = False

    def correr(self):
        print('Voaaaaaaa menino!')
        movimento = True

    def estado(self,movimento):
        if movimento == True:
            print('Está Andando')
        else:
            print('Está Parada')

    def trocar_marchar(self, nro_marcha):
        print('Trocando Marcha...  MARCHA', nro_marcha)
        print('Marcha Anterior: ', self.marcha)

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                self.marcha = self.marcha + 1
                print('Marcha Trocada', self.marcha)
            else:
                print('Não consigo trocar a marcha', self.marcha, nro_marcha)

        _trocar_marcha()


    ## PRA EXIBIR A INSTANCIA , no caso print(bike)
    def __str__(self):
        ## Manualmente:
        # return f'Bicileta : COR {self.cor}, MODELO {self.modelo}, ANO {self.ano}, VALOR {self.valor}'

        #return f'{self.__class__.__name__}'  # Diz o nome da Classe

        #return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"  # Itera pra mostrar todos os atributos(items) da classe Bicicleta presentes no dicionario

        return f"{self.__class__.__name__}: {[', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())]}" # aplicando o join com a virgula e espaço

bike = Bicicleta('azul','Italiano',2020,385)
print('Bicileta está em movimento? :',bike.movimento,'\n')
print('Chamar MÉTODO ESTADO da classe bike :')
bike.estado(bike.movimento)

print(bike.cor, bike.ano, bike.valor)
# Com o __str__ definido
print('----------',bike,'----------')

print('MARCHA ANTES : ',bike.marcha)
print('TROCANDO MARCHA\n')
bike.trocar_marchar(3)
print('------------')
print('MARCHA AGORA : ',bike.marcha)
