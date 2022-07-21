class PessoaA:

    def se_apresentar(self):
        print('Olá, sou a pessoa A')

class pessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()
    
    def se_apresentar(self):
        print('Estou alterando esse método')



pessoa=PessoaA()
pessoa.se_apresentar()

pessoa2 = pessoaB()
pessoa2.se_apresentar()


#Ter cuidado ao quebrar o principio de liskov -> a herança deve ser uma complementação, não alterando os elementos a rodo
#Fazer a classe principal pai ser a mais genérica mais possível, e ir especificando