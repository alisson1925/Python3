def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área entre {l} x {c} é de {a}m².')

# Programa Principal
print(f' CONTROLE DE TERRENO ')
print(f'-' * 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
