from tkinter import *

raiz = Tk()
raiz.title("Calculadora")

#--Frame
div = Frame(raiz)
div.pack()
#--Visualizador
valor = StringVar()
elementos = []
resultadoOp = StringVar()
valorN = 0
valorR = StringVar()

text = Entry(div, widt=30, textvariable=valor)
text.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
text.config(justify="right")

def agregarValor(n):
    valor.set(valor.get() + n)
    
def operacion():
  pass

def agregarElemento(elemento):
    global valorN, valorR
   
    if valorN == 0:
        print("Asignado1")
        valorN = int(valor.get())
    else:
        print("Asignado 2")
        valorR = int(valor.get())
    valor.set('')
    

def mostrarResultado():
    global ValorN, valorR
   # valorR = valor.get()
    #if elementos.count('+') > 0:
      #  print("El resultado es: ", valorN + valorR)
    print(valorR.get())

    


#--Fila 1

button7 = Button(div, width=5, text="7", command=lambda:agregarValor("7"))
button7.grid(row=1, column=0)

button8 = Button(div, width=5, text="8", command=lambda:agregarValor("8"))
button8.grid(row=1, column=1)

button9 = Button(div, width=5, text="9", command=lambda:agregarValor("9"))
button9.grid(row=1, column=2)

buttonMultiplicar = Button(div, width=5, text="X", command=lambda: agregarElemento("*"))
buttonMultiplicar.grid(row=1, column=3)

#--Fila 2

button4 = Button(div, width=5, text="4", command=lambda:agregarValor("4"))
button4.grid(row=2, column=0)

button5 = Button(div, width=5, text="5", command=lambda:agregarValor("5"))
button5.grid(row=2, column=1)

button6 = Button(div, width=5, text="6", command=lambda:agregarValor("6"))
button6.grid(row=2, column=2)

buttonDividir = Button(div, width=5, text="/", command=lambda:agregarElemento('/'))
buttonDividir.grid(row=2, column=3)

#--Fila 3 

button1 = Button(div, width=5, text="1", command=lambda:agregarValor("1"))
button1.grid(row=3, column=0)

button2 = Button(div, width=5, text="2", command=lambda:agregarValor("2"))
button2.grid(row=3, column=1)

button3 = Button(div, width=5, text="3", command=lambda:agregarValor("3"))
button3.grid(row=3, column=2)

buttonMenos = Button(div, width=5, text="-", command=lambda:agregarElemento('-'))
buttonMenos.grid(row=3, column=3)

#--Fila 4

button0 = Button(div, width=5, text="0", command=lambda:agregarValor("0"))
button0.grid(row=4, column=0)

buttonComa = Button(div, width=5, text=",", command=lambda:agregarValor(","))
buttonComa.grid(row=4, column=1)

buttonIgual = Button(div, width=5, text="=", command=mostrarResultado)
buttonIgual.grid(row=4, column=2)

buttonSumar = Button(div, width=5, text="+", command=lambda:agregarElemento('+'))
buttonSumar.grid(row=4, column=3)





raiz.mainloop()