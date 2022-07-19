class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('comendo')

    def estudar(self) -> None:
        print('Estou Estudando')


class Filha(Mae): ## Entre o parênteses é a classe de qual a classe atual está herdando

    def __init__(self) -> None:
        super().__init__('Rua do bolo') 


clara = Filha()
clara.estudar()
print(clara.endereco)