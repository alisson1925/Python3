from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema.'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçaljo(f'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçaljo(f'Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite um opção válida!\033[m')
    sleep(2)

