############### CRIANDO UMA APLICACAO FASTAPI - DIO #########################

# Criando a primeira aplicação FASTAPI
# Após ter configurado o VSCode, criamos o main.py ; usaremos a referencia do https://fastapi.tiangolo.com/#create-it

from fastapi import FastAPI

app = FastAPI()

# Criar uma rota
@app.get("/")
def read_root():
    return {'message': 'Hello World'}
    # Retornar um dicionario pois irá converter para JSON

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
    INFO:     Started reloader process [x] using WatchFiles
    INFO:     Started server process [x]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.  
'''
