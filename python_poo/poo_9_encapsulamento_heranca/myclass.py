class DataBaseConn:
    
    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string' ##Dentro do python a notação protected é apenas uma convenção, acordo de cavalheiros, para não acessar o atributo pelo objeto
        self.user = 'Celso'

    def get_database(self) -> None:
        print(self.__database)
    
    def _testing_conection(self) -> None:
        print('Connection Ok!')
    

class Repository(DataBaseConn):
    
    def __init__(self) -> None:
        super().__init__()
    
    def select(self) -> None:
        self._testing_conection()
        print(f'Connecting to {self._conn}')
        print('SELECT * From table')



db = DataBaseConn()
print(db.user)
print(db._conn)
db._testing_conection()


repo = Repository()
print(repo.user)
repo.select()