lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-' * 30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print(f'FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Nota de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

