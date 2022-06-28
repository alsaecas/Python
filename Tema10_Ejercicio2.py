from tkinter import *
from tkinter import ttk

if __name__ == '__main__':

    window = Tk()

    texto = ttk.Label(window, text='Lista de texto')
    texto.pack()

    listbox = Listbox(window)
    for item in range(1, 10):
        listbox.insert(END, f'Elemento {item}')
    listbox.pack()

    window.mainloop()
