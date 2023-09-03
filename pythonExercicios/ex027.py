nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome: {}'.format(nome))
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
#(n[len(n) - 1])
#Primeiro: "N" vai seprar as palavras por causa do split.
#Segundo: "LEN" vai contar os caractéres dentro do split Colocando o "N" de novo para continuar com as palavras separadas.
#Terceiro: " - 1 " vai tirar toda a palavra menos a ULTIMA, sem ela o programa vai dar erro.
print('Seu ultimo nome é: {}'.format(n[len(n) - 1]))