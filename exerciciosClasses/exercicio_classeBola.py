#### CRIE UMA CLASSE QUE MODELE UMA BOLA 
# Atributos: Cor, Circunferencia, Material
# Metodos: TrocaCor e MostraCor


##########################################################################

class Bola:
    def __init__(self, cor,circunferencia,material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    def trocaCor(self,cor_nova):
        print('Bora trocar de Cor!')
        print(f'A cor antiga era: {self._cor} e vai virar {cor_nova}')
        self._cor = cor_nova
        
    def mostraCor(self):
        print('A cor da bola é : ',self._cor)

basquete = Bola('laranja',30,'borracha')

print(basquete)
basquete.mostraCor()
basquete.trocaCor('azul')
basquete.mostraCor()

