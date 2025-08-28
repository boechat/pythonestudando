## Classe ContaCorrente

# Crie uma classe para implementar uma conta Corrente:
## ATRIBUTOS : Numero da Conta | Nome do Correntista | Saldo 
## METODOS: alterar_nome | deposito | saque
##          obs: No construtor saldo é opcional com valor default = 0 e os demais atributos obrigatórios


#########################################################################################################
import random

class ContaCorrente:
    def __init__(self, conta, cliente, saldo:float = 0):
        self.conta = conta 
        self.cliente = cliente
        self.saldo = saldo

    def alterar_nome(self):
        novonome = input('Entre com o novo nome da conta ::: ')
        self.cliente = novonome
        print('nome da conta alterada!')
    
    def deposito(self):
        dep = float(input('Entre com o valor a ser depositado em conta :::'))
        if dep >= 0:
            self.saldo = self.saldo + dep
            print(f'Deposito de R$ {dep} realizado!')
        else:
            print('Deposito inválido')
    
    def saque(self):
        sac = float(input('Entre com o valor a ser Sacado da conta :::'))
        if self.saldo < sac or self.saldo == 0:
            print('Saldo insuficiente, abortando operação')
        elif sac > 0:
            self.saldo = self.saldo - sac
            print(f'Retirada de R$ {sac}')
        else:
            print('Quantia inválida')
    
    def extrato(self):
        saldores = round(self.saldo,2)
        print(f'Saldo R$ {saldores}')


numero1 = ContaCorrente(100101,'Andre')
numero2 = ContaCorrente(100201,'Banofre',130)

numero1.deposito()
numero1.saque()
numero1.deposito()
numero1.saque()
numero1.extrato()

