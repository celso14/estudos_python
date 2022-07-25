class Elevador:

    def __init__(self, nome: str) -> None:
        self.__nome=nome
        self.__andar=1
    
    def set_andar_atual(self, andar_atual: int) -> None:
        self.__andar=andar_atual
    
    def get_andar_atual(self) -> int:
        return self.__andar

    def get_nome(self) -> str:
        return self.__nome
