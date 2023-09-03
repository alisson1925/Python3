from time import sleep


def linha():
    print(f'-=' * 20)
    print(f'Analisando os valores passados...')


def valores(*num):
    cont = maior = 0
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
linha()
valores(2, 9, 4, 5, 7, 1)
linha()
valores(4, 7, 0)
linha()
valores(1, 2)
linha()
valores(6)
linha()
valores()





