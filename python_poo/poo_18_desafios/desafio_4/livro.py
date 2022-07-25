class Livro:
    
    def __init__(self, titulo:str, autor:str, ano:int, num_id:int) -> None:
        self.__titulo=titulo
        self.__autor=autor
        self.__ano=ano
        self.__num_id=num_id
    
    def livro_info(self) -> str:
        return f'{"="*20}\nTitulo: {self.__titulo} \nAutor: {self.__autor} \nAno: {self.__ano} \nID: {self.__num_id}\n{"="*20}'