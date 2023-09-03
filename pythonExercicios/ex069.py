print('--' * 15)
print('     CADASTRE UMA PESSOA     ')
print('--' * 15)
total = m = f20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        total += 1
    if sexo == 'F' and idade < 20:
        f20 += 1
    if sexo == 'M':
        m += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'Total de pessoa com mais de 18 anos: {total}')
print(f'Ao todo temos {m} homens cadastrados')
print(f'E temos {f20} mulheres com menos de 20 anos.')
