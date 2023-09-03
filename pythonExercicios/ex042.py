print('-=' * 20)
print('Analisandor de Triangulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem formar um TRIÂNGULO', end='')
    if r1 == r2 == r3:
        print('\033[1;31m EQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;31m ESCALENO\033[m')
    else:
        print('\033[1;31m ISÔSCELES\033[m')

else:
    print('Os segmentos acima NÂO PODEM FORMA TRIÂNGULO!!!')