############ HERANCA #############

#### HERANCA EM POO #####
# Capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pai

#### BENEFICIOS
# Reutilização de codigo; nao precisa repetir. Permite adicionar mais recursos a uma classe sem modifica-la
##
# De natureza transitiva, se a classe B herda de A, todas as subclasses de B herdarao de A
##

class Animal:
    def __init__(self,patas,rabo,som):
        self.patas = patas
        self.rabo = rabo
        self.som = som

    def __str__(self):
        return f"{self.__class__.__name__}: {[', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())]}" # aplicando o join com a virgula e espaço

    def sonoro(self,som):
        print('Eu emito som :',som)

    def membros(self,patas):
        print('Tenho Patas!',patas)

class Super(Animal):
    def __init__(self,patas,rabo,som):
        super().__init__(patas,rabo,som)
        self.poderes = []

    def adicionar_poder(self,poder):
        self.poderes.append(poder)
        print(f'Poder {poder} Registrado!')

    def usar_poder(self,poder):
        if poder in self.poderes:
            print('Usando o Poder: ',poder)
        else:
            print('Não Tenho esse poder... ainda!')


rajado = Animal(4,1,'Miado')
kripto = Super(4,3,'Latidão')
kripto.sonoro(kripto.som)
kripto.membros(kripto.patas)

kripto.adicionar_poder('Trovoada')
kripto.usar_poder('Trovão')


###################### HERANCA SIMPLES E HERANCA MULTIPLA
## Simples -> Uma filha herda de um Pai
## Multipla -> Uma filha herda de várias classes Pais
#Ex: Class Ornitorrinco(Mamífero,Ave):


############# EXEMPLO HERANCA SIMPLES ################
print('\n\n############# EXEMPLO HERANCA SIMPLES ################\n\n')

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # METODOS
    def ligar_motor(self):
        print('Ligando o Motor!')

    def __str__(self):
        return f"{self.__class__.__name__}: {[', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())]}"

class Motocicleta(Veiculo):
    def corrida(self):
        print('Bora correr!')



class Carro(Veiculo):
    def taxi(self):
        print('Virei uber')



class Caminhão(Veiculo):
    def __init__(self,cor,placa,numero_rodas,carregando):
        super().__init__(cor,placa,numero_rodas)
        self.carregando = carregando

    def esta_carregado(self):
        print(f"{'Sim' if self.carregando else 'Nao'} estou carregado")

    def carregar(self):
        print('Bora Carregar essa Carga!!! Carregando == ',self.carregando)
        self.carregando = True
        print(f'To Carregado! Carregando == {self.carregando}')
    def desaparecer(self):
        print('Peguei uma Carona...')


moto= Motocicleta('vermelha',23232,2)
#print(moto.__class__.__name__)
moto.ligar_motor()
moto.corrida()
carro = Carro('branco','x32323232',4)
carro.ligar_motor()
carro.taxi()
print('\n------CAMINHAO SUB CLASS --------\n')
caminhao = Caminhão('amarelo','YYYY',8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.desaparecer()
caminhao.esta_carregado()
caminhao.carregar()
caminhao.esta_carregado()
