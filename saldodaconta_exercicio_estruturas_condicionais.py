# Identação e Blocos ; Estruturas condicionais e de Repetição 
# Conforme visto no bootcamp da DIO - Suzano Python Developer 2

#Saldo da Conta - constante
saldo_da_conta = 500

def sacar(valor,saldo):
    
    if saldo >= valor:
        saldo -= valor
        print('valor sacado!')
        print(f'novo saldo: {saldo}')
        return saldo
    else:
        print('Saldo Insuficente!, Saque não realizado!')
        return saldo
        
def depositar(valor,saldo):
    saldo = valor + saldo
    print(f'Depositado : {valor}')
    print(f'novo saldo: {saldo}')
    return saldo
    
'''
print('--------SACAR--------')    
valor_saque = float(input('Entre com o valor a ser SACADO no nosso sistema!'))
saldo = sacar(valor_saque,saldo_da_conta)
print(f'Saldo após Saque: {saldo}')
print(' ')
print('--------DEPOSITAR--------')   
valor_depositar = int(input('Entre com o valor a ser depositado no nosso sistema!'))
saldo = depositar(saldo,valor_depositar)
print(f'Saldo após Depósito: {saldo}')
'''

print(f'------------------BEM VINDO AO SISTEMA BANCARIO!------------------------------')

nome = str(input('Por favor, se Identifique; Digite Seu Nome e Sobrenome.\n Ex:Nataniel Silva'))
mensagem = f"Olá, {nome}! Bem-vindo ao sistema." if nome else "Falha: você não digitou o nome."

print(mensagem)
print('-------------------------------------------------------------------------------')

opcao = 0
cont = False
while opcao != 4:
    if cont == False:
        opcao = int(input('Bom Dia! Qual operação você gostaria de Fazer Hoje?\nDigite :\n[1] SACAR [2] EXTRATO [3] DEPOSITO [4] SAIR'))
    else:
        opcao = int(input('Gostaria de Realizar mais uma transação?\nDigite :\n[1] SACAR [2] EXTRATO [3] DEPOSITO [4] SAIR'))
    
    if opcao == 1:
        print('--------SACAR--------')    
        valor_saque = float(input('Entre com o valor a ser SACADO no nosso sistema!'))
        saldo = sacar(valor_saque,saldo_da_conta)
        print(f'Saldo após Saque: {saldo}')
        print(' ')
        cont = True
    elif opcao == 2:
        print('-------EXTRATO-------')
        print(f'Seu Saldo Atual é De: {saldo}')
        print(' ')
        cont = True
    elif opcao == 3:
        print('--------DEPOSITAR--------')   
        valor_depositar = int(input('Entre com o valor a ser depositado no nosso sistema!'))
        saldo = depositar(saldo,valor_depositar)
        print(f'Saldo após Depósito: {saldo}')
        print(' ')
        cont = True
    elif opcao == 4:
        print('--------SAIR--------')   
        print(f'Obrigado por usar os Nossos Serviços! Volte Sempre!')
        print(' ')
        
