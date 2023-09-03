listanum = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        listanum[0].append(valor)
    else:
        listanum[1].append(valor)
listanum[0].sort()
listanum[1].sort()
print(f'=-' * 10)
print(f'Os números são: {listanum}')
print(f'Os números pares são: {listanum[0]}')
print(f'Os númeroes ímpares são: {listanum[1]}')
