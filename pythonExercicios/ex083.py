exp = str(input('Digite a expressão: '))
lista = []
for p in exp:
    if p == '(':
        lista.append('(')
    elif p == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print(f'Sua expressão está correta!')
else:
    print(f'Sua expressão está incorreta!')

