dias = eval(input('Quantos dias alugado: '))
Km = eval(input('Quantos Km rodados: '))
soma = (dias * 60) + (Km * 0.15)
print('Você pagarar R${:.2f}'.format(soma))