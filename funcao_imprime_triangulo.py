### FUNCAO IMPRIME TRIANGULO

# numero e tipo
def imprimir_tri(numero: int):
    for iterador in range(1, numero +1):
        for _ in range(iterador):
            print('x', end='  ')
        print('')

# Crescendo Numeros
def neo_imprimir_tri(numero: int):
    for iterador in range(1, numero +1):
        #print('iterador =',iterador)
        
        for j in range(iterador):
            if iterador == 1:
                print(iterador, end='  ')
            else:
                print(j + 1, end = ' ')
        print('')

imprimir_tri(4)
print('---------')
neo_imprimir_tri(4)
