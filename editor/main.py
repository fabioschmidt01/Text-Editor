from tkinter import * 


root=Tk()
root.title('Editor de Texto')   #titulo da aplicação
root.geometry('1200x628+10+10')  #tamanha da janela
#root.resizable(False,False) # desabilita o redimensinamento da janela

menubar=Menu(root)  #barra de menu
root.config(menu=menubar)

filemenu=Menu(menubar, tearoff=False)
menubar.add_cascade(label='Arquivo', menu=filemenu)

filemenu.add_command(label='Novo',accelerator='Ctrl+N')
filemenu.add_command(label='Abrir',accelerator='Ctrl+O')
filemenu.add_separator()
filemenu.add_command(label='Salvar',accelerator='Ctrl+S')
filemenu.add_command(label='Salvar como',accelerator='Ctrl+Alt+S')
filemenu.add_separator()
filemenu.add_command(label='Sair',accelerator='Ctrl+Q')

editmenu=Menu(menubar, tearoff=False)
menubar.add_cascade(label='Editar', menu=editmenu)

root.mainloop()