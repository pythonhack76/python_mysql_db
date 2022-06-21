from fileinput import close
import pandas as pd
from tkinter import *
from tkinter import ttk

##Funzioni 

def calculate():
    pass

def show():
    try:
        value = float(csvnum.get())
    except ValueError:
        print("errore")
    


def close():
    try:
        root.destroy()
    except ValueError:
        print("non chiude!")

def callback():
    pass

### Configurazione

root = Tk() 
root.title("Modulo Uno")
window_width = 300
window_height = 200 

screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()

#prendi le dimensioni e cerca il punto 

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#struttura
mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#input
csvnum = StringVar()
ttk.Label(mainframe, textvariable=csvnum).grid(column=2, row=2, sticky=(W, E))
button_cerca = ttk.Button(mainframe, text="Cerca", command=show).grid(column=3, row=3, sticky=W)
button_close = ttk.Button(mainframe, text="Chiudi", command=close).grid(column=2, row=3, sticky=W)



mostra = StringVar()
ttk.Label(mainframe, textvariable=mostra).grid(column=2, row=3, sticky=(W, E))



root.mainloop()

