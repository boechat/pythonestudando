####### CONJUNTOS
# Objetivo Geral
# Entender o funcionamento da estrutura de dados set.

#### COMO CRIAR UM CONJUNTOS
# Criando Sets
###
# Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
# pode ser criado com { } 

arr= set([1,2,3,4,1,3,4])
print(arr)  #nao tem os duplicados! volta 1,2,3,4 apenas
arr = set('abacaxi')
print(arr)  #volta c,i,a,x,b
arr = set (('palio','gol','celta','palio'))
print(arr)
arr = {1,2,3,2,4}
print(arr)

print('\n-----------------')

#Acessando
### 
# Precisa converter o set pra lista
arr= set([1,2,3,4,1,3,4])
arr = list(arr)
print(arr[0],'     -Lista Toda -     ',arr)
print('\n-----------------')

# Função enumerate
for indice, ar in enumerate(arr):
    print(f'{indice}::::: {ar}')
print('\n-----------------')

# METODOS DA CLASSE SET
###
# UNION 
conj_a ={1,2,3}
conj_b ={3,4}
conj_c ={1,2}
conj_d = {5}

uniao = conj_a.union(conj_b)
print(uniao)
print('\n-----------------')

# INTERSECTION
inters = conj_a.intersection(conj_b)
print('intersection: ',inters)
print('\n-----------------')

# DIFFERENCE
difff = conj_a.difference(conj_b)
diffb = conj_b.difference(conj_a)
print('DIFFERENCE A com B: ',difff)
print('DIFFERENCE B com A: ',diffb)
print('\n-----------------')

#SYMMETRIC_DIFFERNCE    -  não interseção - todos os elementos que não estão na interseção
symd = conj_a.symmetric_difference(conj_b)
print('symmetric difference: ',symd)
print('\n-----------------')

#ISSUBSET   - Verifica se é um subconjunto do outro
print(conj_b.issubset(conj_a))
print(conj_c.issubset(conj_a))
print('\n-----------------')

#ISSUPERSET   - Verifica se é um super-conjunto do outro
print(conj_a.issuperset(conj_c))
print(conj_a.issuperset(conj_b))
print('\n-----------------')

#ISDISJOINT   - Verifica se não tem elementos pertencentes / se são completamente diferentes sem inteseções
print(conj_a.isdisjoint(conj_c))
print(conj_a.isdisjoint(conj_d))
print('\n-----------------')

#ADD   - Se elemento nao existe, é adicinado
print(conj_a)
conj_a.add(49)
print(conj_a)
print('\n-----------------')

#COPY  - copia elementos do conjunto
conj_e = conj_a.copy()
print(conj_e,'----',conj_a)
print('\n-----------------')

#CLEAR   - Apaga conjunto
print(conj_e)
conj_a.clear()
print(conj_e)
print('\n-----------------')

#DISCARD   - Remove elemento especificado
conj_a = {1,2,3,4,49,4,9,23,32}
print(conj_a)
conj_a.discard(49)
print(conj_a)
print('\n-----------------')

#POP   - Remove primeiro elemento do conjunto
print(conj_a)
conj_a.pop()
print(conj_a)
print('\n-----------------')


#REMOVE   - Remove elemento especificado, SE NAO EXISTIR, dá erro!
conj_f = {1,2,3,4,49,4,9,23,32}
print(conj_f)
conj_f.remove(49)
print(conj_f)
print('\n-----------------')

#LEN   - Tamanho do conjunto
print(conj_a)
print(len(conj_a))
print('\n-----------------')

#IN   - Verifica se um elemento está dentro do conjunto
print(conj_a)
print(1 in conj_a)
print(13000 in conj_a)
print('\n-----------------')
