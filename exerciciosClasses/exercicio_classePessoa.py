## Classe Pessoa

# Crie uma classe que modele uma Pessoa:
## ATRIBUTOS : nome, idade, peso e altura
## METODOS: Envelhecer | Engordar | Emagrecer | Crescer
##          obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos
##          ela deve crescer 0,5 cm
import random

class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, altura:float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        print('Mais um ano se passou...')
        self.crescer()
        nova_idade = self.idade + 1
        self.idade = nova_idade
        
        numero = random.uniform(0, 3)
        if numero >1:
            print('chamar engordar')
            self.engordar()
        else:
            print('chamar emagrecer')
            self.emagrecer()
    
    def engordar(self):
        numero = random.uniform(0, 2)
        if numero == 0:
            msg = 'Não ganhei nada'
        elif numero > 0 and numero <= 10:
            msg = 'ganhei uns kilinhos...'
            novopeso = round(self.peso + abs(numero),2)
            self.peso = novopeso
        else :
            print('-- ERRO : VALOR INESPERADO--')
            return
        print(f'Sobre meu peso... dessa vez eu {msg} , mais especificamente {round(numero,2)} kg!')

    def emagrecer(self):
        if self.peso <= 0:
            print('Ia ficar com peso negativo! Precisei ser internado e ganhei 30 kilos!')
            self.peso = self.peso + 30
            return
        else:
            numero = random.uniform(-2, 0)
            if numero == 0:
                msg = 'Não perdi nada'
            elif numero < 0 and numero >= -10:
                msg = 'perdi uns kilinhos...'
                novopeso = round(self.peso - abs(numero),2)
                self.peso = novopeso
            else :
                print('-- ERRO : VALOR INESPERADO--')
                return
            print(f'Sobre meu peso... dessa vez eu {msg} , mais especificamente {round(numero,2)} kg!')


    def engordar_aleatorio(self):
        numero = random.uniform(-10, 10)
        if numero == 0:
            msg = 'Não ganhei nada'
        elif numero < 0 and numero >= -10:
            msg = 'perdi uns kilinhos...'
        elif numero > 0 and numero <= 10:
            msg = 'ganhei uns kilinhos...'
        else :
            print('-- ERRO : VALOR INESPERADO--')
            return
        print(f'Sobre meu peso... dessa vez eu {msg} , mais especificamente {round(numero,2)} kg!')

    
    def crescer(self):
        print('Um surto de crescimento!')
        numero = random.uniform(0, 0.1)
        if self.idade != 0 and self.idade < 21:
            novaltura = round(self.altura + numero,2)
            self.altura = round(novaltura,2)
            print(f'Cresci {round(numero,3)} metros! Agora minha altura é de {round(novaltura,2)} metros!')
    
    def retorno_idade(self):
        idade = self.idade
        return idade

    def retorno_peso(self):
        peso_atual = round(self.peso,2)
        return peso_atual
    
        
mateus = Pessoa('Mateus',1,9.8,0.77)
idade_do_mateus = mateus.retorno_idade()
anos = 0
idade_limite = 20
while idade_do_mateus < idade_limite:
    if anos > idade_limite:
        print(f'------------{anos} ANOS SE PASSARAM ----------')
    idade_do_mateus = mateus.retorno_idade()
    print('IDADE ATUAL:',idade_do_mateus)
    print('PESO ATUAL:',mateus.retorno_peso())
    mateus.envelhecer()
    anos = anos + 1
    print('-------------------------------------------------')
    

