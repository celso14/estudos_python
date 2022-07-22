from produtos import Produto
from carrinho import Carrinho


car = Carrinho()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)
tv = Produto('TV', 5000)

car.add_produto(monitor)
car.add_produto(tv)
car.add_produto(cerveja)
car.finalizar_compra()