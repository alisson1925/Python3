from datetime import date
atual = date.today().year
nome = str(input('Nome do Atleta: '))
nc = int(input('Data de Nascimento: '))
idade = atual - nc
print('O alteta tem {} anos!'.format(idade))

if idade <= 9:
    print('O atleta {} é da categoria:\033[1;36m MIRIM \033[m'.format(nome))
elif idade <= 14:
    print('O atleta {} é da categoria:\033[1;33m INFANTIL \033[1;32m'.format(nome))
elif idade <= 19:
    print('O atleta {} é da categoria:\033[1;34m JUNIOR \033[m'.format(nome))
elif idade <= 25:
    print('O atleta {} é da categoria:\033[1;32m SÊNIOR \033[m'.format(nome))
else:
    print('O atleta {} é da categoria:\033[1;31m MASTER \033[m'.format(nome))
