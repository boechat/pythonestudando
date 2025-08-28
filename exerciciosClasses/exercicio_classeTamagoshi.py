### Classe Bichinho Virtual
# Crie uma classe que modele um Tamagoshi
## ATRIBUTOS: Nome | Fome | Saude | Idade
## METODOS: Alterar Nome | Alterar Fome | Alterar Saude | Alterar Idade 
##          Retornar Nome | Retornar Fome | Retornar Saude | Retornar Idade
##
## obs: Considerar também HUMOR ; Humor é uma combinação entre os atributos Fome e Saúde. Não devemos criar
## um atributo para armazer por que ela pode ser calculada a qualquer momento.

import random


class Tamagoshi:
    def __init__(self, nome: str, fome: int = 0, saude: int = 10, idade: int = 0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

### ALTERAR 

    def alterar_nome(self):
        novonome = input('Qual é o novo nome do Bichinho?')
        novonome = self._nome 
        return 

    def alterar_fome(self,alterafome):
        self._fome = self._fome + alterafome
        return
    
    def alterar_saude(self,alterasaude):
        self._saude = self._saude + alterasaude
        return 
    
    def alterar_idade(self,tempo):
        self._idade = self._idade + tempo

### Retornar 
    def retornar_nome(self):
        return self._nome
    def retornar_saude(self):
        return self._saude    
    def retornar_idade(self):
        return self._idade
    def retornar_fome(self):
        return self._fome

## Classe Comidinhas, pro Tamagoshi comer!
class Comidinhas:
    def __init__(self,nome,valor_nutri: int = 1):
        self.nome = nome 
        self.valor_nutri = valor_nutri


# Função Humor
def humor(saude, fome):
    if saude > 0 and fome > 0:
        humor = saude + fome 
        if humor >= 10 and humor < 15:
            print('HUMOR: Felizinho!')
        elif humor >= 15 and humor < 35:
            print('HUMOR: Contente!')
        elif humor >= 35:
            print('HUMOR: RADIANTE!!!')
        else:
            print('HUMOR:  Tristonho')
    else:
        humor = -1
        print('------ HUMOR: DOENTE! ---------')
    
######### INICIO
lista_frutas = ['laranja','pera','uva','mamao','melancia','tomate']
for i,item in enumerate(lista_frutas):
    #print(lista_frutas[i])
    if(lista_frutas[i] == 'melancia' or lista_frutas[i] == 'pera'):
        lista_frutas[i] = Comidinhas(item,6)
    elif(lista_frutas[i] == 'uva' or lista_frutas[i] == 'laranja'):
        lista_frutas[i] = Comidinhas(item,5)
    else:
        lista_frutas[i] = Comidinhas(item)

toto = Tamagoshi('toto')
ano = 0
for i in range(10):
    print(f'=====================RODADA {i} ================')
    ano = ano + 1
    numero = random.randint(0, len(lista_frutas)-1)
    aleatorio = random.randint(0, 2)
    print('aleatorio = ',aleatorio)
    if aleatorio == 1:
        print(f'Vai comer uma fruta: {lista_frutas[numero].nome}')
        valor_nutricional = lista_frutas[numero].valor_nutri
        print('Que Fruta gostosa! recupera ',valor_nutricional, ' de Fome!')
        toto.alterar_fome(valor_nutricional)    
    elif aleatorio == 2:
        print(f'Hora de ir ao médico, recupera {numero} de Saude!')
        toto.alterar_saude(numero)    
    else:
        print('Negligencia, perde 1 de fome e 1 de saude')
        toto.alterar_fome(-1)
        toto.alterar_saude(-1)
    toto.alterar_idade(1)
    print('-----------------')
    print(toto.retornar_nome())
    print('IDADE :',toto.retornar_idade())
    print('FOME :',toto.retornar_fome())
    print('SAUDE :',toto.retornar_saude())
    print('-----------------')



toto.retornar_nome()
toto.retornar_idade()
fm = toto.retornar_fome()
sd = toto.retornar_saude()

print('\n\n---------- FIM DE JOGO -----------')
print('FOME: ',fm,'|| SAUDE: ',sd)

humor(fm,sd)

    
    
