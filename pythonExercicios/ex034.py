salario = float(input('Valor do salário: '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Seu salário era de R${:.2f} agora voce passa a ganhar R${:.2f}'.format(salario, aumento))