class Filme:
    def __init__(self, nome, ano, duracao):     #Correto, sem o construtor nós precisaríamos definir os atributos depois de instanciar, teríamos o trabalho de descobrir quais atributos definir.
        #self.nome =  nome.capitalize()  #O Capitalize faz com que todos o primeiro nome saia com a primeira letra Maiúscula
        self.__nome = nome.title()  #Title deixa todos os nomes com letra maiuscula
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0  #valor inicial de likes

    @property  # usar property é uma ótima prática. Quando criamos getters e setters todos os lugares que já acessam a classe precisam mudar.
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0  #valor inicial de likes

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()





vingadores = Filme('vingadores',2008,160)
atlanta = Serie('atlanta',2017,2)

for i in range (5):
    atlanta.dar_like()
for i in range (15):
    vingadores.dar_like()

print(f'nome: {vingadores.nome} - Ano: {vingadores.ano} -Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')
print(f'nome: {atlanta.nome} - Ano: {atlanta.ano} -Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
