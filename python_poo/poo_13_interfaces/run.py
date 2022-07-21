from terreno.quadrado import TerrenoQuadrado
from terreno.retangular import TerrenoRetangular
from engenheiro import Engenheiro


engenheiro = Engenheiro('Celso')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoretangular = TerrenoRetangular(2,3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_area(terrenoQuadrado)



engenheiro.medir_perimetro(terrenoretangular)