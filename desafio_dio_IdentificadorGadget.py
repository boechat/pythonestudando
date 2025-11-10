#####################################    DESAFIO DE CODIGO   ##########################################

###############################  ENTENDO FUNCOES EM SOLUCOES DIGITAIS #################################
'''
No laboratório de inovação TechDreams, engenheiros trabalham dia e noite criando gadgets incríveis para facilitar o dia a dia das pessoas.
No entanto, as equipes têm enfrentado um pequeno problema: identificar rapidamente a categoria de cada gadget recém-desenvolvido a partir de seu código.
Para otimizar esse processo e incentivar boas práticas de programação, a líder de projetos, Zoe, propôs um desafio aos novos desenvolvedores.
Eles devem criar uma função clara e bem definida que, ao receber como entrada um código de gadget, devolve a categoria correta.
Isso garantirá um código fácil de entender, manter e reutilizar no futuro.

Sua missão é implementar uma função que receba uma string representando o código de um gadget e retorne a categoria correspondente.
Considere estas categorias: códigos que comecem com “T” são “tablet”, com “P” são “phone” e com “N” são “notebook”.
Caso não pertença a nenhuma dessas categorias, retorne “unknown”.
O objetivo é mostrar como funções facilitam o código limpo e reutilizável, elementos essenciais em ambientes de inovação constante.

Respeite os formatos de entrada e saída indicados abaixo e não use bibliotecas externas.
'''
########################################################################################################
'''
ENTRADA

Uma única string com o código do gadget (sem espaços). O código pode conter letras e/ou números.

SAÍDA    

Uma única palavra indicando a categoria do gadget: “tablet”, “phone”, “notebook” ou “unknown”.
'''
##########################################################################################################

'''
EXEMPLOS

Entrada	                      | Saída
------------------------------|---------------------
T12345X	                      |tablet
P45YTS	                      |phone
R2123Z	                      |unknown     

'''

def identificar_categoria_gadget(codigo):
    """
    Recebe uma string 'codigo' e retorna a categoria associada:
    - 'T': tablet
    - 'P': phone
    - 'N': notebook
    Se não corresponder, retorna 'unknown'.
    """
    # TODO: Implemente a lógica para identificar a categoria do gadget
    primeira_letra = codigo[0]
    #print(primeira_letra)
    if primeira_letra == 'T':
        retorno = 'tablet'
        return retorno
    elif primeira_letra == 'P':
        retorno = 'phone'
        return retorno
    elif primeira_letra == 'N':
        retorno = 'notebook'
        return retorno
    else:
        retorno = 'unknown'
        return retorno

    # Dica: Verifique a primeira letra do código para determinar a categoria
    # Tipo esperado: 'codigo' é uma string não vazia

    pass  # Remova este pass ao implementar a solução

# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'
