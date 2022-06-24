from ast import Lambda
import tkinter as tk
from PIL import ImageTk 
from tkinter import font
import sqlite3
from numpy import random 



bg_colour = "#3d6466"


def fetch_db():
    connection = sqlite3.connect("data/ricette.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table")
    all_tables = cursor.fetchall()
    idx = random.randint(0 , len(all_tables)-1)

    #fetch ingredienti
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()


    #print(all_tables[idx]) 
    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])
    

    ingredients = [] 

    #ingredienti
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " di " + name)

    return title, ingredients

    


def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
        #frame1 widgets
    logo_img = ImageTk.PhotoImage(file="./assets/ballons.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack() 

    tk.Label(frame1, text="pronto per una ricetta al volo?",
    bg=bg_colour,
    fg="white",
    font=("TkMenuFont", 14)
    ).pack()

    #button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()).pack(pady=5)




def load_frame2():
    frame2.tkraise()

    table_name, table_records =fetch_db() 
    title, ingredients = pre_process(table_name, table_records)

#inizializziamo
root = tk.Tk() 
root.title("Recipe Picker")
#posiziona app al centro della finestra
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))


#create frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)
# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()




#run app
root.mainloop() 

