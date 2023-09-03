print('-' * 28)
print('     LOJA SUPER BARATÃO     ')
print('-' * 28)
total = maior = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    if preço >= 1000:
        maior += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')


