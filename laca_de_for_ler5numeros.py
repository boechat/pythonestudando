# Dois exercicios com FOR, baseado no treinamento Desafio DevPro , Aula 05 - https://youtu.be/5mHsj_cosQs

# EXERCICO SETE: Faça um Programa que leia 5 numeros e informe o maior numero

def exerciciosete():
  maximo = float(input('Digite um número: '))
  #Usamos o _ para mostrar que nao queremos usar os indices gerados no for
  for _ in range(5):
    #print(i+1)
    #max vai pegar o maximo
    maximo = max(maximo,float(input('Digite um Outro número: ')))
    print(f'Numero maximo encontrado foi: {int(maximo)}')
    print('---------')

# Para executar:
#exerciciosete()

# EXERCICO OITO: Faça um Programa que leia 5 numeros e informe a soma e a média

def exerciciooito():
    soma_ins = 0
  #Usamos o _ para mostrar que nao queremos usar os indices gerados no for
    for _ in range(5):
        numero_inserido = float(input('Digite um número: '))
    #print(i+1)
    #max vai pegar o maximo
        soma_ins = numero_inserido + soma_ins
    else:
        print('Final do laço')
        return soma_ins

# Para executar:
soma = exerciciooito()
print('-----')
print(f'SOMA: {int(soma)}')
print('-----')
print(f'MEDIA: {float(soma/5)}')
