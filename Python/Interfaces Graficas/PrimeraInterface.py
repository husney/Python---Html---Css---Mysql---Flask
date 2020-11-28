from tkinter import *

raiz = Tk() #Creación de la ventana
raiz.title("Ventana de pruebas")

raiz.resizable(1, 1)

raiz.iconbitmap("imagesofspace.ico")

#raiz.geometry("650x500")

raiz.config(bg="lightblue")

frame = Frame()

frame.pack()

frame.config(bd=30)

frame.config(relief="groove")

frame.config(width="650", height="500", bg="gray")

frame.config(cursor="hand2")



raiz.mainloop() #permite ver la ventana (Bucle infinito)
#mainloop() debe estár siempre al final


