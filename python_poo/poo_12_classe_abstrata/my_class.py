#uma classe abstrata não pode ser instanciada
#quando a classe tem um metodo abstrado, é necessário sempre implementar o metodo nas classes flihas

from abs_class import AbstractClass

class Filha(AbstractClass):

    def apresentar_metodo(self):
        print(self.atributo)
    
    def metodo_abstrato(self):
        print('metodo abstrato')
    

#Em python, para um classe ser abstrata ela precisa ter um metodo abstrato

filha = Filha()
filha.apresentar_metodo()
filha.metodo('here')

