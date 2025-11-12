#####################################    DESAFIO DE CODIGO   ##########################################

###############################  Fundamentos de POO em Soluções Digitais #################################
'''
A startup InovaTec lançou seu primeiro protótipo de robô assistente pessoal, chamado RoboMensagem.
Este robô é capaz de ajudar engenheiros a organizar suas comunicações diárias de forma eficiente.
Para testar suas habilidades de Programação Orientada a Objetos, a equipe de desenvolvimento decidiu implementar um sistema
onde cada mensagem enviada ao robô é processada por um objeto da classe Mensagem.
Cada Mensagem possui um remetente e um conteúdo, e o RoboMensagem deve ser capaz de identificar quem enviou a mensagem e
 qual é o conteúdo transmitido, imprimindo ambas as informações no formato correto.

Sua tarefa é implementar a classe Mensagem com dois atributos (remetente e conteudo) e um método chamado exibir, que retorna as informações formatadas como ": ".

Todas as operações devem ser encapsuladas na classe e não é permitido utilizar bibliotecas externas além da biblioteca padrão de sua linguagem
'''
########################################################################################################
'''
ENTRADA

A primeira linha contém o nome do remetente. A segunda linha contém o conteúdo da mensagem, ambos sem acentos ou caracteres especiais.
O comprimento de cada linha está limitado ao máximo de 69 caracteres ASCII.

SAÍDA    

Imprima uma única linha no formato ": ", respeitando exatamente este padrão.
A saída não deve conter espaços extras, aspas ou acentos e deve exibir apenas a mensagem processada pelo objeto criado.

EXEMPLOS:
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	            |       Saída
-------------------------------------------
Maria               |
Bom dia equipe	    |Maria: Bom dia equipe
-------------------------------------------
Joao                |
Reuniao adiada para |
amanha	            |Joao: Reuniao adiada para amanha
-------------------------------------------
Luiz23              |
Teste do sistema    |
completo	        |Luiz23: Teste do sistema completo
-------------------------------------------

'''
##########################################################################################################

class Mensagem:
    def __init__(self, remetente, conteudo):
        # Inicializa os atributos da mensagem
        self.remetente = remetente
        self.conteudo = conteudo

    def exibir(self):
        # Retorna a mensagem formatada conforme o padrão requisitado
        # TODO: Formate a mensagem de acordo com o padrão de saída
        frase_nova = self.remetente +': ' + self.conteudo
        # Dica: utilize f-strings para concatenar remetente e conteúdo
        return frase_nova  # Remova este pass após implementar


# Lê o nome do remetente (primeira linha da entrada)
remetente = input()
# Lê o conteúdo da mensagem (segunda linha da entrada)
conteudo = input()

# Cria o objeto Mensagem com os dados recebidos
mensagem = Mensagem(remetente, conteudo)

# Imprime a mensagem formatada pela função exibir (saída conforme especificação)
print(mensagem.exibir())
