from tkinter import *
from tkinter import messagebox
import csv

def add():
    if e1.get() != '' and e2.get() != '':
        if e1.get().isdigit() == True:
            data[len(data)+1]=list((e1.get(), e2.get()))
            tabel(data)
        else:
            e1.delete(0, 'end')
            return messagebox.showinfo("Teavitus", "Palun sisestage rahavoo lahtrisse aind numbreid")
    else:
        return messagebox.showinfo("Teavitus", "Palun täitke mõlemad lahtrid :)")

def save():
    w = csv.DictWriter(open("raha_data.csv","w"), ['nr','summa','kirjeldus'])
    w.writeheader()
    for nr, sisu in data.items():
        rida = {}
        rida['nr']=nr
        rida['summa']=sisu[0]
        rida['kirjeldus']=sisu[1]
        w.writerow(rida)
        
def read_data():
    w = csv.DictReader(open("raha_data.csv","r"))
    for row in w:
        d_row = []
        d_row.append(row['summa'])
        d_row.append(row['kirjeldus'])
        data[row['nr']]=d_row
    tabel(data)
        
def tabel(data):
    total = 0
    Label(main, text="Sissekande number").grid(row=1, column=1)
    Label(main, text="Summa").grid(row=1, column=2, columnspan=2)
    Label(main, text="Kirjeldus").grid(row=1, column=4, columnspan=2)
    for key in data.keys():
        nr = int(key)
        sisu = data[key]
        Label(main, text=nr).grid(row=nr+1, column=1)
        t1 = Entry(main)
        t2 = Entry(main)
        t1.grid(row=nr+1, column=2, columnspan=2)
        t1.insert(nr+1,sisu[0])
        t2.grid(row=nr+1, column=4, columnspan=2)
        t2.insert(nr+1,sisu[1])
        total = total + int(sisu[0])
        text_total = 'Summa: '+str(total)
        sum = Label(main, text=text_total).grid(row=0, column = 6)

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
