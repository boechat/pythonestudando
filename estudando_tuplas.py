######### TUPLAS
#
# CRIANDO TUPLAS
# Estruturas parecidas com lista, mas IMUTAVEIS.
# Criadas com a classe tuple ou colocando valores separados por vírgula de parenteses

frutas = ('laranja','pera','uva',) # essa virgula no final, sinaliza tupla
print(frutas)
letras = tuple('python')
print(letras)
numeros = tuple([1,2,3,4]) #tupla na lista, nao permitindo mais sua modoficação
print(numeros)
pais = ('Brasil',)
print(pais)

print('\n--------------------------')
# ACESSANDO valores
print(letras[0])
print(letras[-3])
print('\n--------------------------')

# TUPLAS ANINHADAS
# Tupla dentro de tupla, formando tabelas com linhas e colunas
matriz = (
    (1,'a',2),
    ('b',3,4),
    (6,7,'c'),
    )

print(matriz)
print(matriz[2][1])
print('\n--------------------------')
