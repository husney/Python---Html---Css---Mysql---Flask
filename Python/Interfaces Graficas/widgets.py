from tkinter import *
from tkinter import messagebox  


root = Tk()
root.title("Widgets")

menuBar = Menu(root)
root.config(menu=menuBar, width=300, height=300)

def informacion():
    messagebox.showinfo("titulo", "Mensaje")
    #(texto del titulo, mensaje)

def licencia():
    messagebox.showerror("Licencia", "Mensaje")

def salir():
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
    if valor == True:
        exit()
    
def guardar():
    valor = messagebox.askretrycancel("Guardar", "No es posible guardar")
    if valor == True:
        messagebox.showinfo("Guardado", "El archivo se ha guardado")


archivoMenu = Menu(menuBar, tearoff=0)
#-sub elementos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar", command=guardar)
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

archivoEditar = Menu(menuBar)
archivoHerramientas = Menu(menuBar)

archivoAyuda = Menu(menuBar, tearoff=0)
archivoAyuda.add_command(label="Acerca de", command=informacion)
archivoAyuda.add_command(label="Licencia", command=licencia)

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=archivoEditar)
menuBar.add_cascade(label="Herramientas", menu=archivoHerramientas)
menuBar.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()