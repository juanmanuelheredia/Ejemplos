from tkinter import filedialog
from tkinter import *

def examinar():
    global imageProfile
    imageProfile =  filedialog.askopenfilename(initialdir = "/",title = "Selecciona la imagen de perfil",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    print(f 'La ruta es {imageProfile}')

root=Tk()
root.title("Botón examinar")
imagenLabel=Label(root, text="Imagen").grid(row=6, column=0, padx=5, pady=5)
imagenLabel=Button(root, text="Examinar", command=examinar, cursor="hand2", borderwidth=1, bg="#03DAC6").grid(row=6, column=1, sticky="w", padx=10, pady=10)
root.mainloop()