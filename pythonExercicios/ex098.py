from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        contar = i
        while contar <= f:
            print(f'{contar} ', end='', flush=True)
            sleep(0.5)
            contar += p
        print(f'FIM')
    else:
        contar = i
        while contar >= f:
            print(f'{contar} ', end='', flush=True)
            sleep(0.5)
            contar -= p
        print(f'FIM')


# Programa Principal
cont(1, 10, 1)
cont(10, 0, 2)
print(f'-=' * 20)
print(f'Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
cont(ini, fim, pas)
