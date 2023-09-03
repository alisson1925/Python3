from time import sleep
casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o valor do seu salário: R$'))
anos = int(input('Quantos anos financiamento? '))
soma = casa / (anos * 12)
minimo = salario * 30 / 100
print('PROCESSANDO!!!')
sleep(3)

print('Para comprar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(soma))
if soma <= minimo:
    print('PARABÉNS! Você pode comprar esta casa.')
else:
    print('DESCULPE! Você não pode comprar esta casa.')
