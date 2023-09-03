numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Número adicionado com sucesso...')
    else:
        print(f'Número duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
numeros.sort()
print(f'Os números adicionados foram: {numeros}')
