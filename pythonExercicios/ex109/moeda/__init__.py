def moeda(n=0, moeda='R$', formato=False):
    """
    -> Mostrando os paramentros organizados e bem simplificado.
    :param n: Representa a ligação de outro paramentro (p).
    :param moeda: Representa o formato da moeda.
    :param formato: Mostrar o formato da moeda. True 'Mostra' Flase 'Não mostra'.
    :return: Sim. Retornando o valor.
    """
    res = f'{moeda}{n:>.2f}'.replace('.', ',')
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumento(n=0, formato=False):
    res = n + (n * 10/100)
    return res if formato is False else moeda(res)


def reduzido(n=0, formato=False):
    res = n - (n * 13/100)
    return res if formato is False else moeda(res)
