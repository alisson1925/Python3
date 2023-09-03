n1 = int(input('Digite um nuemro: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O \033[1;34mPrimeiro\033[m numero é MAIOR!')
elif n2 > n1:
    print('O \033[34mSegundo\033[m numero é MAIOR!')
else:
    print('Não exite numero maior, os \033[1;31mdois\033[m são IGUAIS[m!')
