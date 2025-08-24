'''
Imagine que você está desenvolvendo um sistema de pagamentos online.
O sistema deve ser capaz de processar diferentes formas de pagamento (CartaoCredito, Boleto, Pix), mas todos devem ter um método chamado pagar(valor) que retorna se o pagamento foi bem-sucedido.

1) Crie uma classe abstrata Pagamento com o método pagar(valor) que será sobrescrito pelas subclasses.
2) Crie pelo menos 3 subclasses representando formas de pagamento diferentes:
  CartaoCredito → só aprova se o limite for suficiente.
  Boleto → sempre gera um código de barras e aprova o pagamento.
  Pix → só aprova se o saldo disponível for suficiente.
3) Crie uma função processar_pagamento(metodo_pagamento, valor) que use polimorfismo para processar qualquer forma de pagamento sem precisar saber a classe.
4) Teste o sistema com uma lista de diferentes métodos de pagamento.
'''

from abc import ABC, abstractmethod
import random


# Classe abstrata
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


# Subclasse Cartão de Crédito
class CartaoCredito(Pagamento):
    def __init__(self, limite):
        self.limite = limite

    def pagar(self, valor):
        if valor <= self.limite:
            self.limite -= valor
            return f"Pagamento de R${valor:.2f} aprovado no Cartão de Crédito. Limite restante: R${self.limite:.2f}"
        return f"Pagamento de R${valor:.2f} negado! Limite insuficiente."


# Subclasse Boleto
class Boleto(Pagamento):
    def pagar(self, valor):
        codigo = random.randint(1000000000, 9999999999)
        return f"Boleto gerado no valor de R${valor:.2f}. Código: {codigo}"


# Subclasse Pix
class Pix(Pagamento):
    def __init__(self, saldo):
        self.saldo = saldo

    def pagar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Pagamento de R${valor:.2f} via PIX concluído. Saldo restante: R${self.saldo:.2f}"
        return f"Pagamento de R${valor:.2f} via PIX negado! Saldo insuficiente."


# Função polimórfica
def processar_pagamento(metodo_pagamento: Pagamento, valor):
    print(metodo_pagamento.pagar(valor))


# Testando o sistema

metodos = [
    CartaoCredito(limite=1000),
    Boleto(),
    Pix(saldo=500),
]

valores = [250, 750, 300]

for metodo, valor in zip(metodos, valores):
    processar_pagamento(metodo, valor)
