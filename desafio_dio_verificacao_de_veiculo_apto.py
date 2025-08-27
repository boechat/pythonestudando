#####################################    DESAFIO DE CODIGO   ##########################################

###############################  MONITORAMENTO E VERIFICACAO COM POO ##################################

### Descrição
'''
Um aplicativo de monitoramento de carros precisa verificar se um carro está apto para rodar com base no ano de fabricação e no ano atual.
Um carro é considerado apto se tiver até 10 anos de uso.
Para resolver este desafio, você deve utilizar conceitos de Programação Orientada a Objetos (POO),
como a definição de métodos estáticos, para realizar a verificação da aptidão do carro sem a necessidade de instanciar objetos.
A aplicação de POO deve ser utilizada para organizar a lógica de verificação do carro e para retornar o resultado da aptidão de forma estruturada.
'''

### Entrada
# A entrada deve conter:
'''
    *   O modelo do carro (String).
    *   O ano de fabricação (int).
    *   O ano atual (int).
'''

### Saída
'''
Deverá retornar uma mensagem indicando se o carro está apto ou não.

Retorno em formato de mensagem.
'''

### EXEMPLOS:
'''
ENTRADA : Civic 
2015
2025
SAIDA :  Civic: Apto
'''

############################################################################################################
def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):
    idade_carro = ano_atual - ano_fabricacao
    if idade_carro > 10:
        msg = f'{modelo}: Nao apto'
    else:
        msg = f'{modelo}: Apto'
    return msg
    # TODO: Verifique se o carro está apto com base na idade


def main():
    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    # TODO: Chame a função para verificar a aptidão do carro

    resultado = verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual)

    print(resultado)


if __name__ == "__main__":
    main()
