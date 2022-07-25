from livro import Livro
from typing import Type

class Biblioteca:

    def __init__(self) -> None:
        self.__lista=[]
    
    def add_livro(self, livro: Type[Livro]):
        self.__lista.append(livro)
        print('Livro Adcionado')
    
    def tabela_livros(self):
        for livro  in self.__lista:
            print(livro.livro_info())
