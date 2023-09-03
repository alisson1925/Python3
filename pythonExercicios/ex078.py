valores = []
for n in range(1, 6):
    num = valores.append(int(input(f'Digite um valor na Posição {n}: ')))
print('=-' * 15)
print(valores)
print(f'O maior número foi {max(valores)} e está na Posição ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c + 1}...', end='')
print()
print(f'O menor número foi {min(valores)} e está na Posição ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c + 1}...', end='')
print('\nFIM!!!')
