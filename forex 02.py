
seq = int(input('Digite até que número irá a sequência: '))
print("Padrão Numérico, goddamit!")
for i in range(1, seq + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")
