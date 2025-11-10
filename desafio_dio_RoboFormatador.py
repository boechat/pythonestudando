#####################################    DESAFIO DE CODIGO   ##########################################

###############################  ENTENDO FUNCOES EM SOLUCOES DIGITAIS #################################
'''
Na futurística cidade de Tecnos, a equipe do Laboratório de Inovação está desenvolvendo um robô que processa comandos de texto enviados por usuários.
Para garantir clareza nos logs e troca de dados, o robô deve ser capaz de padronizar e aprimorar mensagens usando funções bem definidas, seguindo boas práticas de programação.
Seu desafio é ajudar a equipe do laboratório a criar uma função que recebe uma mensagem enviada ao robô e retorna a mesma mensagem:
    (1) sem espaços extras no início ou fim,
    (2) com todas as letras minúsculas, e
    (3) com apenas um único espaço separando as palavras.

Implemente esta função seguindo boas práticas (clareza, reutilização e modularização) e sem utilizar bibliotecas externas. Certifique-se de que a função trate corretamente mensagens já padronizadas ou compostas apenas de espaços.
'''
########################################################################################################
'''
ENTRADA

Uma única linha contendo uma mensagem (string) enviada ao robô. A mensagem pode conter letras maiúsculas ou minúsculas, espaços múltiplos entre palavras ou ao redor, 
e pode estar vazia ou conter apenas espaços.

SAÍDA    

Uma única linha contendo a mensagem processada: sem espaços extras no início/fim, todas as letras em minúsculo, e com apenas um espaço separando cada palavra. 
Se a entrada for vazia ou composta apenas por espaços, a saída deve ser uma linha vazia.
'''
##########################################################################################################

'''
EXEMPLOS

Entrada	                      | Saída
------------------------------|---------------------
Bem  Vindo Ao  LAB            |bem vindo ao lab
INOVAR     sempre             |inovar sempre
Essa   Eh Uma  LINHA     Teste|essa eh uma linha teste

'''

def formatar_mensagem(texto):
    
    texto = texto.strip()
    if not texto:
        return ""

    palavras = texto.lower().split()
    texto = " ".join(palavras)

    return texto


entrada = input('')  
saida = formatar_mensagem(entrada)
print(saida)
