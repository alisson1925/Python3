peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc), end='')

if imc < 18.5:
    print('\033[1;31m Abaixo do Peso\033[m')
elif imc <= 25:
    print('\033[1;31m Peso Ideal\033[m')
elif imc <= 30:
    print('\033[1;31m Sobrepeso\033[m')
elif imc <= 40:
    print('\033[1;31m Obesidade\033[m')
else:
    print('\033[1;31m Obesidade Mórbida\033[m')