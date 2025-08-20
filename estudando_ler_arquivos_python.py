### LENDO E CRIANDO ARQUIVOS EM PYTHON
# Com base no Desafio DevPro https://youtu.be/XNkHgDkTY4o

# Faça um programa que leia um aruqivo texto contento uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos
#
######################################################

def validar(ip: str) -> bool:
    numeros = ip.split('.')  # Separa o caracteres por ponto, retornando uma lista
    # Ve se a lista tem tamanho 4
    if len(numeros) != 4:
        return False
    for n in numeros:
        # iterando por todos os numeros da lista como string
        if not n.isdigit():
            return False
        if not (0 <= int(n) <= 255):  # vê se está entre 0 e 255
            return False
    return True


#  listas
ips_validos = []
ips_invalidos = []
# abrir o arquivo ips.txt, no modo read (r)
with open('ips.txt', 'r') as arquivo:
    for linha in arquivo:
        # Ler linha a linha
        #print(linha.strip())  # strip remove todos os espaços vazios, tabs e caracteres especiais (como pular linha)
        ip = linha.strip()
        #print('Ip :',ip, '| IS VALID = ', validar(ip))
        if (validar(ip)) == True:
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

print('\n--------IPS VALIDOS-----------\n',ips_validos,'\n----------------------------')
print('\n-------IPS INVALIDOS----------\n',ips_invalidos,'\n----------------------------')

# Cria/ Escreve o arquivo de saída 
with open('ips_saida.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços Válidos:]\n')

    for i in ips_validos:
        arquivo.writelines(f'{i}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços Inválidos]\n')

    for i in ips_invalidos:
        arquivo.writelines(f'{i}\n')
