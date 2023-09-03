print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(decimo), end='')
    decimo += razao
    cont += 1
print('ACABOU!!!')

