#importando módulo do SQlite
import MySQLdb

class Banco():
    def __init__(self):
        self.conexao = MySQLdb.Connect('localhost','root','sql123')
        self.conexao.select_db('banco')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key auto_increment ,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")

        self.conexao.commit()
        c.close()
