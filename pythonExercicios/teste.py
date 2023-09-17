# vamos criar uma classe para Clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception(f'Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print(f'Plano Inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver Filme {filme}')
        elif self.plano == 'basic':
            print(f'Faça Upgrade para premium para ver esse filme')
        else:
            print(f'Plano Inválido')



cliente = Cliente('Lira', 'lira@gmail.com', 'basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')

# no botão de uppgrade
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')

