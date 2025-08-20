# Baseado no desafio da Aula 11 do Desafio DevPro : https://youtu.be/XNkHgDkTY4o
#
#
## 2) A ACME Inc., uma empresa de 500 funcionarios está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o ADM da rede precisa saber qual o espaço ocupado pelos usuarios e identificar os usuarios com maior espaço ocupado
# Através de um programa baixado da internet, ele conseguiu gerar o arquivo 'usuarios.txt'

# A partir do arquivo, deve criar um programa que gere um relatorio chamado 'relatorio.txt'

####################################################################################

lista_cabecalho = ['Nr.','\t\t\tUsuario','\t\t\tEspaço Utilizado','\t\t\t% do uso ']
lista_nomes = []
lista_espaco = []
lista_porcentual = []
lista_iterador = []
listafinal = []


def calcula_bytes(valor):
    MB = valor / 1024 / 1024
    MB = round(MB,2)
    return MB

# with open('/txt/usuarios.txt', 'r') as arquivo:
with open('usuarios.txt', 'r') as arquivo:
    calculo = 0
    for linha in arquivo:
        usuario = linha.strip()
        linha_usuario = usuario.split()
        for linha_valida in linha_usuario:
            if linha_valida.isdigit():
                #print(linha_valida)
                espaco_utilizado = calcula_bytes(float(linha_valida))
                espaco_utilizado = (str(espaco_utilizado)+ ' MB')
                lista_espaco.append(espaco_utilizado)
                calculo = calculo + float(linha_valida)
            else:
                lista_nomes.append(linha_valida)
                #listafinal.append(usuario)


    # Descobre a Quantidade Total Ocupada em MB
    #print('LISTA NOMES',lista_nomes,'\n')
    #print('LISTA ESPACO', lista_espaco, '\n')
    TOTAL_MB = calcula_bytes(calculo)
    #print('TOTAL_MB: ',TOTAL_MB)
    tamanho = len(lista_nomes)
    #print(tamanho)
    ESPACO_MEDIO = TOTAL_MB / tamanho
    ESPACO_MEDIO = round(ESPACO_MEDIO,2)
    #print('ESPACO_MEDIO: ', ESPACO_MEDIO)

    for iterador, nome in enumerate(lista_nomes):
        for espaco in lista_espaco:
            #print('espaco:',espaco)
            if espaco == lista_espaco[iterador]:
                espaco_float = float(espaco.replace(" MB", ""))
                # (iterador+1, nome, lista_espaco[iterador],' MB')
                lista_iterador.append(iterador+1)
                porcentagem = (espaco_float / TOTAL_MB) * 100
                porcentagem = round(porcentagem,2)
                porcentagem = str(porcentagem) + '%'
                lista_porcentual.append(porcentagem)
                #print('PORCENTAGEM',porcentagem)
        #print(linha_usuario)

    #print(lista_iterador,'\n',lista_nomes,'\n',lista_espaco,'\n',lista_porcentual)

    listafinal = [list(t) for t in zip(lista_iterador, lista_nomes, lista_espaco, lista_porcentual)]
    #print(listafinal)


with open('relatorio.txt', 'w') as arquivo:
    arquivo.writelines('ACME Inc.                      Uso do Espasço Em Disco Pelos Usuarios\n')
    arquivo.writelines('#####################################################################\n')
    arquivo.writelines('\n')

    arquivo.writelines(lista_cabecalho)
    arquivo.writelines('\n')

    for linha in listafinal:
        # converte cada elemento em string e junta por vírgula (ou outro separador)
        linha_str = '\t\t\t'.join(map(str, linha))
        arquivo.write(linha_str + "\n")

    arquivo.writelines('\n')
    msg_final = 'Espaço Total Ocupado: ' + str(TOTAL_MB) + ' MB'
    arquivo.writelines(msg_final)
    arquivo.writelines('\n')
    msg_final = 'Espaço Médio Ocupado: '+ str(ESPACO_MEDIO) + ' MB'
    arquivo.writelines(msg_final)

