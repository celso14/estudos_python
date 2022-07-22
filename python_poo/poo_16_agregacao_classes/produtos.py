class Produto:

    def __init__(self, prod_nome: str, prod_valor: float) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor

    def informacoes_produto(self):
        print(f'Produto: {self.__prod_nome} / valor: R$ {self.__prod_valor}')
