lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    stop = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stop == 'N':
        break
lista.sort(reverse=True)
print('=-' * 30)
print(f'Você digitou {len(lista)} números.')
print(f'Os valores em ordem decrescente são: {lista}')

if 5 in lista:
    print(f'O valor 5 faz parta da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')

