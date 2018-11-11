import tkinter as tk
from tkinter import messagebox

class Program(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Projekt")
        self.geometry("800x600")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for FRAME in (MainPage, Finance):
            page_name = FRAME.__name__
            frame = FRAME(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button_finance = tk.Button(self, text="Finants", command=lambda: controller.show_frame("Finance"))
        button_finance.place(x=0, y=0, width=400, height=600)

        button_school = tk.Button(self, text="Kool \n (Peagi tulekul)", state='disabled')
        button_school.place(x=400, y=0, width=400, height=600)
    
    def alert(self, text):
        messagebox.showinfo('Teavitus', message=text)


class Finance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button_back = tk.Button(self, text="Avalehele", command=lambda: controller.show_frame("MainPage"))
        button_back.place(x=0, y=0)

class School(tk.Frame):
    def __init__(self, parent, controller):
        return None

if __name__ == "__main__":
    prog = Program()
    prog.mainloop()
