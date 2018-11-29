import tkinter as tk
from tkinter import ttk


class nombreClase(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="start", command=self.start)
        self.button.pack()
        self.root = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.root.pack()

        self.valor = 0
        self.valorMaximo = 0

    def start(self):
        self.root["value"] = 0
        self.valorMaximo = 50000
        self.root["maximum"] = 50000
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update root bar'''
        self.valor += 50
        self.root["value"] = self.valor
        if self.valor < self.valorMaximo:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
        # print(valor)
    
app = nombreClase()
app.mainloop()