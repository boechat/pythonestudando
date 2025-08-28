#############################################################################################################

### Classe Ponto e Retangulo
# Possua uma classe chamado Ponto, com os atributos x e y 
# Possua uma classe chamado Retangulo, com atributos LARGURA e ALTURA
# Voce deve criar alguns objetos da classe Retangulo 
# Cada objeto deve ter um vértice de partida, por exemplo, vertice inferior esquerdo do retangulo que deve 
# ser um objeto da classe Ponto 
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que
# indique os valores de x e y para o centro do objeto 
# O valor do centro do objeto deve ser mostrado na tela 
# Crie um MENU para alterar os valores do retângulo e imprimir o centro desse retangulo.

class Ponto:
    def __init__(self,x : int, y : int):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'    
        
class Retangulo:
    def __init__(self,largura : int, altura : int, vertice = Ponto):
        self.largura = largura
        self.altura = altura
        self.vertice = vertice
        
    def retorna_centro(self):
        x_centro = self.vertice.x + self.largura / 2
        y_centro = self.vertice.y + self.altura / 2
        return Ponto(x_centro,y_centro)
    
    def alterar_valores(self):
        larg = int(input('Entre com a nova largura'))
        alt = int(input('Entre com a nova altura'))
        self.largura = larg 
        self.altura = alt
        
    def __str__(self):
        return f"Retângulo: largura={self.largura}, altura={self.altura}, vértice={self.vertice}"

def menu(reta):
    while True:
        print(f'''
        ------------------------------
        ---------- MENU --------------
        1) Alterar Valores do Retângulo
        2) Imprimir Centro do Retangulo
        3) Sair
        ------------------------------
        ''')
        escolha = int(input('Digite a opção'))
        if escolha == 1:
            reta.alterar_valores()
        elif escolha == 2:
            print(f'\n CENTRO DO RETÂNGULO: {reta.retorna_centro()}')
        else:
            print(f'!!!FIM!!!!')
            break


##########              PRINCIPAL           ##################
pontoret1 = Ponto(x = 4, y = 2)
ret1 = Retangulo(largura = 12, altura = 10, vertice = pontoret1 )


menu(ret1)
