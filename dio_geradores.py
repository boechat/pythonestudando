### CONTEUDO BASEADO NA AULA GERADORES DA DIO 
### https://web.dio.me/track/luizalabs-back-end-com-python/course/decoradores-iteradores-e-geradores-com-python/learning/
## referencia: https://github.com/digitalinnovationone/trilha-python-dio

'''
Tipos especiais de iteradores; ao contrário das listas ou outros iteraveis, não armazem todos os seus valores em memória.

São definidos unsado funões regulares ,mas, ao invés de retornar valores usando 'return', utilizm 'yield'


CARACTERISTICAS DE GERADOR
* Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.
* O estado interno de um gerador é mantido entre chamadas.
* A execução de um gerador é pausada na declaração 'yield' e retomada daí na próxima vez que ele for chamado.


'''

'''
RECUPERANDO DADOS DE UMA API


* Solicitar dados por páginas(paginação).
* Fornecer um produto por vez entre as chamadas.
* Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas.
* Tratar o consumo da API como uma lista Python.


'''

### EXEMPLO DE CODIGO: 
'''
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?page={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

# Uso do gerador.
for product in fetch_products('http://api.example.com/products'):
    print(product['name'])
'''

### Outro Exemplo 
from typing import List

def meu_gerador(numeros):
    #contador += 1
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1,2,3]):
    print(i)
