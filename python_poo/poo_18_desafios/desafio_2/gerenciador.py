from elevador import Elevador
from typing import Type

class Gerenciador:
    def __init__(self, andares: int) -> None:
        self.__andares=andares

    def locomover(self, elevador: Type[Elevador], andar_final: int) -> str:
        if(andar_final < 1 or andar_final > self.__andares):
            return self.__msg_error(elevador)
        else:
            return self.__msg_alteracao_andar_info(elevador, andar_final)

    def __msg_alteracao_andar_info(self, elevador: Type[Elevador], andar_final) -> str:
        elevador.set_andar_atual(andar_final)
        if(andar_final ==1):
            return self.__msg_elevador_ao_terreo(elevador)
        return self.__msg_elevador_para_andar(elevador)

    def __msg_error(self, elevador: Type[Elevador]) -> str:
        return f'Andar incorreto! {elevador.get_nome()} no {elevador.get_andar_atual()}º andar'

    def __msg_elevador_ao_terreo(self, elevador: Type[Elevador]) -> str:
        return f'{elevador.get_nome()} indo para o térreo'

    def __msg_elevador_para_andar(self, elevador: Type[Elevador]) -> str:
        return f'{elevador.get_nome()} indo para o {elevador.get_andar_atual()}º andar'