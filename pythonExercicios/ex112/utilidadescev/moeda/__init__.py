def moeda(n=0, moeda='R$', formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: Representa a ligação de outro paramentro (p).
    :param taxa: qual é a porcentagem do aumento.
    :param moeda: Representa o formato da moeda.
    :param formato: Mostrar o formato da moeda. True 'Mostra' Flase 'Não mostra'.
    :return: Sim! Retornando o valor.
    """
    res = f'{moeda}{n:>.2f}'.replace('.', ',')
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumento(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def reduzido(n=0, taxa=0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def resumo(n=0, taxaa=10, taxar=5):
    print(f'-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(n, taxaa, True)}')
    print(f'{taxar}% de redução: \t{reduzido(n, taxar, True)}')
    print(f'-' * 30)
