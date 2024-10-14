a = int(input('Digite até que número irá a tabuada: '))
b = int(input('Digite o número a ser tabuado: '))
for c in range(0,a+1) :
    m = c * b
    print('{} x {} é ==> {}'.format(b,c,m))