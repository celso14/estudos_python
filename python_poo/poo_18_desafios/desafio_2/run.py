from elevador import Elevador
from gerenciador import Gerenciador

rio_orange=Gerenciador(15)
elevador_1= Elevador('Elevador 1')
elevador_2= Elevador('Elevador 2')
resp = rio_orange.locomover(elevador_1, 3)
resp2 = rio_orange.locomover(elevador_2, 5)
print(resp)
print(resp2)
resp2 = rio_orange.locomover(elevador_2, 1)
print(resp2)
print(elevador_2.get_andar_atual())
print(elevador_1.get_andar_atual())