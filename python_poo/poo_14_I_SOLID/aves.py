from myclass import AveVoadora, AveQueNaoVoa


class Canario(AveVoadora):

    def comer(self):
        print('comendo...')
    
    def voar(self):
        print('voando...')

    def gritar(self):
        print('Gritando...')



class Pinguin(AveQueNaoVoa):

    def comer(self):
        print('comendo...')
    
    def gritar(self):
        print('Gritando...')


