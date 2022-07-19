from typing import Type

class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.__comodo=comodo

    
    def acender(self):
        print(f'Acendendo {self.__comodo}')

    def apagar(self):
        print(f'Apagando {self.__comodo}')



class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]): #notando que o objeto interruptor vai ser do tipo Interruptor(classe)
        interruptor.acender()
    
    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Zzz')




lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_cozinha = Interruptor('cozinha')

interruptor_quarto.acender()
lhama.acender_luz(interruptor_quarto)
lhama.acender_luz(interruptor_cozinha)