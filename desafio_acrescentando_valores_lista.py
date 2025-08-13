# Exercicio Desafio DevPro - AULA 06 - acrescentar valores em lista
# https://youtu.be/76jVKDXeVNI
# EX-15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a '-1' que não deve ser armazenado. 
# Apos essa entrada de dados faça:
# a) mostre a quantidade de valores que foram lidos
# b) exiba todos os valores na ordem em que foram informados, um ao lado do outro
# c) Exiba todos os valores na ordem inversa a que foram informados, um abaixo do outro
# d) Calcule e mostre a soma dos valores;
# e) Calcule e mostre a média dos valores.
# f) Calucle e mostre a qtd de valores acima da média calculada;
# g) Calcule e mostre a quantidade de valores abaixo de sete;
# h) Encerre o programa com uma mensagem;


# INICIO DO CODIGO #

#=======FUNCOES=======================================

#-----Funcao Cria Lista -----------------------------#
def cria_lista(valor_usuario,lista_criada):
    if valor_usuario == -1:
        print('-Valor Proibido, encerrando-')
    else:
        lista_criada.append(valor_usuario)
        print(f'lista criada ficou: {lista_criada}')
        return(lista_criada)
        
#-----A)   Funcao Pega Tamanho -----------------------------#
def pega_tamanho(lista_tam):
    valor_qtd = len(lista_tam)
    return(valor_qtd)

#-----B)  Funcao Horizontaliza Elementos -----------------------------#
def horizontaliza_lista(lista_hor):
    line = ''
    for i in range(len(lista_hor)):
        line += str(lista_hor[i])
        if i < len(lista_hor) - 1:
            line += ', '
    return line
#-----C)  Funcao Verticaliza Elementos -----------------------------#
def verticaliza_lista(lista_ver):
    for i in range(len(lista_ver)):
        print(lista_ver[i])
#-----D)  Funcao Inverte Verticaliza Elementos -----------------------------#
def inverso_verticaliza_lista(lista_inver):
    for item in reversed(lista_inver):
        print(item)
#-----E)  Funcao Calcula Soma -----------------------------#
def soma_lista(lista_s):
    total = sum(lista_s)
    return(total)
#-----F)  Funcao Calcula Media -----------------------------#
def media_lista(valores,tam):
    media = valores/tam
    return(media)
#-----G)  Funcao Calcula Quantidade Acima da Média Calculada -----------------------------#
def verifica_media(lista_ver,med):
    lista_acima_da_media = []
    for i in range(len(lista_ver)):
        if lista_ver[i] > med:
            lista_acima_da_media.append(lista_ver[i])
    return(lista_acima_da_media)

#-----H)  Funcao Calcula Quantidade Abaixo de Sete -----------------------------#
def verifica_sete(lista_sete):
    lista_abaixo = []
    for i in range(len(lista_sete)):
        if lista_sete[i] < 7:
            lista_abaixo.append(lista_sete[i])
    return(lista_abaixo)

#=======MAIN=======================================
def main():
    # Inicio da Main 
    # Variaveis
    iteracao = 0
    lista_criada = []
    #
    print('----------------------INICIO-----------------------------')
    
    while True:
        try:
            #Insere valor na lista 
            valor = float(input('Entre com um valor para a lista!\nCaso queira encerrar a lista prematuramente, digite -1'))
            if int(valor) == -1:
                ('Valor de entrada foi -1, ENCERRANDO ITERACAO')
                break
            elif isinstance(valor, (int, float)) and int(valor) != -1:
                lista_resultado = cria_lista(valor,lista_criada)
                print(lista_resultado)
            else:
                ('Caracter Não permitido! Precisa ser Int ou Float')
            
            condicao_saida = input("Digite [s] para sair ou [n] para continuar no loop ")
        
            # Garante que é string e converte para minúsculas
            if not isinstance(condicao_saida, str):
                raise TypeError("A entrada não é uma string.")

            condicao_saida = condicao_saida.lower()

            if condicao_saida == 's':
                print('Sair do Loop')
                print('-------------#----------#--------------')
                print('---------Lista Resultado ------------')
                print(f'LISTA RESULTADO = : {lista_resultado}')
                
                print('---------TAMANHO DA LISTA ------------')
                tamanho = pega_tamanho(lista_resultado)
                print(f'* A ) Quantidade de Valores que Foram Lidos = : {tamanho}')
                
                print('---------VALORES HORIZONTAL ------------')
                horizontal_valores = horizontaliza_lista(lista_resultado)
                print(f'* B ) Todos os Valores Na Ordem Que Foram Informados, na Horizontal = : {horizontal_valores}')
               
                print('---------VALORES VERTICAL ------------')
                print('* C ) Todos os Valores Na Ordem Que Foram Informados, na Vertical ='),verticaliza_lista(lista_resultado)
               
                print('---------VALORES VERTICAL INVERTIDO ------------')
                print(f'* D ) Todos os Valores Na Ordem INVERSA Que Foram Informados, na Vertical  ='),inverso_verticaliza_lista(lista_resultado)
                
                print('---------SOMA DOS VALORES DA LISTA ------------')
                soma_total = soma_lista(lista_resultado)
                print(f'* E ) Resultado Da SOMA Dos valores da Lista  = {soma_total}')
                
                print('---------MÉDIA DOS VALORES ------------')
                media = media_lista(soma_total,tamanho)
                print(f'* F ) Média dos Valores da Lista  = {media}')
                
                print('---------VERIFICA QUANTIDADE DE VALORES ACIMA DA MÉDIA ------------')
                #lista_media =[]
                lista_media = verifica_media(lista_resultado,media)
                print('G) Lista dos Valores Acima da média :',lista_media)
                print(f'G) Quantidade de Valores acima da Média: ====  {len(lista_media)}  =====')

                print('---------VERIFICA QUANTIDADE DE VALORES ABAIXO DE SETE ------------')
                #lista_media =[]
                lista_sete = verifica_sete(lista_resultado)
                print('H) Lista dos Valores Abaixo de Sete :',lista_sete)
                print(f'H) Quantidade de Valores acima de Sete: ====  {len(lista_sete)}  =====')
                
                print('-------------------------------------')
                
                break
            
            
            
            elif condicao_saida =='n':
                iteracao +=1 
                print('Próxima Iteracao')
            else:
                print('Caracter inválido')

        except TypeError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

#=====================================================
    
