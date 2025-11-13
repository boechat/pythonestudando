#### INTRODUÇÂO AO DESENVOLVIMENTO WEB
'''
Como visto em : https://web.dio.me/track/luizalabs-back-end-com-python/course/introducao-ao-desenvolvimento-web-com-python

O QUE É DESENVOLVIMENTO WEB?
    - Processo de criação de websites e aplicações para internet ou uma intranet.

COMPONENTES PRINCIPAIS:
    - FRONTEND - a parte do website que os usuarios interagem diretamente.
                - envolve tecnologias como HTML, CSS e JavaScript
    
    - BACKEND   - Onde ocorrem o processamento de dados, gerenciamento de BD e controle do servidor.
                - Envolve linguagens como Python, Java , etc 

################################################################################

COMO A WEB FUNCIONA?
-   Internet vs Web
        Internet é uma rede global de computadores interconectados.
        Web (WWW) é um sistema de informação construído sobrea a internet que utiliza o protocolo HTTP para transmitir dados

-   Funcionamento de Um Website
    1: Solicitação do Usuario: usuario entra com url no navegador
    2: Resolução de DNS : O URL é traduzido em um endereço IP através de um sistema chamado DNS.
    3:  Conexão com o servidor: O navegador utiliza o endereço IP para estabelecer uma conexão com o servidor que hospeda o site. 
    4:  Resposta do servidor: O servidor processa a solicitação HTTP e envia de volta os aruqivos, geralmente em HTML, CSS e Javascript
    5:  Rendereização no Navegador: O Navegador interpreta esses arquivos e exibe os sites ao usuario.
    
################################################################################

Tecnologias front-end e back-end

FRONT-END - refere-se à parte do desenvolvimento web que lida com a interface do usuário.
O Objetivo é apresentar informações de forma interativa e acessível para o usuário final.
    HTML - estrutura o conteudo da web
    CSS - estiliza e apresenta o conteudo HTML
    JAVASCRIPT - torna as páginas web interativas e dinâmicas.

BACK-END - é a parte do site que o usuáro não vê. Inclui servidor, aplicação e banco de dados.
É responsável por gerenciar e processar dados, garantindo que tudo no front-end funcione corretamente.

LINGUAGENS E TECNOLOGIAS
- Linguagens: Python, Ruby, PHP, Java, JavaScript
- Banco de dados: PostrgreSQL, MySQL, MongoDB, Oracle
- Frameworks: Django(Python) , Express (JAvascript)l SpringBoot (Java)

DESENVOLVIMENTO FULLSTACK
- Profissionais que tem habilidades tanto em Front-End quanto em Back-End; sendo capazes de trabalhar em ambas as
áreas do desenvolvimento Web 

################################################################################

APIs 

O QUE É UMA API? 
- Interface de Programação de Aplicações; é um conjunto de regras e definições que permite que diferentes aplicações definições
software ou componentes se comuniquem entre si.
Funciona como um intermediário, permitindo que pedidos sejame feitos e respostas sejam recebidades entre diferentes sistemas de software.

APIs NO CONTEXTO DA WEB
- Na Web, as APIs são usadas para permitir a interação entre diferentes serviços e aplicações,
como enviar dados de um usuário de um aplicativo para um servidor ou solicitar dados de
um serviço externo (por exemplos, redes sociais, mapas, previsão do tempo)

IMPORTANCIA DAS APIs
- As APIs são cruciais para a construção de aplicações modernas e escalaveis. 
Elas permitem a flexibilidade para integrar e expandir funcionalidades sem reinventar a roda.

TIPOS DE APIS - RESTful, SOAP e GraphQL

- RESTful refere-se a APIs que seguem os principios do REST (Representational State Transfer).
Baseadas em padrões HTTP e utilizadas para interações Web
    Caracteristicas: 
        Uso dos métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD
        Curva de Aprendizado menor
        Fácil de entender e implementar
    
- SOAP (Simple Object Access Protocol) é um protocolo que define um padrão para a troca
de mensagens baseadas em XML.
    Caracteristicas:
        Protocolo baseado em XML para troca de informações.
        Independente de linguagem e plataforma de transporte
        Suporte para operações complexas e segurança avançada
        
- API GraphQL é uma linguagem de consulta para API, e um servidor capaz de executar
essas consultas, retornando apenas os dados especificados.
ex: https://studio.apollographql.com/public/SpaceX-pxxbxen/variant/current/explorer
    Características:
        Permite que os clientes especifiquem exatamente quais dados querem.
        Eficiente na redução de solicitações e no tamanho dos dados transferidos.
        Flexível e fortemente tipada, facilitando a evolução das APIs.
        
ESCOLHENDO O TIPO CERTO DE API
- A escolha depende das necessidades do projeto e dos recursos disponiveis.
RESTful é popular pela simplicidade; SOAP é preferido para segurança e transações complexas; 
GraphQL é ideal para aplicações que requerem dados dinâmicos personalizados

################################################################################

VERBOS HTTP: GET, POST, PATCH, PUT e DELETE

Em APIs RESTful, os verbos HTTP se alinham com operações CRUD.

CONVENÇÔES RESTFUL 
    GET - leitura
    POST - criação
    PUT / PATCH - atualização
    DELETE - remoção

#################################################################################

Artigo de Boas Práticas Profissionais para APIs Restful
https://web.dio.me/articles/7-boas-praticas-para-apis-restful-profissionais


'''
