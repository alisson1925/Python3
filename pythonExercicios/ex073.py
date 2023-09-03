times = ('Botafogo', 'Gêmio', 'Flamengo', 'Palmeiras', 'São Paulo',
         'Fluminense', 'Bragatino', 'Athetico-PR', 'Fortaleza', 'Cruzairo',
         'Cuiabá', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos',
         'Bahia', 'Goiás', 'Coritiba', 'América-MG', 'Vasco da Gama')
print('-=' * 10)
cont = 0
for t in times:
    cont += 1
    print(f'{cont}ª Time: {t}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 ultimos colocados: {times[-4:]}')
print(f'Times em Alfabética: {sorted(times)}')
print(f'O Corinthians está em {times.index("Corinthians")} Lugar.')
