s = 0
ct = 0
for a in range(1,501):
    if a % 2 != 0 and a % 3 == 0:
        s += a
        ct += 1
print('A soma dos {} números primos divisíveis por 3 é: {}'.format(ct,s))
