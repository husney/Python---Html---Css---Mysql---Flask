from tkinter import *

raiz = Tk()

framePrincipal = Frame(raiz, width=1200, height=500)
framePrincipal.pack()

nombrelbl = Label(framePrincipal, text="Nombre:")
nombrelbl.grid(row=0,column=0, sticky="e", padx=10, pady=10)

pruebaVar = StringVar()
nobretxt = Entry(framePrincipal,textvariable=pruebaVar)
nobretxt.grid(row=0, column=1, padx=10, pady=10)

contraseñalbl = Label(framePrincipal, text="Contraseña: ")
contraseñalbl.grid(row=1, column=0, sticky="e", padx=10, pady=10)

contraseñatxt = Entry(framePrincipal)
contraseñatxt.grid(row=1, column=1, padx=10,pady=10)
contraseñatxt.config(fg="blue", justify="center", show="*")

comentarioslbl = Label(framePrincipal, text="Comentarios:")
comentarioslbl.grid(row=2, column=0, padx=10, pady=10)

comentariosText = Text(framePrincipal, widt=15, height=10, )
comentariosText.grid(row=2, column=1, pady=10, padx=10)

scroll = Scrollbar(framePrincipal, command=comentariosText.yview)
scroll.grid(row=2, column=2, sticky="nsew")

comentariosText.config(yscrollcommand=scroll.set)


def metodoBoton():
    pruebaVar.set("Agregado por boton enviar")


miBoton = Button(raiz, text="Enviar", command=metodoBoton)
#variable = Button(contenedor, text="texto", command=método)
miBoton.pack()


raiz.mainloop()
