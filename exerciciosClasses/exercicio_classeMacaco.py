#############################################################################################################

### Classe Macaco
# Desenvolva uma classe Macaco que possua:
## ATRIBUTOS: Nome | Bucho
## METODOS: Comer | verBucho | Digerir.
##
## Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos
## 3 alimentos diferentes e verificando o conteudo do estomago a cada refeição.
## Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
import random 

class Macaco:
    def __init__(self,nome,bucho = None):
        self.nome = nome
        self.bucho = [] if bucho is None else bucho
    
    def comer(self,alimento):
        print(f'Comendo {alimento}...')
        self.bucho.append(alimento)

    
    def ver_bucho(self):
        print(f'Vamos ver o Buchinho do {self.nome} ...')
        for item,i in enumerate(self.bucho):
            print(f'Indice:{item} / Comida: {self.bucho[item]}')
    
    def digerir(self):
        print(f'Minha barriguinha dói, vou defecar...')
        self.bucho.pop(0)

alimentos = ['banana','maçã','uva','coco','margarida','limão','caqui']
mac1 = Macaco('leo')
mac2 = Macaco('tião')

print(mac1.nome,mac1.bucho)

for i in range(0,3):
    print(f'================ITERACAO {i} ====================')
    numero = random.randint(0, len(alimentos)-1)
    alimento = alimentos[numero]
    print(f'-------{mac1.nome}--------')
    mac1.comer(alimento)
    numero = random.randint(0, len(alimentos)-1)
    alimento_mac2 = alimentos[numero]
    print(f'-------{mac2.nome}--------')
    mac2.comer(alimento_mac2)

mac2.comer(mac1.nome)

print('---------------------------------')
mac1.ver_bucho()
('---------------------------------')
mac2.ver_bucho()
