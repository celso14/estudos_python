class PessoaA:

    def se_apresentar(self):
        print('Ola, sou a pessoa A')


class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print('Ola, Sou a pessoa B')


class PessoaC(PessoaB):

    def __init__(self) -> None:
        super().__init__()
    
## QUANDO SE ALTERA UM COMPORTAMENTO, EM UM CLASSE, ESSE COMPORTAMENTO É PROPAGADO NAS PRÓXIMAS CLASSES


pessoa =  PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()

