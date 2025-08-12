# Tratando erros em Python com estruturas de Repetição
# Com base no exercicio proposto na Aula 04 do Desafio DevPro https://youtu.be/FhJlgfqBP28

# Programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Defino a função exercicioum, que vai receber o numero_entrada do usuario e retornar um boolean
def exercicioum(numero_entrada):
    if(numero_entrada < 0 or numero_entrada >10):
        print('Valor Inválido! Tente novamente')
        return False
    else:
        print('Valor válido')
        return True
###################################################################################################
# aqui é o corpo do nosso código, vou inicializar as variaveis locais resultado e contador
resultado = False
contador = 0

# inicio da estrutura de repetição, vejo se a variavel resultado está negativada. Na primeira rodada, sempre vai estar pois setei ela anteriormente para isso
while resultado == False and contador < 10:
    # Pergunto ao user um valor
    perguntanum = input('Digite valor')
    # chamo a funcao exercicioum , armazenando seu valor em resultado. passo como parametro a perguntaum que o usuario inseriu
    resultado = exercicioum(int(perguntanum))
    print(str(resultado))
    # faço a validação, verificando se o resultado agora é False ou True
    if resultado == False:
        # para forma de conferencia, aumento o contador
        contador = contador + 1
        print('Errou! Tente novamente!')
        print('-------------------------')
    else:
        print('---------!SUCESSO!----------------')
        print(f'Finalmente você conseguiu heim! Só me custou {contador} tentativas')
        print('---------!SUCESSO!----------------')
        break

if contador >= 10:
  print('---------!FALHA!----------------')
  print(f'Contador excedeu {contador} tentativas, programa Falhou!')
  print('---------!FALHA!----------------')
  
print('Final de Programa')
print('----------FIM---------------')
