#### CRIANDO UM PACOTE DE PROCESSAMENTO DE IMAGENS COM PYTHON ###

### Objetivos:
### 1) Entender conceitos relacionados aos pacotes
### 2) ATualizar o projeto e gerar as distribuições
### 3) Publicar o Pacote

## Modulo x Pacote
# Módulo = objeto que serve como unidde organizcional do código que é carregado pelo comando de import
# Pacote: coleção de módulos com hierarquia

## Modularização
# Vantagens : Legibilidade ; Manutenção; Reaproveitamento de código

## Pacote em Python
# Vantagens de criar um pacote: Facilidade de Compartilhamento, Facilidade de Instalação

#### CONCEITOS
## Pypi : repositório público oficial de pacotes
## Wheel e Sdist : dois tipos de distribuições
## Setuptools : pacote usado em setup.py para gerar as distribuições
## Twine: pacote usado para subir as distribuições no repositório Pypi


########## PARTE 2 - CRIAR O PROJETO E GERAR AS DISTRIBUIÇÕES ###########

###  Exemplos de estruturas de pacotes simples:

#simple-package-template
'''
project_name/
    README.md
    setup.py
    requirements.txt
    package_name/
        __init__.py
        file1_name.py
        file2_name.py
'''

## Exemplo de chamadas a file1_name:
# import package_name.file1_name
# from package_name import file1_name

###  Exemplos de estruturas de pacotes com vários módulos:

#package-template
'''
project_name/
    README.md
    setup.py
    requirements.txt
    package_name/
        __init__.py
        module1_name/
            __init__.py
            file1_name.py
            file2_name.py
        module2_name/
            __init__.py
            file1_name.py
            file2_name.py
'''

## Exemplo de chamadas a file1_name:
# import package_name.module1_name.file1_name
# from package_name.module1_name import file1_name

## Repositório de Exemplo: https://github.com/tiemi/

######################## PASSOS PARA CRIAR O PROJETO ######################## 
# 1.) Fork do template
# 2.) Adição do Conteúdo dos módulos do projeto
# 3.) Edição do arquivo 'setup.py'
# 4.) Edição do 'requirements.txt' 
# 5.) Edição do README.md

#####

######################## EDIÇÃO DO ARQUIVO 'SETUP.PY######################## 

# Faz os imports
from setuptools import setup, find_packages

#abre o Read-me
with open("README.md", "r") as f:
    page_description = f.read()

#abre o requirements para instalação
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",                        # nome do pacote
    version="0.0.1",                            # versionamento
    author="my_name",
    author_email="my_email",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,              #instala o requirements
    python_requires='>=3.8',
)


######################## CRIAR AS DISTRIBUIÇÕES######################## PARTE 5

# Para subir o pacote, criar uma distribuição binária ou distribuição de código fonte.
# As versões mais recentes do pip instalam primeiramente a binária e usam a distribuição de código fonte,
# apenas se necessário.

#### PASSOS PARA GERAR AS DITRIBUIÇÔES:
# 1) Acessar a raiz do projeto
# 2) Comandos de Instalação
'''
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
'''
# 3) Comando para criar a distribuição
'''
python setup.py sdist bdist_wheel
'''



######################## PUBLICNADO O PACOTE ###################### PARTE 6

#Passos para subir o pacote para o Pypi 
'''
1. Criar conta no Test Pypi
2. Publicr no Test Pypi
3. Instalar pacote usando Test Pypi
4. Testar pacote
5. Criar conta no Pypi
6. Publicar no Pypi
7. Instalar pacote usando
'''

### Criando conta no Pypi:
'''
https://pypi.org/account/register/
https://test.pypi.org/acoount/register/
'''

## Comando para publicar no Test Pypi
'''
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
'''

## Comando para publicar no  Pypi
'''
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
'''

###################################### ADICIONAIS #########################################

'''
Documentação do setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html

Testes automatizados: https://docs.pytest.org/en/latest/goodpractices.html

Uso do Tox: https://tox.readthedocs.io/en/latest/

'''


###################################### EXERCÍCIO PRÁTICO ###################################

'''
Fazer um pacote usando a estrutura SIMPLES de um módulo para testar os conhecimentos adquiridos
'''

