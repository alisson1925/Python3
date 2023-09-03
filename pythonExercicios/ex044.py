print('========== LOJA AMERICANAS ==========')
produto = float(input('Qual é o valor do produto? R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] À Vista dinheiro / Cheque
[ 2 ] À Vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    valor = produto - (produto * 10 /100)
    print('Você obteve 10% de desconto.')
elif opção == 2:
    valor = produto - (produto * 5 / 100)
    print('Você obteve 5% de desconto.')
elif opção == 3:
    valor = produto
    parcelas = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcelas))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = produto + (produto * 20 / 100)
    valor1 = valor / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com Juros'.format(parcelas, valor1))
else:
    valor = 0
    print('Opção Inválida! Tente novamente!')

print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(produto, valor))
