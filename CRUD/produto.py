from produto_db import Produto
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidproduto = Label(self.container2,
        text="idProduto:", font=self.fonte, width=10)
        self.lblidproduto.pack(side=LEFT)

        self.txtidproduto = Entry(self.container2)
        self.txtidproduto["width"] = 10
        self.txtidproduto["font"] = self.fonte
        self.txtidproduto.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lbldescricao = Label(self.container3, text="Descrição:",
        font=self.fonte, width=10)
        self.lbldescricao.pack(side=LEFT)

        self.txtdescricao = Entry(self.container3)
        self.txtdescricao["width"] = 25
        self.txtdescricao["font"] = self.fonte
        self.txtdescricao.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirProduto
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProduto
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProduto
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirProduto(self):
        prod = Produto()

        prod.descricao = self.txtdescricao.get()
        self.lblmsg["text"] = prod.insertProdutos()
        self.txtidproduto.delete(0, END)
        self.txtdescricao.delete(0, END)


    def alterarProduto(self):
        prod = Produto()

        prod.idproduto = self.txtidproduto.get()
        prod.descricao = self.txtdescricao.get()
        self.lblmsg["text"] = prod.updateProdutos()
        self.txtidproduto.delete(0, END)
        self.txtdescricao.delete(0, END)


    def excluirProduto(self):
        prod = Produto()

        prod.idproduto = self.txtidproduto.get()
        self.lblmsg["text"] = prod.deleteProdutos()
        self.txtidproduto.delete(0, END)
        self.txtdescricao.delete(0, END)

    def buscarUsuario(self):
        prod = Produto()

        prod.idproduto = self.txtidproduto.get()
        self.lblmsg["text"] = prod.selectProdutos()
        self.txtidproduto.delete(0, END)
        self.txtidproduto.insert(INSERT, prod.idproduto)
        self.txtdescricao.delete(0, END)
        self.txtdescricao.insert(INSERT, prod.descricao)


root = Tk()
root.title("Cadastro Produtos")
Application(root)
root.mainloop()