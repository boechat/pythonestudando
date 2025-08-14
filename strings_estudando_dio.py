### Dominando Strings 

curso = '   PytGThon|  '

print(curso.lower())
print(curso.title())
print(curso.upper())
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
curso = "Python"
print(curso.center(20, "#"))
print('.'.join(curso))

print('----------------------------------')
################ OLD STYLE  % - Interpolação
nome = 'Andre'
idade = 200
profissao = 'Cozinheiro'
linguagem = 'humana'

print('Oi, eu sou %s, tenho %d anos, trabalho com %s e minha lingua é %s' % (nome, idade, profissao, linguagem))

################ METODO FORMAT {} - Interpolação
print('Oi, eu sou {}, tenho {} anos, trabalho com {} e minha lingua é {}'.format(nome, idade, profissao, linguagem))

############### formatar strings com f-string

PI = 3.14949394039403903
print(f'Valor de PI: {PI: .2f}')
print(f'Valor de PI: {PI: 10.2f}')


####### FATIAMENTO
print('----------------------------------')
nome = 'Olaria do Vasco da Gama '
print(nome[0])
print(nome[:9])
print(nome[9:])
print(nome[4:9])
print(nome[2:12:1])
print(nome[:])
print(nome[::-1])

####### STRINGS DE MULTIPLAS LINHAS 
print('----------------------------------')

name = 'Andre'
msg = f'''oi 
meu nome 
é {name}
'''

print(msg)
