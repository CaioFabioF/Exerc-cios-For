frase = str(input('Digite a sua frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = junto[::-1]
if inverso == junto :
    print('Palíndromo encontrado!, dammit!')
else:
    print('Não é um palíndromo')
print('O inverso de {} é {}'.format(junto,inverso))