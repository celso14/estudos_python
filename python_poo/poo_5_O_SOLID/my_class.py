#Entradas diferentes, geram ações diferentes -> principio aberto/fechado
#Existe um erro nesse código abaixo, foi assim que surgiu o conceito de herança e interfaces

class Circo:

    def apresentar(self, tipo: any):
        tipo.apresentar_show()

class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentado seu show!')


class Palhaco:
    
    def apresentar_show(self):
        print('Palhaço apresentando seu show!')



circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)