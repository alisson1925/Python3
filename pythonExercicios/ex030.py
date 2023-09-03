num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é um número PAR'.format(num))
else:
    print('O número {} é um número IMPAR'.format(num))