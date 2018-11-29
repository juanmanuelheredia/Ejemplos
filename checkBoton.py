from tkinter import *

def imprimir(*args):
    print(f" Opcion 1 {opcion1.get()}")
    print(f" Opcion 2 {opcion2.get()}")


root=Tk()
root.title("Botón examinar")

opcion1=IntVar()
opcion2=IntVar()
opcionesLabell=Label(root, text="Opciones").grid(row=0, column=0, padx=5, pady=5)
Checkbutton(root, text="Hola", variable=opcion1, command=imprimir, cursor="hand2").grid(row=0,column=1)
Checkbutton(root, text="Adiós", variable=opcion2, command=imprimir, cursor="hand2").grid(row=0,column=2)

root.mainloop()