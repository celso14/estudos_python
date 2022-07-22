from .interface_repo import Repositorio

class MongoDB(Repositorio):

    def inserir(self, dado):
        print(f'Inserindo {dado} no MongoDB')

    def deletar(self, dado):
        print(f'Deletando {dado} no MongoDB')