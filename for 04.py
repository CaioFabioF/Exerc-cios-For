a = int(input('Digite o número a ser tabuado: '))
b = int(input('Digite até que número ele será tabuado: '))
for c in range(0,b+1) :
    t = c * a
    print('{} multiplicado por {:2} é {}'.format(a,c,t))
