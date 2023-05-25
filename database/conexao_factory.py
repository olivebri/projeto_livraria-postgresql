import psycopg2

class ConexaoFactory:

    def get_conexao(self):
         return psycopg2.connect(host="silly.db.elephantsql.com" , database="pzwjbxpa" , user="pzwjbxpa" , password="uJc-nBJ3OsueJnkemJfbDBvTDQferYHa")
