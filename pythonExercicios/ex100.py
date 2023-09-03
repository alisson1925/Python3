from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 números de 1 a 10. Os números sorteados foram: ', end='')
    for valor in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print(f'PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os números Pares de {lista}, temos: {soma} ', end='')
    print(f'PRONTO!')


numeros = []
sorteia(numeros)
somaPar(numeros)

