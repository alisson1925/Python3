numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    stop = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stop == 'N':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'=-' * 30)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')

