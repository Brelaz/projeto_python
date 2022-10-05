from curses import newwin
from tkinter import *

janela = Tk()
janela["bg"] = "white"
app = Frame(janela)
app.grid()
menuPrincipal = Menu(app)
janela.config(menu=menuPrincipal)

fileMenu = Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar"
            ,command=iniciarTelaCadastro)
fileMenu.add_command(label="Cadastrar"
            ,command=iniciarTelaCadastro)
menuPrincipal.add_cascade(label="Funcao"
                        ,menu=fileMenu)


def escrever():
    print("O meu nome é :",entryNome.get()
        , "e minha idade é: ", entryIdade.get())
    

lblNome = Label(janela,text="Informe o seu nome: "
            ,font="Times"
            ,bg="white",foreground="black")
lblNome.place(x=100,y=50)

entryNome = Entry(janela)
entryNome.place(x=230,y=55)

lblIdade = Label(janela,text="Informe a sua Idade:"
                ,font="Times"
                ,bg="white", foreground="black")
lblIdade.place(x=100, y=75)

entryIdade = Entry(janela)
entryIdade.place(x=230,y=80)

btnFalarNome = Button(janela,width=40
            ,text="Clicar", command=escrever)
btnFalarNome.place(x=150,y=110)

title = "Sistema Tarumã"
janela.title(title)
janela.geometry("800x600")
janela.resizable(False,False)
janela.mainloop()
janela.destroy()