dados = {}
partidas = []
dados['nome'] = str(input(f'Nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na {c}º partida? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(dados['gols'])
print(f'-=' * 30)
print(dados)
print(f'-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(partidas)}')
for p, g in enumerate(dados['gols']):
    print(f'    => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')
