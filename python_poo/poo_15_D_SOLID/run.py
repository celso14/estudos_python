from typing import Type
from db.mongo_repo import MongoDB
from db.mysql_repo import MySqlRepo
from db.interface_repo import Repositorio

#Fazer o Usuario não depender diretamente da mysqlrepo
#Fazer uma interface repositorio e associar ela aos outros como o Mysql ou Mongo

class User:

    def __init__(self, repo: Type[Repositorio]) -> None:
        self.__repo = repo

    def armazenar_dado(self, dado:any):
        self.__repo.inserir(dado)

    def remover_dado(self, dado:any):
        self.__repo.deletar(dado)




user = User(MySqlRepo())
user.armazenar_dado(23)

user = User(MongoDB())
user.armazenar_dado(23)