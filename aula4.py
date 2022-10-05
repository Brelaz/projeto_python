import tkinter as tk



def cadastrarUsuarios():
    janelaUsuarios = tk.Toplevel(app)

    lblNome = tk.Label(janelaUsuarios,text="Informe o seu nome: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblNome.place(x=100,y=50)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=230,y=55)
    
    lblSobrenome = tk.Label(janelaUsuarios,text="Informe o seu sobrenome: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblSobrenome.place(x=100,y=75)
    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=260, y=75)

    lblDataNascimento = tk.Label(janelaUsuarios,text="Informe sua data de nascimento"
            ,font="Times"
            ,bg="white", foreground="black")
    lblDataNascimento.place(x=100, y=100)
    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=300, y=100)

    lblCidade = tk.Label(janelaUsuarios,text="Informe a sua cidade"
            ,font="Times"
            ,bg="white", foreground="black")
    lblCidade.place(x=100,y=125)
    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place(x=230,y=125)

    lblEstado = tk.Label(janelaUsuarios, text="Informe o estado: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblEstado.place(x=100, y=150)
    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place(x=230, y=150)
    
    def salvarUsuario():
        print("O nome informado foi: ",entryNome.get())
        print("O sobrenome informado foi: ", entrySobrenome.get())
        print("A data de nascimento informada foi: ", entryDataNascimento.get())
        print("A cidade informada foi: ", entryCidade.get())
        print("O estado informado foi: ",entryEstado.get())
    btnSalvar = tk.Button(janelaUsuarios,width=20
            ,text="Salvar", command=salvarUsuario)
    btnSalvar.place(x=100,y=175)
    
    #entryNome.insert("end","teste")
    #entryNome.insert("end","tormes")
    
    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")
def cadastrarProdutos():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários"
            ,command=cadastrarUsuarios)
fileMenu.add_command(label="Cadastrar Produtos"
            ,command=cadastrarProdutos)
menuPrincipal.add_cascade(label="Funcao"
                        ,menu=fileMenu)

#buttonExample = tk.Button(app, 
#              text="Create new window",
#              command=createNewWindow)
#buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()