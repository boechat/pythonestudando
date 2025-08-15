######################################################## LISTAS : CRIACAO E ACESSO AOS DADOS
# podemos criar listas utilizando o construtor list, a função range ou colocando os valores separados por virgula dentro de colchetes.
# listas são OBJETOS MUTAVEIS portanto podemos alterar seus valores após a criação.

frutas = ['laranja','maca']
print(frutas)
frutas = []
print(frutas)
letras = list('python')
print(letras)
numeros = list(range(10))
print(numeros)
carro = ['Ferrari', 'F8', 42222222, 2020, 29000, 'São Paulo', True]
print(carro)

print('--------------------------')
######################################################## ACESSO DIRETO
# Podemos acessar com o indice
# Ex: list[1] acessa a segunda posição

print(carro[2])
######################################################## INDICE NEGATIVOS
# Sequencias suportam indexação negativa. A contagem começa em -1 
print(carro[-1])

######################################################## LISTAS ANINHADAS
# Listas podem armazenar todos os tipos de objetos Python, inclusive Listas; podendo assim ser criado tabelas (lista dentro de listas)

matriz = [
    [1,'a',2],
    ['b',3,5],
    [6,9,'c']
    ]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print('--------------------------')

######################################################## FATIAMENTO
# Alem de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. 
# Para isso basta passar o índice inicial e/ou final para acessar o conjunto.
# Podemos ainda informar quantas posições o cursor deve 'pular' no acesso.

lista = ['p','y','t','h','o','n']
print(lista[2:])  # começa da terceira posição ate o final
print(lista[:2])  # vai do 0 até a terceira posição (final)
print(lista[1:3]) #  vai da segunda posição até a quarta
print(lista[0:3:2]) # inicil, final e step; começa do 0, vai até a 4 posição, pulando de 2 em 2
print(lista[::]) # tudo vazio; pega a lista toda 
print(lista[::-1]) #inverte a lista

print('--------------------------')

######################################################## ITERAR LISTAS
# A forma mais comum para percorrer os dados de uma lista é utilizando o comando for
carros = ['gol','celta','palio']

print(carros)
for carro in carros:
    print(carro)

print('--------------------------')

######################################################## FUNCAO ENUMERATE 
# Para saber o indice
print(carros)
for indice,carro in enumerate(carros):
    print(f'{indice}: {carro}')

print('--------------------------')

######################################################## COMPREENSAO DE LISTAS 
# Sintaxe mais curta;

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#VERSAO 2
impares = [numero for numero in numeros if numero % 2 == 1]
#                 [Essa parte é a iteracao                ]
#         [Essa é o Retorno]
print(impares)

# Modificando Valores na Versão 1 
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)
print(quadrados)

# Modificando Valores na Versão 2
quadrodo_do_quadrado = [quadrado ** 2 for quadrado in quadrados]
print(quadrodo_do_quadrado)

######################################################## Métodos da Classe List
print('---------Métodos da Classe List-----------------')

# APPEND -> adiciona ao fim
listateste = []
listateste.append(2)
listateste.append([32,32,32])
print(listateste)
print('\n--------------------------')

# CLEAR -> apaga a lista
listavazia = listateste
print(listavazia)
listavazia.clear()
print(listavazia)
print('\n--------------------------')

# COPY -> copia lista, em uma instancia diferente
lista = ['1',1,[23,32,43]]
l2 = lista.copy()
print(lista,id(lista),'\n',l2,id(l2))  #Pra ver que são objetos diferentes usando id
print('\n--------------------------')

# COUNT -> conta elementos
print(l2.count(1))
print('\n--------------------------')

# EXTEND -> junta uma lista ao final
l2.extend(lista)
print(l2)
print('\n--------------------------')

# INDEX -> retorna o index do PRIMEIRO elemento na lista
print(l2.index('1'))
print('\n--------------------------')

# POP -> remove um item da lista, se nao passar nada, remove o ultimo item
print(l2)
l2.pop() # removeu o ultimo
print(l2)
l2.pop(0) # removeu no indice 0
print(l2)
print('\n--------------------------')

# REMOVE -> remove UM item da lista, passando o OBJETO em si
print(l2)
l2.remove(1) # removeu o item de elemento 1
print(l2)

print('\n--------------------------')

# REVERSE -> Pega a Lista e inverte os elementos
print(l2)
l2.reverse()
print(l2)
print('\n--------------------------')

# SORT -> Ordena lista
l3 = [1,3,5,7,9,20,12,15]
print(l3)
l3.sort()  #ordena do menor ao maior
print(l3)
l3.sort(reverse=True)  #ordena do maior ao menor 
print(l3)
# Ordena por tamanho da palavra / string
l4 = ['carro','ano','dromedario','dragao','sexto']
l4.sort(key= lambda x: len(x))  #ordena do menor ao maior; passa uma função anonima lambda que pra cada item executa x, querendo saber o len(tamanho) de x
print(l4)
l4.sort(key= lambda x: len(x), reverse=True)  #ordena do maior ao menor
print(l4)
print('\n--------------------------')

# LEN -> Pega o tamanho da Lista
print(len(l2))
print('\n--------------------------')

# SORTED -> Ordena iteraveis, mas a diferença é que é uma função
l5 = ['carro','ano','dromedario','dragao','sexto']
print(sorted(l5, key=lambda x: len(x)))
print(sorted(l5, key=lambda x: len(x), reverse= True))
#mais simples
print(sorted(l5))
print('\n--------------------------')
