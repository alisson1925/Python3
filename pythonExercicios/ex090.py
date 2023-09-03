alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'APROVADO!'
elif alunos['media'] >= 5:
    alunos['situacao'] = 'RECUPERAÇÂO!'
elif alunos['media'] < 5:
    alunos['situacao'] = 'REPROVADO!'
print(f'-=' * 20)
for k, v in alunos.items():
    print(f'   -  {k} é igual a {v}')
