# FUNCOES 
# Bloco código indentificado por um nome que pode receber uma lista de parametros que podem ou nao ter alores padroes.
# Facilita leitura do código, deixa a programação ESTRUTURADA

def exibir_mensagem():
    print('Ola!')

def exibir_mensagem_2(nome):
    print(f'Ola, {nome}!')

def exibir_mensagem_3(nome='Antonio'):
    print(f'Ola, {nome}!')

# Print Normal    
exibir_mensagem()
# Parametro passado
exibir_mensagem_2(nome='Alucard')
# Sem passar parametro, puxa o padrão
exibir_mensagem_3()
# Parametro passado
exibir_mensagem_3(nome='Dracula')


##############
## Retornando valores

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor , sucessor 

print('-----------')
print('Calcular Total = ',calcular_total([10,20,34]))
print('Antecessor e Sucessor: ',retorna_antecessor_e_sucessor(10))
retorno = retorna_antecessor_e_sucessor(10)
for i in retorno:
    print('Valor da Tupla : ',i)
    
#### Argumentos Nomeados
## Funções tambem podem ser chamadas usando argumentos nomeados da forma chave=valor
print('-----------')
def salvar_carro(marca,modelo,ano,placa):
    # salva carro no banco de dados
    print(f'carro inserido com sucesso! :{marca}/{modelo}/{ano}/{placa}')

#salvar_carro('Fiat'.'Palio',1999,'ABC-1234')
## Desvantagem: Precisa estar ordenado!

#salvar_carro(marca='Fiat',modelo='Palio',ano=1999,placa='ABC-1234')
## Desvantagem: Se o nome do argumento for modificado, vai dar erro de argumento

salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':1999,'placa':'ABC-1234'})
#Passando um dicionario; usando dois ** pra falar 'estou passando um dicionario pra essa função'

print('-----------')

######################### Args e kwargs
# Podemos combinar parametros obrigatorios com args e kwargs.
# Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla(*args) e dicionario(**kwargs)

#### No caso baixo, usamos KWARGS! passando dicionario!
#salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':1999,'placa':'ABC-1234'})

# Exemplo:


def exibir_poema(data_extenso, *args, **kwargs):
    # vai ser passado a data que o poema foi criado, a lista de versos e as informações pro poema (AUtor, Distribuidora etc)
    texto = '\n'.join(args)
    #pega todos os valores que vieram em *args e concatena com '\n'
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    # recebe o kwargs, coloca o .items para acessar o dicionario. O .items vai entregar uma lista de tuplas com chave e valor que vamos iterar na lista.
    # crio uma string com a chave e valor; colocando um meta_dados por linha
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    #no final, criando uma variavel mensagem colocando a data_extenso, o texto e metadados
    print(mensagem)

exibir_poema('Quinta-Feira - 14 de Agosto de 2025','Zen of Python', 'Beautiful is better than ugly.', autor = 'Tim Peters', ano=1999)
# Na Primeira linha, vai passar como data_extenso; os demais argumentos não declarados em chaves-valor se tornam uma tupla; autor e ano são declarados, então viram kwargs
print('-------------------')
exibir_poema('Data Extenso','poema','poema','poema','poema','poema','poema','poema', autor = 'nome qualquer', ano=9999)


print('-------------------PARTE 02 -------------------------')
#####################PARAMETROS ESPECIAIS
# def f(pos1, pos2, / , pos_or_kwd, * ,kwd1, kwd2):
        #|esses são só por posição (pos1,pos2)
        #|após a /, pode ser posição ou keyword
        #|após o *, só aceita keyword 

########SOMENTE POSIÇÃO:
print('\n---SOMENTE POSIÇÃO---')
def carro_pos(modelo,ano,placa,/,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

### Funcao valida pois respeita os parametros
carro_pos('Palio',1999,'ABC-1234', marca='FIAT',motor='1.0',combustivel='Gasolina')    
### Funcao valida pois respeita os parametros
carro_pos('Palio',1999,'ABC-1234', 'FIAT','1.0','Gasolina')    
### Funcao Invalida Porque passa keyword onde só aceita posição
#carro_pos(modelo ='Palio',ano = 1999,placa='ABC-1234', marca='FIAT',motor='1.0',combustivel='Gasolina')  

print('\n---SOMENTE KEY---')
########SOMENTE KEYWORD:

def carro_key(*,modelo,ano,placa,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

##Funcao valida pois passa chave e valor
carro_key(modelo ='Palio',ano = 1999,placa='ABC-1234', marca='FIAT',motor='1.0',combustivel='Gasolina')  
##Funcao invalida pois passa posicao tbm
#carro_key('Palio',ano = 1999,placa='ABC-1234', marca='FIAT',motor='1.0',combustivel='Gasolina')  


############ OBJETOS DE PRIMEIRA CLASSE ################ 
## Objeto que pode ser passado por parametro para funcoes, usada como valores em estrutura de dados e como valor de retorno
print('\n---OBJETOS DE PRIMEIRA CLASSE---')

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b
    
def exibir_resultado(a,b,funcao_aleatoria):
    resultado = funcao_aleatoria(a,b)
    print(f'Essa funcao chamou uma Outra Função e fez o calculo de dois numeros: {a} e {b} ,trazendo dela o resultado: {resultado}')

op = somar
print('Mostrando que dá pra atribuir variavel e execura com somar, passando 1 e 23 como parametros e tendo como resultado: ',op(1,23))
exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)

############ ESCOPO LOCAL E ESCOPO GLOBAL ################ 
print('\n---ESCOPO LOCAL E ESCOPO GLOBAL---')

salario = 1000  
# Salario está fora da funcao, na raiz. Vamos chamar de global entao

def salario_bonus(bonus, lista):
    global salario
    print(lista)
    lista.append(2)
    #avisando que salario está na raiz
    salario += bonus
    return salario

lista = [1]
print(salario_bonus(500, lista))
print(salario)
print(lista)
# Perceba que a lista foi alterada dentro da função; para que nao se perca nada, convem-se criar uma lista auxiliar, fazendo uso do comando lista.copy()

def salario_bonus(bonus, lista):
    global salario
    #faz copia da lista
    lista_aux = lista.copy()
    # trabalha com a lista auxiliar ao inves da lista comum
    lista_aux.append(2)
    print('\n-------------\nLista =',lista,'\n-------------\nLista Aux =',lista_aux,'\n-----------')
    salario += bonus
    
    return salario

lista = [1]
print(salario_bonus(500, lista))
print(salario)
print('Lista =',lista)
