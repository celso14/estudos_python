class Elevador:

    def __init__(self, andares) -> None:
        self.__andares=andares
        self.__andar=1
    
    def locomover(self, andar_final):
        if(andar_final < 1 or andar_final > self.__andares):
            return self.__msg_error()
        else:
            return self.__msg_alteracao_andar_info(andar_final)

    def __msg_alteracao_andar_info(self, andar_final):
        self.__andar=andar_final
        if(andar_final ==1):
            return self.__msg_elevador_ao_terreo()
        return self.__msg_elevador_para_andar()

    def __msg_error(self):
        return f'Andar incorreto! Elevador no {self.__andar}º andar'

    def __msg_elevador_ao_terreo(self):
        return f'Elevador indo para o térreo'

    def __msg_elevador_para_andar(self):
        return f'Elevador indo para o {self.__andar}º andar'