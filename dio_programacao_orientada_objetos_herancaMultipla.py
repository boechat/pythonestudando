class Animal:
    def __init__(self,numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {[', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())]}"


class Ave(Animal):
    def __init__(self,cor_do_bico,**kw):
        super().__init__(numero_patas=kw['numero_patas'])
        self.cor_do_bico = cor_do_bico

    def poe_ovo(self):
        print('Ponho Sim!')

class Mamifero(Animal):
    def __init__(self,cor_pelo,**kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Gato(Mamifero):
    pass

class Cachorro(Mamifero):
    pass

class Onitorrinco(Mamifero,Ave):
    def __init__(self,cor_pelo,cor_do_bico, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_do_bico=cor_do_bico, numero_patas = numero_patas)
        Onitorrinco.mro()
        print('Ordem de Resolução: ',Onitorrinco.mro())
    pass

####################### executa
gato = Gato(numero_patas=4,cor_pelo='preto')
print(gato)

perry = Onitorrinco(numero_patas=4,cor_pelo='verde com Chapéu',cor_do_bico='amarelo')
print(perry)
perry.poe_ovo()
