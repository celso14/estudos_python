from livro import Livro
from biblioteca import Biblioteca

livraria = Biblioteca()
livro1 = Livro('js','celso',2022,1)
livro2 = Livro('java','celso',2020,2)
livro3 = Livro('python','celso',2019,3)

livraria.add_livro(livro1)
livraria.add_livro(livro2)
livraria.add_livro(livro3)

livraria.tabela_livros()