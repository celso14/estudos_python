class MinhaClasse:
    def __init__(self, att):  # metodo construtor
        self.atributo1 = 'olá mundo'
        self.atributo2 = att

    def meu_metodo(self):  # self se referencia a classe que ele tá identado
        print('Estou no metodo')

    def meu_metodo2(self, num, mult):
        return num * mult


objeto = MinhaClasse('hello world')
objeto.meu_metodo()
print(objeto.meu_metodo2(3, 2))
print(objeto.atributo1)
print(objeto.atributo2)
