class Loja:

    tarifa: float = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(cls) -> float:
        return 40*cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: float) -> None:
        cls.tarifa = nova_tarifa



loja1 = Loja('matriz')
loja2 = Loja('filial')

loja1.apresentar_endereco()

print(loja1.vender())
print(loja2.vender())

loja1.alterar_tarifa(1.50)

print(loja1.vender())
print(loja2.vender())