class Alarme:
    
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        if(isinstance(valor, bool)):
            self.__estado = valor
        else:
            print('Valor não é um booleano')



al = Alarme(True)
print(al.get_estado())
al.set_estado(False)
print(al.get_estado())
al.set_estado('local')
