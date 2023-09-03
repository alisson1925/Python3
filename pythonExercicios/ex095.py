time = []
dados = {}
partidas = []
while True:
    dados.clear()
    dados['nome'] = str(input(f'Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c}º partida? ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(dados['gols'])
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'ERRO! Digite novamente com [S] ou [N]: ')
    if resp == 'N':
        break
print(f'-' * 40)
print(f'cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print(f'-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nâo existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez tantos {g} gols.')
        print(f'-' * 40)
print(f'<< VOLTE SEMPRE >>')


