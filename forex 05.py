n = []
for c in range(1,6):
    num = int(input('Digite um número: '))
    if num % 5 == 0 and num < 150:
        n.append(num)
    if num > 500:
        break
print(n)