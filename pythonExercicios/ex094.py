pessoas = []
dados = {}
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print(f'ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'[{p["nome"]}] ', end='')
print()
print(f'D) lista das pessoas que estão acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= media:
        print(f'     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print(f'<< ENCERRADO >>')
