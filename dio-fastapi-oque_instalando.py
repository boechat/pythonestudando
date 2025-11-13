################################ FastAPI - O que é e como Instalar no VSCODE usando poetry ################################ 
'''
FastAPI é um framework web para construição de APIs com Python.

Pontos Positivos:
- Alto Desempenho : Superior ao Flask, comparavel ao NodeJS
- Geração de Documentação Automatica: Suporta OpenAPI para documentação
- Validação de dados e serialização: Usa o Pydantic para validação de dados e serialização automática
- Facilidade de uso: Aprender e começar a usar o FastAPI é considerado simples
- Suporte a async/await: Suporte nativo para operações assíncronas, o que é ótimo para lidar com operações de IO.

Pontos Negativos:
- Comunidade menor
- Maturaidade : relativamente novo, com menos plugins
- Complexidade em Projetos Grandes

######################################################################
Instalando FastAPI

- Abre o Terminal
- Tendo o poetry instalado, vamos usa-lo:
    -poetry init
        - depois de configurado o pacote, é gerado o py project
    -poetry env info
        - Vermos o ambiente env, agora vamos atualizar as dependecias
    -poetry add 'fastapi=*'
        - Instala a ultima versão do fastapi e cria o ambient venv, que pode ser verificado com o poetry env info
        - Pegar o caminho completo com o 'poetry env info' na linha PATH 
        - apertar 'ctrl + shift + p' e procurar por selecionar interpretador
        - clicar, ir em INSIRA O CAMINHO DO INTERPRETADOR e colar a info copiada do PATH
            - Com isso, no VSCODE quando você abrir um novo terminal ele já vai abrir com a virtual env selecionada
    - Com isso, já instalamos a API, mas precisa instalar também o ASGI Server ('uvicorn[standard])
    - poetry add 'uvicorn[standard]'
        - Agora foi adicionado às dependencias
    - Vamos verificar se está tudo ok, digitando o comando 'python' no terminal
    - import fastapi
    - dir(fastapi)
        - esse comando verifica se está tudo dentro do fastapi para você
'''
