# Exercico 04, baseado no video do Canal DevPro 'https://youtu.be/FhJlgfqBP28'

# Supondo que a população de um país "Avarelandia" seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% 
# e que a populaçao de "Arandur" seja de 200.000 com uma taxa de crescimento de 1.5%;
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B;
# Mantidas as taxas de crescimento.

#Tamanho das cidades 
avare =     80000
arandur =   200000
# Contador de Anos
ano = 0

#Cria-se o dicionario primordial, passando as chaves String avare e seu valor e arandur e seu valor.
pri_dic = { 'avare' : avare, 'arandur' : arandur}

#Para fins de visualização
print(pri_dic)

#Função para comparar duas cidades com seus crescimentos fixos de 3% e 1,5%, retornando um novo dicionario estabelecido com new_dic
def equiparando_cidades(ava,ara):
    new_avare = avare + avare * 0.03
    new_arandur = arandur + arandur *0.015
    new_dic = {
        'avare' : float(new_avare),
        'arandur' : float(new_arandur)
    }
#    print(new_dic)
    return(new_dic)

print('------INICIO DA CONTAGEM ---------')

#Iteração
while ano <= 200 and pri_dic['avare'] <= pri_dic['arandur']: 
    avare = pri_dic['avare']
    arandur = pri_dic['arandur']
    res_dic = equiparando_cidades(avare,arandur)
    print(f'Ano: {ano} ||| Dicionario: {pri_dic}')
    pri_dic.update(res_dic)
    ano = ano + 1
    #print(f'Ano: {ano} ||| Dicionario: {res_dic}')
    #print('---------------')
print(res_dic)

# Mudando de Float pra int
# Percorre o dicionario para cada chave, mudando o tipo de valor de float pra int
for chave in res_dic:
    res_dic[chave] = int(res_dic[chave])
    
# Print Final
print('==============FINAL=====================')
print(f'ano : {ano}, Dic: {str(res_dic)}')
