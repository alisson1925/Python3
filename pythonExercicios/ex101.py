def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18 or idade < 65:
        return f'Com {idade} anos: VOTO OVRIGATÓRIO'


# Programa Principal
print(f'-' * 30)
nsc = int(input('Em que ano você nasceu? ')[0:4])
print(voto(nsc))
