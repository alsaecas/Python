import tkinter
from tkinter import ttk

if __name__ == '__main__':
    def reset():
        seleccionado.set(None)


    window = tkinter.Tk()

    seleccionado = tkinter.StringVar()
    r1 = ttk.Radiobutton(window, text='Option 1', value='1', variable=seleccionado)
    r2 = ttk.Radiobutton(window, text='Option 2', value='2', variable=seleccionado)
    r3 = ttk.Radiobutton(window, text='Option 3', value='3', variable=seleccionado)

    r1.grid(column=0, row=1, pady=5, padx=5)
    r2.grid(column=0, row=2, pady=5, padx=5)
    r3.grid(column=0, row=3, pady=5, padx=5)

    boton = ttk.Button(window, text='Reset', command=reset)
    boton.grid(column=3, row=1, pady=5, padx=5)

    window.mainloop()
