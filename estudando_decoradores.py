### CONTEUDO BASEADO NA AULA DECORADORES DA DIO 
### https://web.dio.me/track/luizalabs-back-end-com-python/course/decoradores-iteradores-e-geradores-com-python/learning
## referencia: https://github.com/digitalinnovationone/trilha-python-dio

def dizer_oi(nome):
    return f'Oi {nome}'

def incentivo_aprende(nome):
    return f'Oi {nome}, vamos aprender Python!'
    
def mensagem_aleatoria(funcao_mensagem):
    return funcao_mensagem('Você ')

print(mensagem_aleatoria(incentivo_aprende))
print(mensagem_aleatoria(dizer_oi))

## INNER FUNCTIONS
# É possiuvel definir funções dentro de outras funções. Tais Funções são chamadas de funções internas

print('---------------- inner function ---------')

def pai():
    print('escrevendo func pai()')
    
    def filho1():
        print('escreveindo func filho1()')
    
    def filho2():
        print('escrevendo func filho2()')
        
    filho2()
    filho1()

pai()

### RETORNANDO FUNCOES DE FUNCOES 
# Python tambem permite que você usa funções como valores de retorno
print('------ retornando funcoes de funcoes -------------')
def calcular(operacao):
    def somar(a,b):
        return a + b
    def subrtrair(a,b):
        return a-b
    
    if operacao == '+':
        return somar
    else:
        return subtrair

resultado = calcular('+')(1,3)
print(resultado)

### Exemplos ####
print('---------Exemplo 1----------------')
print('\n#### PASSAGEM PARAMETRO ########')

def mensagem(nome):
    print('Executando nome')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Execuntado mensagem longa')
    return f'Olá tudo bem com você {nome}?'

def executar(funcao, nome):
    print('executar')
    return funcao(nome)

print(executar(mensagem, 'Teste'))
print(executar(mensagem_longa, 'Teste'))

print('---------Exemplo 2----------------')
print('\n####  FUNCAO INTERNA ########')

def prin():
    print('Executando Principal')
    
    def fun_int():
        print('executando a funcao interna')
    
    def fun_2():
        print('executando a funcao 2')
    
    fun_int()
    fun_2()
    
prin()

print('---------Exemplo 3----------------')
print('\n####  RETORNA FUNCAO ########')

def calculadora(op):
    def soma(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
'''   
    match op:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return mul
        case '/':
            return div
print(calculadora('+')(2,2))
print(calculadora('/')(2,2))
op = calculadora('*')(2,2)
print(op)
'''

################# DECORADOR SIMPLES ###################
## Agora que entedemos que funcoes sao como qualquer outro objeto em Python,
## Podemos seguir em frente e ver a mágica que é o decorador Python

## Decorador são funções.
## Pode ser usado para checagens de segurança
## Personalização de codigo

print('\n-------DECORADORES -------')
print('\n-------1º Decorador -------')

def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a funcao')
        funcao()
        print('Faz algo depois de executar a funcao')
    
    return envelope

def ola_mundo():
    print('Ola Mundo')

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

### AÇÚCAR SINTÀTICO####
# O python permite que você use de coradores de forma mais simples, usando o síbmolo @

print('\n-------Açúcar Sintático -------')


def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a funcao')
        funcao()
        print('Faz algo depois de executar a funcao')
    
    return envelope

@meu_decorador
def ola_mundo():
    print('Ola Mundo')

ola_mundo()

### Funções de decoração com Argumentos
# Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave

################# DECORADOR COM ARGUMENTOS ###################

print('\n-------2º Decorador -------')


def duplicar(func):
    def envelope(*args, **kwargs):
       #chama a função duas vezes
       func(*args, **kwargs)
       func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo{tecnologia}')



print('\n-------3º Decorador - Com argumentos -------')

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar a funcao')
        funcao(*args, **kwargs)
        print('Faz algo depois de executar a funcao')
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print('Ola Mundo ',nome)

################# RETORNANDO VALORES DE FUNÇÕES DECORADAS ###################
# O decorador pode decidir se retorna o valor da função decorada ou não.
# Para que o valor seja retornado, a função de ENVELOPE deve retornar o valor da função decorada

print('\n-------4º Decorador - Com argumentos e RETORNANDO-------')

def duplicar(func):
    def envelope(*args, **kwargs):
       #chama a função novamente
       func(*args, **kwargs)
       return func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()
    #Retorna em Maiusculo
    
tecnologia = aprender('python')
print(tecnologia)

################# INTROSPECÇÂO ###################
# Capacidade de um objeto saber sobre seus proprios atributos em tempo de execucao

print('\n-------Introspeccao, usando functools-------')

import functools 

def duplicar(func):
    # Usando functools, você mantem o nome da função e os parametros para você não perder a capacidade de introspecção!
    @functools.wraps(func)
    def envelope(*args, **kwargs):
       #chama a função novamente
       func(*args, **kwargs)
       return func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()
    #Retorna em Maiusculo
    
tecnologia = aprender('python')
print(tecnologia)

