# Exercicio de Estrutura de Repetição usando Try / Except e um contador

contar = 0
while True and contar <= 4:
    try:
        numero_entrada = int(input('Entre com um Numero natural entre 0 e 10'))
    except ValueError:
        print('ERROR: Não é um número natural!')
        contar = contar + 1
    else:
        if 0 <= numero_entrada <= 10:
            print(f'Numero informado é: {numero_entrada}')
            break
        else:
            print('O numero deve estar entre 0 e 10, tente novamente')
            contar = contar + 1

if contar >= 4:
    print('--------------------')
    print('tentativas excedidas')
