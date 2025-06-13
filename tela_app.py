from tkinter import Tk,Button,Label,Text,Frame,Entry,LEFT,RIGHT,END
import os

class AppListaCompras(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x550')
        self.resizable(width=False,height=False)
        self.title('App Lista_Compras')
        self.font = ('ArialBlack','10','bold')
        with open('lista_compras.txt','r',encoding='utf-8') as arquivo:
            self.lista = [linha.strip() for linha in arquivo.readlines()]
        self.container = Frame(self,padx=20)
        self.container.pack()
        self.label = Label(self.container, text='Veja aqui sua Lista de Compras', fg='blue', font=self.font)
        self.label.pack()
        self.tela = Text(self.container,bg='black',fg='limegreen')
        self.tela.pack()
        self.container2 = Frame(self,padx=20)
        self.container2.pack()
        self.label2 = Label(self.container2, text='Digite Aqui um Produto por Vez! Para Adicionar a Lista de Compras', fg='blue', font=self.font)
        self.label2.pack()
        self.entry = Entry(self.container2,width=100)
        self.entry.pack()
        self.add_produto = Button(self.container2,command=self.adicionar,text='Adicionar',font=self.font,bg='blue',width=10)
        self.add_produto.pack(side=LEFT)
        self.excluir_produto = Button(self.container2,command=self.excluir,text='Excluir',font=self.font,bg='red',width=10)
        self.excluir_produto.pack(side=RIGHT)
        self.container3 = Frame(self,padx=20)
        self.container3.pack()
        self.mostrar = Button(self.container3, command=self.mostar_lista, text='Mostar Lista de Compras',font=self.font, bg='green', width=20)
        self.mostrar.grid(row=0,column=0)
        self.sair = Button(self.container3,text='Sair',command=self.quit,width=10,font=self.font)
        self.sair.grid(row=3,column=1)
        self.status = Button(self.container3,text='')
        self.status.grid(row=0,column=2)

    def adicionar(self):
        texto = self.entry.get()
        if texto not in self.lista:
            self.lista.append(self.entry.get().capitalize())
        with open('lista_compras.txt', 'r',encoding='utf-8') as arquivo:
            conteudo = [linha.strip() for linha in arquivo.readlines()]
        with open('lista_compras.txt', 'a', encoding='utf-8') as l:
            for produto in self.lista:
                if produto not in conteudo:
                    l.write(produto+'\n')
        self.tela.delete('0.0','end')
        self.mostar_lista()
        self.status.configure(text='Adiconado com Sucesso a Lista de Compras', fg='green')


    def mostar_lista(self):
        for produto in self.lista:
            self.tela.insert(END, f'{produto}\n')
            self.tela.see(END)
        self.status.configure(text='Lista de Compras aparecendo na Tela', fg='blue')

    def excluir(self):
        texto = self.entry.get().capitalize()
        with open('lista_compras.txt', 'r', encoding='utf-8') as lista:
            linhas = [linha.strip() for linha in lista.readlines()]
        for linha in linhas:
            if texto in linha:
                linhas.remove(linha)
                self.lista.remove(linha)
        with open('lista_compras.txt', 'w', encoding='utf-8') as lista:
            for produto in self.lista:
                lista.write(produto+'\n')
        self.tela.delete('0.0', 'end')
        self.mostar_lista()
        self.status.configure(text='Excluido da Lista de Compras', fg='red')
