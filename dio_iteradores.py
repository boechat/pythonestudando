### CONTEUDO BASEADO NA AULA ITERADORES DA DIO 
### https://web.dio.me/track/luizalabs-back-end-com-python/course/decoradores-iteradores-e-geradores-com-python/learning/
## referencia: https://github.com/digitalinnovationone/trilha-python-dio

'''
Um iterador é um objeto que contém um número CONTAVEL de valores que podem ser ITERADOS,
o que significa que você pode percorrer todos os valores.

O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais:
__iter__() e __next__()
'''

### FUNCOES DE ITERADORES: 
'''
Usamos para:
* Economizar memória, evitando carregar todas as linhas do arquivo.
* Iterar linha a linha do arquivo
'''

### Exemplo ####
'''
print(' ---- Exemplo Iterador ------ \n')

class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration                 #Finaliza o Laço com StopIteration
    
# Uso do FileIterator
for line in FileIterator('large_file.txt')
    print(line)
'''

print('1 ---- Exemplo Iterador ------ \n')

from typing import List

class MeuIterador:
    def __init__(self, numeros: List[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero *2
            
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros = [1,2,3]):
    print(i)
