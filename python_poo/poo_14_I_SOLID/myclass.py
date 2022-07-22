from abc import ABC, abstractmethod

#Evitar depender de elementos que não são utilizados

class AveVoadora(ABC): # especificar mais a classe para não haver problemas -> Pinguin não voa

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'

    

class AveQueNaoVoa(ABC): # especificar mais a classe para não haver problemas -> Pinguin não voa

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'