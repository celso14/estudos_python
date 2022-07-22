from abc import ABC, abstractclassmethod

class Repositorio(ABC):

    @abstractclassmethod
    def inserir(self, dado):
        raise 'Deveria ter um método aqui'

    @abstractclassmethod
    def deletar(self, dado):
        raise 'Deveria ter um método aqui'