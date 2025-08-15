### DICIONARIOS
# COnjunto naoordenado de pares - CHAVE : VALOR 
# Delimitado por chaves

pessoa = {'nome':'Alfonso', 'idade':40}
print(pessoa)
elementos = dict(nome='agua', forca = 30)
print(elementos)
pessoa['telefone'] = '2222-2343'
print(pessoa)

print('\n------------------------------------')

# Acessando valor
print(pessoa['nome'])
print(pessoa['idade'])

# DICIONARIOS ANINHADOS

contatos ={
    'uno': {'nome':'UM','tel':'11141'},
    'duo': {'nome':'DOIS','tel':'11211'},
    'tre': {'nome':'TRES','tel':'11131'},
    'cat': {'nome':'QUATRO','tel':'115511','extra':{'ALFA':'EEEEEXTRA'}},
}

print(contatos['uno']['tel'])
print(contatos['cat']['extra']['ALFA'])

print('\n------------------------------------')

# ITERAR DICIONARIOS
# mais comum usando for

for chave in contatos:
    print(chave, contatos[chave])
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

for chave, valor in contatos.items():
    print(chave, valor)
print('\n------------------------------------')

# dicionario nao permite que você duplique chaves
#
#
############# METODOS
#
# CLEAR - apaga
contatosapaga = contatos
print(contatosapaga)
contatosapaga.clear()
print(contatosapaga)
print('\n------------------------------------')

#
# COPY
contatos ={
    'uno': {'nome':'UM','tel':'11141'},
    'duo': {'nome':'DOIS','tel':'11211'},
    'tre': {'nome':'TRES','tel':'11131'},
    'cat': {'nome':'QUATRO','tel':'115511','extra':{'ALFA':'EEEEEXTRA'}},
}

contatosapaga = contatos.copy()
print(contatosapaga)
print('\n------------------------------------')

# FROMKEYS  - Cria as chaves para você

eee =dict.fromkeys(['nome','tel'])
print(eee)
eee =dict.fromkeys(['end','col'],'Placeholder')
print(eee)

print('\n------------------------------------')

# GET  - Acessa info no dicionario

xxx = {
    'emaildocara': {'nome': 'Nominho', 'tel':'Brastemp'}
}
print(xxx)
chave = xxx.get('chave') # Procura uma chave que nao existe, retornando none
print(chave)
chave = xxx.get('chave',{})  # Procura uma chave que nao existe, retornando dicionario vazio{ }}
print(chave)
chave = xxx.get('emaildocara',{})
print(chave)

print('\n------------------------------------')

# ITEMS

xxx = {
    'emaildocara': {'nome': 'Nominho', 'tel':'Brastemp'}
}
chave = xxx.items()
print(chave)
print('\n------------------------------------')

# KEYS 
xxx = {
    'emaildocara': {'nome': 'Nominho', 'tel':'Brastemp'}
}
chave = xxx.keys()
print(chave)
print('\n------------------------------------')

### POP

