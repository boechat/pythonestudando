## Classe Retangulo
# Crie uma classe que modele um retangulo:
## ATRIBUTOS : Base e Altura
## Métodos: Mudar valor dos lados | Retornar valor dos lados | Calcular área | Calcular Perimetro
## Crie um programa que utilize esta classe. Ele deve pedir ao usuario que informe as medidas de um
# local. Depois, deve criar um objeto com as medidas e calcualr a quantidade de pisos e de rodapés
# necessárias para o local

##################################################################################################


class Retangulo:
    def __init__(self, base, altura):
        self._tam_base = base
        self._tam_alt = altura

    def mudarValorLado(self):
        escolha= int(input('''
        DIGITE A OPÇÃO:
        [1] Mudar valor da BASE
        [2] Mudar valor da ALTURA
        [3] Mudar valor da BASE E ALTURA
        '''))
        if escolha == 1:
            n_base = input('Entre com o novo valor de Base')
            self._tam_base = n_base
        elif escolha ==2:
            n_altura = input('Entre com o novo valor de Altura')
            self._tam_alt = n_altura            
        elif escolha ==3:
            n_base = input('Entre com o novo valor de Base')
            self._tam_base = n_base
            n_altura = input('Entre com o novo valor de Altura')
            self._tam_alt = n_altura
        else:
            print('\nValor Inválido, nada Será Alterado\n')
    
            
    def mostraTamanhoLado(self):
        print('\n - Mostrar Tamanho dos Lados - \n')
        print(f'O tamanho da base é {self._tam_base} e da altura é {self._tam_alt}')


    def calcularArea(self):
        print('\n - Calculo da Area do Retangulo - \n')
        area = int(self._tam_alt)*int(self._tam_base)
        print('A área do retângulo é de : ', area)
        return area

    def calcularPerimetro(self):
        # Soma de todos os lados do Retangulo
        print('\n - Calculo do Perimetro do Retangulo - \n')
        peri = (int(self._tam_alt)*2)+(int(self._tam_base)*2)
        print('O perímetro do retangulo é de : ', peri)
        return peri
        
        
ba = int(input('Entre com o tamanho da base do retangulo em cm: '))
alt = int(input('Entre com o tamanho da altura do retangulo em cm: '))
ret = Retangulo(base=ba,altura=alt)

print('---------')
ret.mostraTamanhoLado()
ret.mudarValorLado()
ret.mostraTamanhoLado()
ret.calcularArea()
ret.calcularPerimetro()


