from tkinter import commondialog
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Demo')


def show():
    print("MOSTRA MOSTRA")

#label
label = Label(root, text="testo", font=("Helvetica", 14))


#immagine
photo = tk.PhotoImage(file='./images/Python-logo.png')
image_label = ttk.Label(root, image=photo, text="Pitone", padding=5)
image_label.pack() 
# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

# show button

show_button = ttk.Button(
    root,
    text='Mostra',
    command=lambda: show()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

show_button.pack(
    ipadx=0,
    ipady=5,
    expand=True
)

root.mainloop()

## sezione del codice PANDAS
df = pd.read_csv("starwars.csv", index_col=0)

print(df.loc["R2-D2"])


## Mostro finestra
root.mainloop()