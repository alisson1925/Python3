from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga uma valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print('--' * 26)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('--' * 26)
    if tipo == 'P':
        if total % 2 == 0:
            cont += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            cont += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente.')
    print('=-' * 15)
print('=-' * 16)
print(f'GAMER OVER! Você venceu {cont} vezes.')

