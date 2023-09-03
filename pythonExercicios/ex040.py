nome = str(input('Nome do Aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('O aluno {} ficou com a média de {:.1f}'.format(nome, media))

if media >= 7.0:
    print('APROVADO!!!')
elif media >= 5.0:
    print('RECUPERAÇÂO!!!')
else:
    print('REPROVADO!!!')
'''
if media < 5.0:
    print('REPROVADO!!!')
elif media < 7.0:
    print('RECUPERAÇÂO!!!')
else:
    print('APROVADO!!!')
'''
