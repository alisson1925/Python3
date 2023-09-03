lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = par = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor [{l}, {c}]'))
print(f'=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
print(f'=-' * 15)
print(f'A soma dos valores pares: {par}.')
for l in range(0, 3):
    soma += lista[l][2]
print(f'A soma dos valores da terceira colunoa é: {soma}.')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior da segunda linha é: {maior}')

