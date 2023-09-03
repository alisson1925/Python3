from time import sleep
from datetime import date
atual = date.today().year
nc = int(input('Sua data de Nascimento: '))
soma = atual - nc
print('PROCESSANDO!!!\n')
(sleep(3))
print('Você tem {} anos!'.format(soma))

if soma == 18:
    print('Você precisa se alistar IMEDIATAMENTE.')
elif soma < 18:
    idade = 18 - soma
    atual = atual + idade
    print('Faltam {} anos para você se alistar ao serviço militar. Será em {}'.format(idade, atual))
else:
    idade = soma - 18
    atual = atual - idade
    print('Já passou {} anos do alistamento. Foi em {} ano'.format(idade, atual))
