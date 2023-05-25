class Categoria:

    def __init__(self, nome: str): # alterado
        self.__id: int = 0 # alterado
        self.__nome: str = nome

    def __str__(self):
        return f'{self.__id} | {self.__nome}'

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome