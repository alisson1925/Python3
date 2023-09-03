distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

#forma simplificada:
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

#-------------------------------------------------------------------------------------
'''if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45'''
#-------------------------------------------------------------------------------------

print('Sua passagem custará R${:.2f}'.format(valor))