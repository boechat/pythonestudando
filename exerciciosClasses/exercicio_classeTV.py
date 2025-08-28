############################################## # # # # # # Classe TV # # # # # # #############################################

# Faça um programa que simule um televisor criando como um objeto.
# O usuario deve informar o numero do canal e aumentar ou diminuir o volume.
# Certifique-se que o numero do canal e o nivel do volume permaneça dentro de faixas válidas



#############################################################################################################################
class TV:
    def __init__(self, canal=1, volume=10, canal_min=1, canal_max=99, volume_min=0, volume_max=100):
        # Dicionario com Atributos
        self.estado = {
            "canal": canal,
            "volume": volume,
            "canal_min": canal_min,
            "canal_max": canal_max,
            "volume_min": volume_min,
            "volume_max": volume_max
        }

    def mudar_canal(self, novo_canal):
        if self.estado["canal_min"] <= novo_canal <= self.estado["canal_max"]:
            self.estado["canal"] = novo_canal
            print(f"Canal alterado para {self.estado['canal']}")
        else:
            print(f"Canal inválido! Escolha entre {self.estado['canal_min']} e {self.estado['canal_max']}.")

    def aumentar_volume(self):
        if self.estado["volume"] < self.estado["volume_max"]:
            self.estado["volume"] += 1
        print(f"Volume atual: {self.estado['volume']}")

    def diminuir_volume(self):
        if self.estado["volume"] > self.estado["volume_min"]:
            self.estado["volume"] -= 1
        print(f"Volume atual: {self.estado['volume']}")

    def status(self):
        print(f"Canal: {self.estado['canal']} | Volume: {self.estado['volume']}")


#############################################################################################################################
tv = TV()

tv.mudar_canal(25)
tv.aumentar_volume()
tv.diminuir_volume()
tv.status()
