from random import randint
from time import sleep
print('-=' * 25)
print('     TENTA ADIVINHAR O MESMO NÚMERO QUE EU!     ')
print('-=' * 25)
comp = randint(0, 5)
jg = 0
cont = 0
while jg != comp:
    jg = int(input('O número que você pensou foi: '))
    cont += 1
    print('-=' * 12)
    print('     PROCESSANDO!!!    ')
    print('-=' * 12)
    sleep(1)
    if jg == comp:
        jg = comp
    else:
        if jg < comp:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print('Acertou com {} Tentativas. PARABÉNS!'.format(cont))

