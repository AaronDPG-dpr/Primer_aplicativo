import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")


cajatexto = tkinter.Entry(ventana, font="Arial, 13")
cajatexto.grid(row=1, column=1)

etiqueta = tkinter.Label(ventana, bg="green")
etiqueta.grid(row=0, column=1)


def multiplicacion():
    base1 = cajatexto.get()
    etiqueta["text"] = base1


boton1 = tkinter.Button(ventana, text="X", width=10, height=5, command=multiplicacion)
boton1.grid(row=3, column=1)


ventana.mainloop()
