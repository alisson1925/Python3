num = int(input('Digite um número de 0 a 9999: '))
print('Analisando o número {}'.format(num))

#Usei o sinal da matematica; divisão com o resto da divisão. 1 % 10
u = num // 1 % 10
print('unidades: {}'.format(u))

#Usei o sinal da matematica; divisão com o resto da divisão. 10 % 10 = num // 10 % 10
print('dezenas: {}'.format(d))

#Usei o sinal da matematica; divisão com o resto da divisão. 100 % 10
c = num // 100 % 10
print('centenas: {}'.format(c))

#Usei o sinal da matematica; divisão com o resto da divisão. 1000 % 10
m = num // 1000 % 10
print('milhares: {}'.format(m))