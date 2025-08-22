##### POLIMORFISMO ####

# O que é?
## Mesmo nome de função (com assinaturas diferentes) usado para tipos diferentes

# Exemplo - len
e = len('python')
c = len([10,20,30])
print(e,'\n',c)

## Polimorfismo com Herança

# Na herança, a classe filha herda os metodos da classe pai.
# No entanto, é possivel modificar um mtodo em uma classe filha herdada da pai.
# Util em momentos em que o metodo nao se encaix perfeitamente na classe filha

print('-----------------------\n')

class Passaro:
    def voar(self):
        print('Voando!')

class Pardal(Passaro):
    def voar(self):
#        print('Pardal voa')
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz NAO voa')

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
