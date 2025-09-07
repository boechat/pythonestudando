import random

class Stats:
    def __init__(self, ranges):
        """
        ranges: dicionário com valores min e max de cada stat
        Exemplo: { "hp": (16, 20), "str": (4, 6) }
        """
        
        self.hp = random.randint(*ranges["hp"])
        self.str = random.randint(*ranges["str"])
        self.skl = random.randint(*ranges["skl"])
        self.spd = random.randint(*ranges["spd"])
        self.lck = random.randint(*ranges["lck"])
        self.defense = random.randint(*ranges["defense"])
        self.res = random.randint(*ranges["res"])
        self.mov = ranges["mov"]  # movimento fixo normalmente

    def mostrar(self):
        print(f"HP: {self.hp}, Str: {self.str}, Skl: {self.skl}, Spd: {self.spd}, "
              f"Lck: {self.lck}, Def: {self.defense}, Res: {self.res}, Mov: {self.mov}")

    def aumentar(self, stat):
        if hasattr(self, stat):
            setattr(self, stat, getattr(self, stat) + 1)

class Hero:
    def __init__(self, nome, stat_ranges, crescimento):
        self.nome = nome
        self.level = 1
        self.exp = 0
        self.stats = Stats(stat_ranges)  # agora gera aleatório
        self.crescimento = crescimento

    def mostrar_stats(self):
        print(f"\n👤  {self.nome} - Nível {self.level}")
        self.stats.mostrar()
    
    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        print(f"\n{self.nome} ganhou {quantidade} XP! (Total: {self.exp}/100)")
        while self.exp >= 100:
            self.subir_nivel()
            self.exp -= 100
    
    def subir_nivel(self):
        if self.level <10:
            self.level += 1
            print(f"\n⬆️ {self.nome} subiu para o nível {self.level}!")
            for stat, chance in self.crescimento.items():
                if random.randint(1, 100) <= chance:
                    self.stats.aumentar(stat)
                    print(f"  {stat} aumentou para {getattr(self.stats, stat)}!")
        else:
            print('Nível Máximo!')




# -----------------------------
# Função de ataque
# -----------------------------
def atacar(atacante, defensor):
    # Chance de acertar baseada no Skill
    acerto = 75 + (atacante.stats.skl - defensor.stats.spd) * 2
    acerto = max(10, min(acerto, 95))  # limite entre 10% e 95%
    if random.randint(1, 100) <= acerto:
        # Dano base
        dano = atacante.stats.str - defensor.stats.defense
        dano = max(0, dano)

        # Chance de crítico baseada em Lck
        critico = random.randint(1, 100) <= atacante.stats.lck
        if critico:
            dano *= 3
            print(f"💥 CRÍTICO! {atacante.nome} causa {dano} de dano!")
        else:
            print(f"{atacante.nome} causa {dano} de dano.")

        defensor.stats.hp -= dano
        if defensor.stats.hp < 0:
            defensor.stats.hp = 0
    else:
        print(f"{atacante.nome} errou o ataque!")

# -----------------------------
# Combate por turnos
# -----------------------------
def combate(hero1, hero2):
    print("\n⚔️ Combate iniciado!")
    turnos = 1
    while hero1.stats.hp > 0 and hero2.stats.hp > 0:
        print(f"\n--- Turno {turnos} ---")
        hero1.mostrar_stats()
        hero2.mostrar_stats()

        atacar(hero1, hero2)
        if hero2.stats.hp <= 0:
            print(f"\n🏆 {hero1.nome} venceu!")
            break

        atacar(hero2, hero1)
        if hero1.stats.hp <= 0:
            print(f"\n🏆 {hero2.nome} venceu!")
            break

        turnos += 1

# -----------------------------
# Exemplo de uso
# ----------------------------


#####################################################################################################
if __name__ == "__main__":
    
####################################################################
    # Ranges iniciais estilo "Lord"
    stat_ranges = {
        "hp": (16, 20),
        "str": (4, 6),
        "skl": (4, 6),
        "spd": (6, 8),
        "lck": (6, 8),
        "defense": (4, 6),
        "res": (0, 2),
        "mov": 5  # fixo
    }

    # Taxas de crescimento
    crescimento = {
        "hp": 80,
        "str": 45,
        "skl": 50,
        "spd": 40,
        "lck": 45,
        "defense": 30,
        "res": 35,
        "mov": 0
    }
    
        # Ranges iniciais estilo "Lord"
    sentai_stat_ranges = {
        "hp": (14, 22),
        "str": (2, 8),
        "skl": (4, 6),
        "spd": (2, 8),
        "lck": (2, 4),
        "defense": (2, 9),
        "res": (0, 3),
        "mov": 6  # fixo
    }

    # Taxas de crescimento
    sentai_crescimento = {
        "hp": 60,
        "str": 40,
        "skl": 70,
        "spd": 50,
        "lck": 50,
        "defense": 30,
        "res": 35,
        "mov": 0
    }
#######################################################################
    heroi = Hero("Red Phoenix", sentai_stat_ranges, sentai_crescimento)
    heroi.mostrar_stats()

    heroi2 = Hero('Spoiler', stat_ranges, crescimento)
    heroi2.mostrar_stats()
    
    
    # Simulação de batalhas
    for _ in range(40):
        heroi.ganhar_exp(random.randint(40, 60))
        heroi2.ganhar_exp(random.randint(40, 60))
    
    heroi.mostrar_stats()
    heroi2.mostrar_stats()


###########################################################################

    combate(heroi, heroi2)
