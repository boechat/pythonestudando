########################### GERENCIAMENTO DE PACOTES , CONVENCOES E BOAS PRATICAS PYTHON ###########################
'''
O QUE SAO PACOTES?

- Módulos que podem ser instalados e utilizados em python; Permitem que você utilize código que foi escrito por outros.

PAPEL DO PIP

- Pip é o gerenciador de pacotes do python. Se comunica com o PyPI (Python Package Index) que é onde tem as maiorias dos pacotes armazenados de maneira pública.
- https://pypi.org

ex:
pip install numpu
pip uninstall numpy
pip list

AMBIENTE VIRTUAL
- Ambientes Virtuais, como os criados por venvs, nos permitem manter as dependencias de diferentes projetos.
- Importante para evitar conflitos entre versões de pacotes

Para criar o ambiente virtual, pasta usar:

-----------------------------------------------------------------------------------------------------

python3 -m venv NomeDoAmbienteVirtual   -------> [dessa forma cria-se o ambiente virutal]
source NomeDoAmbienteVirtual/bin/activate    -----> [e assim, ativa-se]

-----------------------------------------------------------------------------------------------------

Desativar o Ambiente Virtual:
- deactivate         

COMANDOS DO PIP

-Instalar pacote
pip install nome_do_pacote

-Desinstalar Pacote
pip uninstall nome_do_pacote

- Listar Todos os Pacotes Instalados
pip list

- Atualizar Pacote
pip install --upgrade nome_do_pacote

- Procurar por pacotes 
pip search termo_de_busca   ---> DEPRECADO! Tem que ir no pypi

'''

### GERENCIANDO DEPEDENCIAS COM O PIPENV ###
'''
PIPENV é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências 
com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes autoamticamente 
do arquivo pipfile conforme voc~e instala e desinstala pacotes.

-----------------------------------------------------------------------------
pip install pipenv
pipenv install numpy
pipenv uninstall numpy
pipenv lock           -----> gera um arquivo de lock e dependencias
pipenv graph          -----> mostra todas as dependências
pipenv clean          -----> desinstala todos os pacotes e suas dependencias
-----------------------------------------------------------------------------

Documentação: 
https://pipenv.pypa.io/en/latest/

'''

### GERENCIANDO DEPEDENCIAS COM O POETRY ###
'''
Outra ferramenta de gerenciamento de dependencias para Python, que permite declarar as bibliotecas
de que seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você.
Ela também suporta o EMPACOTAMENTE e a PUBLICAÇAÔ de projetos no PyPI

-----------------------------------------------------------------------------
pip install poetry
poetry new myproject                    ----> cria um projeto do zero
cd myproject                            ----> entra na pasta
poetry add numpy                        ----> adiciona
poetry remove numpy                     ----> remove
poetry init                             ----> caso tenha um projeto, ao inves de criar um, vc inicia ele.

-----------------------------------------------------------------------------
'''


