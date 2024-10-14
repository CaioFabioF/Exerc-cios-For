from datetime import datetime
hj = datetime.now().year
s = 0
f = 0
for c in range(0,7):
    a = int(input('Digite o seu ano de nacimento: '))
    id = hj - a
    if id >= 18 :
        print('Você é de maior')
        s += 1
    else:
        print('Você é de menor')
        f += 1

print('O número de pessoas maiores de idade é {}, e menores de idade é {}'.format(s,f))