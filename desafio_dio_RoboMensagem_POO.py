#####################################    DESAFIO DE CODIGO   ##########################################

###############################  Fundamentos de POO em Soluções Digitais #################################
'''
Na cidade futurista de Inovapolis, engenheiros trabalham em uma startup dedicada à criação de robôs inteligentes para ajudar pequenas tarefas diárias.
Como parte da competição anual de tecnologia, sua equipe precisa construir um sistema que dê nomes exclusivos para cada novo protótipo fabricado, unindo duas palavras de identificação.
Para garantir flexibilidade e organização, a equipe decidiu usar conceitos de Programação Orientada a Objetos para representar cada robô.
Sua missão é implementar o núcleo desse sistema: uma classe responsável por armazenar os dois identificadores de cada robô e gerar corretamente o nome composto.

Sua solução deve criar uma classe que receba dois nomes (modelos) na inicialização e disponibilize um método para exibir o nome completo do robô no formato correto.
O objetivo é demonstrar domínio básico de POO criando e utilizando objetos, métodos e construtores.
As palavras informadas não terão espaços nem acentuação e devem ser unidas por um hífen.
'''
########################################################################################################
'''
ENTRADA

Uma linha contendo duas strings separadas por espaço, representando os modelos do robô (apenas caracteres ASCII sem acentuação, mínimo 1 e máximo 30 cada).

SAÍDA    

Uma única linha contendo o nome completo do robô, no formato modelo1-modelo2 (sem espaços adicionais e sem acentuação), tudo em uma string.

EXEMPLOS:
A tabela abaixo apresenta exemplos de entrada e saída:

----------------------------------------------
Entrada             |	Saída
----------------------------------------------
nano chip	        |   nano-chip
eco bot	            |   eco-bot
laser rover	        |   laser-rover
----------------------------------------------

'''
##########################################################################################################

# RoboNomeador 3000 - Núcleo em Python (POO)

class Robo:
    def __init__(self, modelo1: str, modelo2: str):
        self.modelo1 = modelo1
        self.modelo2 = modelo2

    def nome_completo(self) -> str:
        return f"{self.modelo1}-{self.modelo2}"

# Lê a entrada padrão e separa em dois modelos usando espaço como separador
entrada = input().strip()
modelos = entrada.split()

if len(modelos) != 2:
    print("Entrada invalida: devem ser dois modelos separados por espaço.")
else:
    modelo1, modelo2 = modelos

    # TODO: Crie um objeto da classe Robo com os modelos e imprima o nome completo
    # Dica: utilize o método nome_completo para compor o nome

    robo = Robo(modelo1, modelo2)
    print(robo.nome_completo())
