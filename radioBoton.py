from tkinter import *

def imprimir(*args):
    print(f" El usuario {opciones.get()}")


root=Tk()
root.title("Botón examinar")

opciones=StringVar()
opcionesLabell=Label(root, text="Opciones").grid(row=0, column=0, padx=5, pady=5)
Radiobutton(root, text="Opción 1", variable=opciones, command=imprimir, cursor="hand2", value='Selecciona 1').grid(row=0,column=1)
Radiobutton(root, text="Opción 2", variable=opciones, command=imprimir, cursor="hand2", value='Selecciona 2').grid(row=0,column=2)

root.mainloop()