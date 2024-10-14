s = 0
b = int(input('Digite até que número você deseja: '))
for c in range(1,b+1):
    if c % 2 == 0:
        s += c
print('A soma dos números pares entre 1 e {}, é: {}'.format(b,s))