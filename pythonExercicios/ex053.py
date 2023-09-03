nome = str(input('Digite seu nome: ')).strip().upper() #Tirando os espaços da laterais e colocando em maiúscula.
palavras = nome.split() #Separagem por grupos.
junto = ''.join(palavras) #unindo novamente as palavras tirando os espaços que ficam entre uma palavra e outra.
inverso = junto[::-1] #Mesma coisa do comentario abaixo, de uma forma mais simplificada.
print('Você digitou a frase {}'.format(junto))

'''inverso = ''
for letra in range(len(junto) -1, -1, -1): #O primeiro -1 é a onde começa. o outro -1 é a onde termina. o último -1 é a contagem,neste caso. de trás para frente
    inverso += junto[letra]'''

print(junto, inverso)
if inverso == junto:
    print('É UM PALINDROMO!')
else:
    print('NÂO É UM PALINDROMO!')
