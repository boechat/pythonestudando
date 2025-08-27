#####################################    DESAFIO DE CODIGO   ##########################################

###############################  MONITORAMENTO E VERIFICACAO COM POO ##################################

### Descrição
'''
Um sistema de monitoramento de bicicletas compartilhadas precisa calcular a distância máxima que cada 
bicicleta pode percorrer, com base no nível atual de bateria. 
Cada 1% de bateria permite percorrer 0,5 km. 

Neste desafio, você deve utilizar os conceitos de Programação Orientada a Objetos (POO) para 
modelar a bicicleta. 

Crie uma classe que contenha os atributos necessários e um método para calcular a distância estimada.
'''

### Entrada
# A entrada deve conter:
'''
O nome do modelo da bicicleta (String).
O nível de bateria (int).
'''

### Saída
'''
Deverá retornar uma mensagem com o modelo da bicicleta e a distância máxima estimada, 
formatada com uma casa decimal.

    * Retorno em formato de mensagem.
'''

### EXEMPLOS:
'''
ENTRADA : BikeX 80
SAIDA : BikeX: Distancia estimada = 40.0 km
'''

############################################################################################################

class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        # TODO: Calcule a distância estimada com base no nível de bateria
        distancia = float(self.nivel_bateria) / 2
        return distancia

    def obter_mensagem(self):
        # TODO: Retorne a mensagem formatada com o modelo e a distância
        distancia = self.calcular_distancia()
        msg = f'{self.modelo}: Distancia estimada = {distancia} km'
        return msg

def main():
    modelo = input('Entre com o Modelo da Bike')

    nivel_str = input('Entre com o Nivel da Bateria')
    nivel_bateria = int(nivel_str)

    # TODO: Crie o objeto BicicletaInterna com os dados lidos
    bicicleta = BicicletaInterna(modelo, nivel_bateria)

    print(bicicleta.obter_mensagem())

if __name__ == "__main__":
    main()
