#Faça um Programa que Leia 5 números e informe o Maior numero
listnova = []
contar = 0
while True and contar <= 10 and len(listnova) != 5:
    try:
        numero_pedido = int(input('Entre com um Numero natural entre 0 e 10'))
    except ValueError:
        print('ERROR: Não é um número natural!')
        contar = contar + 1
    else:
        listnova.append(numero_pedido)
        print('Lista = ',listnova)
        print('Tamanho da Lista =',len(listnova))
        if len(listnova) == 5:
            print('Tamnho da Lista excedido')
            break
        else:
            print('--Adicione Mais Itens--')

if contar >= 11:
    print('--------------------')
    print('tentativas excedidas')

print('=====================')
print(f'Tentativas : {contar}')
print('=====================')
print('LISTA FINAL   ',listnova)
print('MAIOR NUMERO DA LISTA', max(listnova))
print('MENOR NUMERO DA LISTA', min(listnova))
print('SOMA DOS NUMEROS DA LISTA', sum(listnova))
print('MEDIA DOS NUMEROS DA LISTA FLOAT', float(sum(listnova)/len(listnova)))
print('MEDIA DOS NUMEROS DA LISTA INT', int(sum(listnova)/len(listnova)))


print('=====================')
