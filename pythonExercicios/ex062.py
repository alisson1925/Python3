print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Priemiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        cont += 1
        termo += razao
        print('{} > '.format(termo), end='')
    print('PAUSA!')
    mais = int(input('Quanto você deseja agora? '))
print('FIM!')

