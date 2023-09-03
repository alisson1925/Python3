print('PROMOÇÃO, SALSICHA COM 5% DE DESCONTO!!!\n')
produto = eval(input('Valor do produto: '))
desconto = (produto * 5) / 100
Pf = produto - desconto
print('O desconto é de: R${}'.format(desconto))
print('O valor do produto é: R${:.2f}'.format(Pf))
