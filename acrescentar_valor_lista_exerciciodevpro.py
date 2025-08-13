#AUla 06 - Como Acrescentar Valores em uma lista(vetor) em Python - Desafio DevPro

#EX-01  : FAÇA UM PROGRAMA QUE LEIA UM VETOR DE 5 NUMEROS INTEIROS E MOSTRE-OS

#Definir lista
exerciciouno= [1,2,3,4,5]
#print(exerciciouno)

def ler_vetor(exerciciouno):
    print(exerciciouno)

def armazena_novoelemento(lista,elemento):
    lista.append(elemento)
    
#EX-02  : FAÇA UM PROGRAMA QUE LEIA UM VETOR DE 10 NUMEROS REAIS E MOSTRE-OS NA ORDEM INVERSA

# Usando FOR manualmente
def ordem_inversa(exercicioduo):
    listainversa = []
    for i in range(len(exercicioduo)-1,-1,-1):
        listainversa.append(exercicioduo[i])
        print(listainversa)
    print(f'Lista INVERSA DO USUARIO! {listainversa}')
    return listainversa
    
# Usando Reverse
def ordem_inversa_reverse(exercicioduo):
    listainversa = list(reversed(exercicioduo))
    print(f'Lista INVERSA DO USUARIO! {listareversa}')
    return listareversa

# Chama Função pra ler a lista
ler_vetor(exerciciouno)
# Pergunta sobre novo elemento
pergunta = int(input('Entre com um Elemento!'))
# Chama Função para inserir elemento
armazena_novoelemento(exerciciouno,pergunta)
# Chama Função pra ler a lista
ler_vetor(exerciciouno)

# Cria uma lista dentro da lista
listadentro =  ['Agua','Terra','Coracao']
armazena_novoelemento(exerciciouno,listadentro)
# Chama Função pra ler a lista
ler_vetor(exerciciouno)

#Pergunta ao usuário NUMEROS
print('LISTA DO USUARIO')
listausuario = []
for _ in range(5):
    numero = float(input('Digite um Numero!'))
    listausuario.append(numero)
print(listausuario)

#Inverte Lista do Usuario
ordem_inversa(listausuario)
    
