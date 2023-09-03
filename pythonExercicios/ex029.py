velocidade = float(input('Qual é a velocidade do carro? '))

if velocidade > 120:
    multa3 = (velocidade - 80) * 20
    print('MULTADO! Você foi multado por altas velocidades')
    print('Você foi multado no valor de R${:.2f}'.format(multa3))

elif velocidade > 100:
    multa2 = (velocidade - 80) * 10
    print('MULTADO! Você passou de 100km/h')
    print('Você foi multado no valor de R${:.2f}'.format(multa2))

elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o lime permitido que é de 80km/h')
    print('Você foi multado no valor de R${:.2f}'.format(multa))

print('BOM DIA! DIRIJA COM SEGURANÇA!')