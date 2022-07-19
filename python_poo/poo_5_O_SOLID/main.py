from exercicio import Repositorio
from repositorios import PostgresDB, MysqlDB

db_conn_postgres = PostgresDB()
db_conn_mysql = MysqlDB()
repo = Repositorio()

repo.insert(db_conn_mysql)
print()
repo.select(db_conn_postgres)