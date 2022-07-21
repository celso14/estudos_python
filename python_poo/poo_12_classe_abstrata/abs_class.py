from abc import ABC, abstractclassmethod

class AbstractClass(ABC):

    def __init__(self) -> None:
        self.atributo = 'Olá Mundo'
    
    def metodo(self, elemento):
        print(elemento)
    
    @abstractclassmethod
    def metodo_abstrato(self):
        pass
