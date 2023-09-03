while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num <= -1:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 30)
print('ACABOU!!!')

