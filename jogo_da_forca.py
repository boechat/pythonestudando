### COM BASE NO VIDEO : DesafioDevPro Aula 10 https://youtu.be/QvrOUHX9hcI ####

import pandas as pd
import unicodedata

palavras_csv = """pilates,alongamento,postura,core,respiração,estabilidade,flexibilidade,equilíbrio,
fortalecimento,coluna,lombar,cervical,mobilidade,alinhamento,consciência,controle,precisão,fluidez,
resistência,relaxamento,dor,alívio,bem-estar,saúde,condicionamento,funcional,solo,aparelhos,reformer,
cadillac,chair,spine,bola,faixa,elástico,prancha,abdômen,glúteos,pernas,braços,ombros,joelhos,tornozelos,
aquecimento,recuperação,prevenção,lesões,ergonomia,homeoffice,sedentário,ansiedade,estresse,sono,rotina,
iniciante,intermediário,avançado,tutorial,guia,exercícios,sequência,desafios,dicas,mitos,verdades,correção,
técnica,postura-ereta,alongamento-matinal,alongamento-noturno,respiração-diafragmática,consciência-corporal,
alinhamento-pélvico,neutral-spine,estabilidade-lombar,mobilidade-torácica,fortalecimento-profundo,ativação,
propriocepção,isometria,amplitude,cadência,séries,repetições,descanso,progresso,consistência,recuperação-ativa,
hidratação,aquecimento-articular"""

def remover_acentos(texto):
    # Normaliza para NFD e remove acentos
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sem_acento = "".join(c for c in texto_normalizado if unicodedata.category(c) != "Mn")
    return texto_sem_acento

# Lê como texto e divide manualmente
palavras = [p.strip() for p in palavras_csv.replace("\n", "").split(",") if p.strip()]

# Transforma em DataFrame
df = pd.DataFrame(palavras, columns=["palavra"])
# Sample para sorteio
palavra_aleatoria = df.sample().values[0][0]
#print("Palavra sorteada:", palavra_aleatoria)
palavra_aleatoria = remover_acentos(palavra_aleatoria).upper()

def jogo(palavra_magica):

    # CRIA OS CONJUNTOS
    conjunto_letras_palavra = set(palavra_magica)
    conjunto_letras_digitadas = set()


    tentativas = 6


    print('----------INICIO DO JOGO-------------')
    print('-------------------------------------')

    while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas):
        achou = False
        for letra in palavra_magica:
            print(f'_ ', end='')
        #print(conjunto_letras_palavra)
        letra_digitada = input('\nDigite uma letra:::  ').upper()

        conjunto_letras_digitadas.add(letra_digitada)
        #print(conjunto_letras_palavra)
        if letra_digitada in conjunto_letras_palavra:
            print('A palavra é: ',end='')
            for letra in palavra_magica:
                # print(letra,letra_digitada)
                if letra in conjunto_letras_digitadas:
                    print(f'{letra} ', end='')
                    achou = True
                else:
                    print('_ ', end='')
        else:
            tentativas -= 1
            print(f'xxxxxxxxx PERDEU 1 TENTATIVA! RESTAM {tentativas} xxxxxxxxx')

        if achou == True:
            print('\nACERTOU!  ', end='')
        print('\nLETRAS JÁ DIGITADAS: ', conjunto_letras_digitadas)
        if tentativas <= 0:
            print('--------- GAME OVER! VOCÊ PERDEU! ---------')
            break




jogo(palavra_aleatoria)
