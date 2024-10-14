a = int(input('Digite o termo incial: '))
r = int(input('Digite a razão: '))
d = a + (11-1) * r
for c in range(a,d,+r):
    print(c,end=' ⮕ ')
print('Fim')