from tkinter import *

def salvesta():
    andmed[len(andmed)+1]=set((e1.get(), e2.get()))

andmed = {}

main = Tk()
main.title("Projekt")
main.geometry("800x600")

Label(main, text="Rahavoog:").grid(row=0, column = 0)
Label(main, text="Kirjeldus:").grid(row=0, column=2)

e1 = Entry(main)
e2 = Entry(main)

e1.grid(row=0, column=1)
e2.grid(row=0, column=3)

Button(main, text='Lisa', command=salvesta).grid(row=0, column=4, sticky=W)

main.mainloop()
