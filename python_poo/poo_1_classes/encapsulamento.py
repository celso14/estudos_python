class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf


    def correr(self):
        print('Correndo...')

    def beber(self, bebida):
        if(bebida == 'cerveja'):
            self.__apresentar_documento()
        else:
            print('bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', '8899877', 32)




class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__add(num1, num2)
        elif op == '-':
            return self.__sub(num1, num2)
        else:
            print('Operação inválida')

    def __add(self, num1, num2):
        return num1 + num2

    def __sub(self, num1, num2):
        return num1 - num2


calculadora = Calculadora()
resultado = calculadora.calcular('+', 3, 2)
print(resultado)