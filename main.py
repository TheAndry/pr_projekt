from tkinter import *
from tkinter import messagebox

def teavita():
    messagebox.showinfo('Teavitus', 'Vabandame, antud moodul ei ole veel valmis.')

def main():
    
    main = Tk()
    main.title("Projekt")
    main.geometry("800x600")

    button_finance = Button(main, text="Finants")
    button_finance.place(x=0, y=0, width=400, height=600)

    button_school = Button(main, text="Kool \n (Peagi tulekul)", command=teavita)
    button_school.place(x=400, y=0, width=400, height=600 )

    main.mainloop()
    
main()