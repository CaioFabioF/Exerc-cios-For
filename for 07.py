a = int(input('Digite um número: '))
tdiv = 0
for c in range(1,a+1) :
    if a % c == 0 :
        tdiv += 1
if tdiv == 2:
     print('Primo')
else :
    print('Não primo')
