sair = False
total = 0
cont = -1
while not sair:
    n = int(input('Digite um número [999 para parar]: '))
    total += n
    cont += 1
    if n == 999:
        total -= 999
        sair = True
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, total))

#    FORMA MAIS SIMPLIFICADA!!!

#   sair = cont = total = 0
#   sair = int(input('Digite um número [999 para parar: '))
#   while sair != 999:
#    cont += 1
#    total += sair
#    sair = int(input('Digite um número [999 para parar: '))
#   print('Você digitou {} números e a soma entre eles são {}.'.format(cont, total))

