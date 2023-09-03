nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')

#Tudo em letras maiusculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

#Tudo em letra minusculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

#Tirando todos os espaços / O 'count' conta as letras, portanto, usamos o MENOS ' - ' para tira a letra que ele contou
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#Contando a primeira palavra usando o 'find'; mas tem que usar o ESPAÇO dentro dos parenteces, se não, não funciona.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Ou pode usar o fatiamento com 'split'
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))