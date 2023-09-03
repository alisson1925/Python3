def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumento(n=0):
    return n + (n * 10/100)


def reduzido(n=0):
    return n - (n * 13/100)
