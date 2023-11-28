# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadruplicar(numero):
    return numero * 4

numero = int(input())

print('Forma Simples :',duplicar(numero))

########### OUTRA FORMA ####################

def criar_multi(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multi(2)
triplicar = criar_multi(3)
quadruplicar = criar_multi(4)

print('Forma Dois Duplicar:', duplicar(numero))
print('Forma Dois Triplicar:',triplicar(numero))
print('Forma Dois Quadruplicar:',quadruplicar(numero))

