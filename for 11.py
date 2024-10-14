si = 0
sm = 0
idades = []
maioridadeh = 0
nomemaiorh = 0
for c in range(1,5):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    idades.append(idade)
    sexo = str(input('Dige M para Masculino ou F para Feminino: '))
    if sexo == 'F':
        if idade >= 20 :
            sm += 1
    si += idade
    if c == 1 and sexo == 'M':
        maioridadeh = idade
        nomemaiorh = nome
    if sexo == 'M' and idade > maioridadeh :
        maioridadeh = idade
        nomemaiorh = nome
print('A média de idade foi {}'.format(si/c))
print('A maior idade foi {}'.format(max(idades)))
print('A quantidade de mulheres acima dos 20 anos foi {}'.format(sm))
print('O homem de maior idade é o {} e tem {} anos'.format(nomemaiorh,maioridadeh))