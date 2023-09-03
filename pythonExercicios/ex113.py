def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[0;31m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro foi {n1} e o real foi {n2}')

