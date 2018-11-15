from tkinter import *
import csv

def add():
    data[len(data)+1]=set((e1.get(), e2.get()))
    
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
        
data = {}
read_data()

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

main.mainloop()
