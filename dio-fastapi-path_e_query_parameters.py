############### CRIANDO UMA APLICACAO FASTAPI - DIO #########################

# Continuando a aplicação FASTAPI, agora mexendo mais com Path e Query Parameters
# Após ter configurado o VSCode, criamos o main.py ; usaremos a referencia do https://fastapi.tiangolo.com/#create-it

from fastapi import FastAPI

app = FastAPI()

# Criar uma rota
'''
@app.get("/")
def read_root():
    return {'message': 'Hello World'}
    # Retornar um dicionario pois irá converter para JSON
'''
    

'''
Para rodar a aplicação, precisa acessar o terminal, acessando a pasta local (/dio-blog)
Entrar com o comando:
    uvicorn main:app --reload
                main  --> nome do arquivo
                app   --> nome da variavel que chama FastAPI()
                      --reload quer dizer que a cada modificação, o servidor vai recarregar automaticamente o código feito

    Resultado da run no powershell terminal:
    INFO:     Will watch for changes in these directories: ['F:\\RPA\\DIO-API\\dio-blog']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)                 --------> Informa onde está
    INFO:     Started reloader process [11524] using WatchFiles
    INFO:     Started server process [22716]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.  
'''

##### ESTRUTURA BÁSICA DE UMA API FASTAPI ####
# Usamos mvc (models / views / control)
# Entaõ na estrutura de pastas, criamos as pastas : models ; services ; controllers; views;

#### ROTAS E ENDPOINTS EM FAST API - PATH PARAMETER ### 
# Path Parameter -> são os parametros que vem no endereço da requisição (url)

from datetime import datetime, UTC

@app.get("/posts/{framework}")
def read_postst(framework):
    return {
        'posts': [
            {'title': f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            {'title': f'Internalizando uma APP {framework}','date': datetime.now(UTC)},
        ]
    }
    # agora, para verificar, ir em http://localhost:8000/posts/  e adicionar o framework que quer procurar, por exemplo: http://localhost:8000/posts/django 


### PASSAGEM DE PARAMETROS COM TIPOS

@app.get("/posts/{framework}")
#def read_postst(framework : str):    #---> estabeleço que o framework é do tipo string
def read_postst(framework : int):    #---> estabeleço que o framework é do tipo int, então só recebe int na url de consulta
    return {
        'posts': [
            {'title': f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            {'title': f'Internalizando uma APP {framework}','date': datetime.now(UTC)},
        ]
    }

#### ROTAS E ENDPOINTS EM FASTAPI - QUERY PARAMETERS

# Quando passamos argumentos pro FastAPI e não for um PathParameter, por padrão ele entende que é um QUERY PARAMETER
# Para construirmos um endpoint query, basta passarmos os parametros como argumentos da função
# ex: async def read_item(skip: int = 0, limit: int = 10):
#        return fake_items_db[skip: skip+limit]

# Vamos criar uma variavel chamada fake_db, como uma lista com objetos
fake_db = [
            {'title': f'Criando uma aplicação com DJANGO','date': datetime.now(UTC)},'published' : True
            {'title': f'Internalizando uma APP FASTAPI','date': datetime.now(UTC)},'published' : True
            {'title': f'Internalizando uma APP FLASK','date': datetime.now(UTC)},'published' : True
            {'title': f'Internalizando uma APP STARLETT','date': datetime.now(UTC)},'published' : False
]

lenght = len(fake_db)
@app.get('/posts')
def read_posts(skip: int = 0, limit: int = lenght, published: bool = True):
    return [post for post in fake_db[skip: skip+ limit] of post ['published'] is published]  # paginacao

def read_framework_posts(framework : str):    
    return {
        'posts': [
            {'title': f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            {'title': f'Internalizando uma APP {framework}','date': datetime.now(UTC)},
        ]
    }
