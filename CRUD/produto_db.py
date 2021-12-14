#para usar SQlite  utilize o Banco de banco
from banco import Banco

#para usar MySQL  utilize o Banco de bancomysql
#from bancomysql import Banco

class Produto(object):
    def __init__(self, idproduto = 0, descricao = ""):
      self.info = {}
      self.idproduto = idproduto
      self.descricao = descricao


    def insertProdutos(self):
      banco = Banco()
      try:
          c = banco.conexao.cursor()
          c.execute("insert into produto (descricao) "
                    "values ('" + self.descricao + "' )")

          banco.conexao.commit()
          c.close()
          return "Produto cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do Produto"

    def updateProdutos(self):
      banco = Banco()
      try:
          c = banco.conexao.cursor()
          c.execute("update produto set descricao = '" + self.descricao + "' where idproduto = "
                    + self.idproduto + " ")
          banco.conexao.commit()
          c.close()
          return "Produto atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do Produto"

    def deleteProdutos(self):
      banco = Banco()
      try:
          c = banco.conexao.cursor()
          c.execute("delete from produto where idproduto = " + self.idproduto + " ")
          banco.conexao.commit()
          c.close()
          return "Produto excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do Produto"

    def selectProdutos(self):
      banco = Banco()
      try:
          c = banco.conexao.cursor()
          c.execute("select * from produto where idproduto = " + self.idproduto + "  ")
          for linha in c:
              self.idproduto = linha[0]
              self.descricao = linha[1]

          c.close()
          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do Produto"