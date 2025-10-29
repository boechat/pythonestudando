### MANIPULAÇÃO DE ARQUIVOS ###

'''
Arquivo é um container no computador onde as informações são armazenadas em formato digital.
Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binários.


'''

### ABRINDO E FECHANDO ARQUIVOS ###

'''
Para manipular arquivos em Python:  open()
Para fechar :   close() 
Fechar libera recursos do pc.

""""
file = open('exemplo.txt','r')
file.close()
""""

'''
### MODOS DE ABERTURAR DE ARQUIVO ###
'''
'r' -> apenas leitura
file = open('exemplo.txt','r')

'w' -> gravação 
file = open('exemplo.txt','w')

'a' -> anexar
file = open('exemplo.txt','a')

'''

### LENDO UM ARQUIVO ###
'''
read()
readline()    --> lê uma linha por vez 
readlines()    ---> retorna uma lista onde cada elemento é uma linha do arquivo

""""
file = open('example.txt','r')
print(file.read())          ----> Pega todo o conteudo do arquivo, coloca numa string
file.close()

for linha in arquivo.readlines():
    print(linha)
    
while len(linha := arquivo.readline()):
    print(linha)
    
### OBS-> o operador ':='   --> Atribui e retorna o valor ao mesmo tempo.

""""
'''

### ESCREVENDO EM ARQUIVO ###
'''
write()             
writelines()        -> é um iterable, coloca todos os elementos

"""
file.write('Olá mundo!')

file.writelines(['1','2','3','4','5'])

"""
'''

### GERENCIANDO ARQUIVOS E DIRETÓRIOS ###
'''
Podemos criar, renomear e excluir diretórios usando os módulos 'os' e 'shutil'

"""
import os
import shutil

#Cria Diretorio
os.mkdir('exemplo')

#Renomeia arquivo
os.rename('arquivoold.txt','novonome.txt')

#Remover Arquivo
os.remove('unwanted.txt')

#Mover um Arquivo
shutil.move('origem.txt','destino.txt')


"""

########### EXEMPLO CODIGO ################

import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent  --> a variavel file dá o caminho até o arquivo + arquivo; Path pega só o caminho, da biblioteca pathlib.


os.mkdir('novo-diretorio')
os.mkdir(ROOT_PATH / 'novo-diretorio-dinamico')

arquivo = open(ROOT_PATH / 'novo.txt', 'w')
arquivo.close()

os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo_alterado.txt')

#os.remove(ROOT_PATH / 'novo_alterado.txt')

shutil.move(ROOT_PATH / 'novo.txt' , ROOT_PATH / 'outro-diretorio' / 'novo.txt')


'''

### Tratamento de Exceções Manipulando Arquivos ###
'''
### Exceções mais comuns:

FileNotFoundError -> arquivo não encontrado no diretorio

PermissionError -> tentativa de abrir arquivo se pemissões adequadas pra leitura ou gravação

IOError -> quando ocorre um erro de entrada/saida ao trabalahr com o arquivo. Ex: falta de permissão de gravação; espaço insuficiente

UnicodeDecodeError -> erro ao decodificar os dados de um arquivo de texto com uma codificação inadequada

UnicodeEncodeError -> erro ao codificar dados em uma determinada codificação ao gravar em um arquivo de Texto.

IsADiretoryError -> quando tenta abrir um aruqivo de texto e na verdade é um diretório

"""
try:
    file = open('naoexiste.txt','r')
except FileNotFoundError as exec:
    print('Arquivo nao encontrado')
    print(exec)
"""

'''

### BOAS PRATICAS ###
'''
# BLOCO WITH 
--> Use o context manager com a declaração 'with', garantido seu fechamento

with open('rquivo.txt','r') as arquivo

# VERIFIQUE SE O ARQUIVO FOI ABERTO COM SUCESSO

try:
    with open('arquivo.txt','r') as arquivo:
        #operacoes
    except IOError as exc:
        print(f'Nao abriu! {exc}')

#USE A CODIFICACAO CORRETA 

with open('arquivo.txt','r', encoding = 'utf=8') as arquivo

'''


### TRABALHANDO COM ARQUIVOS CSV ###
'''
'Comma Separated Values' - valores separados por virgula

## EXEMPLO DE CODIGO 

import csv

with open('example.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nome','idade'])
    writer.writerow(['Ana',30])
    writer.writerow(['Joao',25])

### Praticas Recomendadas 

- Usar csv.reader e csv.writer para manipular arquivos CSV.
- Fazer o tratamento correto das exceções
- Ao gravar arquivos CSV definir o argumento newline='' no método 'open'

### Exemplos

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv','w', encoding = 'utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(['id','nome'])
        escritor.writerows(['1','MARIA'])
        escritor.writerows(['2','JOAO'])
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')


try:
    with open(ROOT_PATH / 'usuarios.csv','r', newline='', encoding = 'utf-8') as arquivo:
        leitor = csv.writer(arquivo)
        for row in leitor:
            print(row[0],row[1])
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')


'''
