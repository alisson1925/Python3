from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
sair = False
while not sair:
    print('''
    [ 1 ] somar.
    [ 2 ] multiplicar.
    [ 3 ] maior.
    [ 4 ] novos valores.
    [ 5 ] sair do programa.
    ''')
    n3 = int(input('>>>>>Qual opção você deseja? '))
    if n3 == 5:
        sair = True
        print('FINALIZANDO...')
    else:
        if n3 == 1:
            print('A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
        elif n3 == 2:
            print('A multiplicação de {} x {} é {}'.format(n1, n2, n1 * n2))
        elif n3 == 3:
            if n1 > n2:
                print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
            elif n1 < n2:
                print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
            else:
                print('Não há número maior.')
        elif n3 == 4:
            print('Informe os números novamente: ')
            n1 = int(input('Primeiro Valor: '))
            n2 = int(input('Segundo Valor: '))
        else:
            print('Opção inválida. Tente novamente')
        print('=-=' * 10)
    sleep(2)
print('Fim do Programa! Volte Sempre!')
