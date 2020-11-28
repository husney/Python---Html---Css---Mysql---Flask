from tkinter import *
from tkinter import filedialog

root = Tk()

frame = Frame(root)
frame.pack()

def abrirFichero():
    fichero = filedialog.askopenfilenames(title="Abrir", initialdir="C:",
    filetypes=(("Ficheros text", "*.txt"), 
               ("Ficheros de imagen", "*.png"),
               ("Todos los ficheros", "*.*")
               ))
    #askopenfilename(titulo="" ,) un archivo
    #asdkopenfilenames(titulo="") más de un archivo
    #atributos:
    #initialdir="ruta" especifica la ruta en la cual se posicionara
    #cuando se abra la ventana, normalmente esta en mi documentos
    #filetypes recibe una tupla y indica los nombres a buscar y extenciones
    print(fichero)

botonAbrir = Button(frame, text="Abrir archivo", command=abrirFichero)
botonAbrir.grid(row=0, column=0)


root.mainloop()
