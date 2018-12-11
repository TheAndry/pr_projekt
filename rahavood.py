from tkinter import *
from tkinter import messagebox
import csv

def add():
    if e1.get() != '' and e2.get() != '':
        if e1.get().isdigit() == True:
            data[len(data)+1]=set((e1.get(), e2.get()))
            tabel(data)
        else:
            e1.delete(0, 'end')
            return messagebox.showinfo("Teavitus", "Palun sisestage rahavoo lahtrisse aind numbreid")
    else:
        return messagebox.showinfo("Teavitus", "Palun täitke mõlemad lahtrid :)")

def save():
    w = csv.DictWriter(open("raha_data.csv","w"), ['nr','sisu'])
    w.writeheader()
    for nr, sisu in data.items():
        rida = {}
        rida['nr']=nr
        rida['sisu']=sisu
        w.writerow(rida)
        
def read_data():
    w = csv.DictReader(open("raha_data.csv","r"))
    for rida in w:
        data[rida['nr']]=rida['sisu']
    tabel(data)
        
def tabel(data):
    Label(main, text="Jrk").grid(row=1, column=1)
    Label(main, text="Summa").grid(row=1, column=2, columnspan=2)
    Label(main, text="Kirjeldus").grid(row=1, column=4, columnspan=2)
    for key in data.keys():
        nr = int(key)
        sisu = data[key]
        Label(main, text=nr).grid(row=nr+1, column=1)
        e1 = Entry(main)
        e2 = Entry(main)
        e1.grid(row=nr+1, column=2, columnspan=2)
        e1.insert(nr+1,sisu)
        e2.grid(row=nr+1, column=4, columnspan=2)
        e2.insert(nr+1,sisu)

main = Tk()
main.title("Projekt")
main.geometry("800x600")

Label(main, text="Rahavoog:").grid(row=0, column = 0)
Label(main, text="Kirjeldus:").grid(row=0, column=2)

e1 = Entry(main)
e2 = Entry(main)

e1.grid(row=0, column=1)
e2.grid(row=0, column=3)

Button(main, text='Lisa', command=add).grid(row=0, column=4, sticky=W)
Button(main, text='Salvesta andmed', command=save).grid(row=0, column=5)

data = {}
read_data()

main.mainloop()
