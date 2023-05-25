from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Categoria]:
        categorias = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM categorias")
        resultados = cursor.fetchall()

        for result in resultados:
            cat = Categoria(result[1])
            cat.id = result[0]
            categorias.append(cat)

        cursor.close()
        conexao.close()

        return categorias


    def adicionar(self, categoria: Categoria) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO categorias (nome) VALUES (%(nome)s)
           """,
        ({'nome': categoria.nome, }))
        conexao.commit()
        cursor.close()
        conexao.close()
        #self.__categorias.append(categoria)


    def remover(self, categoria_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM categorias WHERE id = %s", (categoria_id,))
        
        categorias_removidas = cursor.rowcount

        conexao.commit()
        cursor.close()
        conexao.close()

        if (categorias_removidas == 0):
            return False
        return True
        
    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM categorias where id = %s", (categoria_id,))
        resultado = cursor.fetchone()
        if (resultado):
            cat = Categoria(resultado[1])
            cat.id = resultado[0]
        cursor.close()
        conexao.close()
        return cat
