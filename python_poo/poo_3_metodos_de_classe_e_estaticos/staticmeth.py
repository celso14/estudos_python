class MinhaClasse:
     
    def __init__(self, estado: bool) -> None:
          self.estado = estado

    @staticmethod #é atribuito um contexto único para esse tipo de comportamento -> se utiliza como especificador
    def metodo_estatico() -> None:
        print('Static method')


obj = MinhaClasse(True)
obj.metodo_estatico()
MinhaClasse.metodo_estatico()


#EXEMPLO


class Error:

    @staticmethod
    def erro_protoclo() -> None:
        print('Protocolo apresenta error')

    @staticmethod
    def erro_entrada() -> None:
        print('Parâmetros inválidos')

    