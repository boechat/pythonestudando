## Classe Quadrado
# Crie uma classe que modele um quadrado:
## ATRIBUTOS : Tamanho do lado 
## Métodos: Mudar Valor do Lado, Retornar Valor do Lado e Calcular Area

##################################################################################################


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self._tamanho_do_lado = tamanho_do_lado

    def mudarValorLado(self,novo_tamanho):
        print('\n - Trocar Tamanho do Lado - \n')
        print(f'Tamanho a ser alterado: {self._tamanho_do_lado} ; NOVO TAMANHO : {novo_tamanho}')
        self._tamanho_do_lado = novo_tamanho
        
    def mostraTamanhoLado(self):
        print('\n - Mostrar Tamanho do Lado - \n')
        print('O tamanho do lado do quadrado é de : ',self._tamanho_do_lado)
        return self._tamanho_do_lado

    def calcularArea(self):
        print('\n - Calculo da Area do Quadrado - \n')
        area = int(self._tamanho_do_lado)**2
        print('A área do quadrado é de : ', area)
        return area

lado = input('Entre com o tamanho do lado do quadrado em cm: ')
quad = Quadrado(lado)

print('---------')
quad.mostraTamanhoLado()
quad.mudarValorLado('15')
quad.mostraTamanhoLado()
quad.calcularArea()
