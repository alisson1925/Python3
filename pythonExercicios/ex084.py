lista1 = []
lista2 = []
maior = menor = 0
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    if len(lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    stop = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if stop == 'N':
        break
print(f'Ao todo temos {len(lista2)} Cadastrado!')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in lista2:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in lista2:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()

