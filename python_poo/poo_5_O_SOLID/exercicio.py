from django.db import connection


class Repositorio:

    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f'conectei ao banco {connection}')
        print(f'fazendo um Select * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print(f'conectei ao banco {connection}')
        print(f'fazendo um Insert Values...')
        db_connection.desconectar()