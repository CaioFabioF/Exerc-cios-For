s = 0
for c in range(0,6) :
    n = int(input('Digite um número par, para ser somado: '))
    if n % 2 == 0 :
        s +=n
    else:
        print('Número ímpar')
print('A soma de todos os números pares escolhidos foi: {}'.format(s))