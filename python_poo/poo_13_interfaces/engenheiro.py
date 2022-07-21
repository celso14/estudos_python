from interfaces.formas import FormasInterface
from typing import Type


class Engenheiro:

    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def medir_perimetro(self, terreno: Type[FormasInterface]) -> None:
        perimetro = terreno.get_perimetro()
        print(f'Perimetro Calculado pelo engenheiro {self.nome} é {perimetro}')
    
    def medir_area(self, terreno: Type[FormasInterface]) -> None:
        area = terreno.get_area()
        print(f'Área Calculado pelo engenheiro {self.nome} é {area}')
