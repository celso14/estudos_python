from produtos import Produto
from typing import Type

class Carrinho:

    def __init__(self) -> None:
        self.__produtos = []
    
    def add_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)
    
    def finalizar_compra(self):
        print('Compras Finalizadas')

        for produto in self.__produtos:
            produto.informacoes_produto()

