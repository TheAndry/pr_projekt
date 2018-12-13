import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as stock_info
import csv

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

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
        for FRAME in (MainPage, Stocks, MoneyData):
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

        button_finance = tk.Button(self, text="Aktsiad", command=lambda: controller.show_frame("Stocks"))
        button_finance.place(x=0, y=0, width=400, height=600)

        button_school = tk.Button(self, text="Rahavoog", command=lambda: controller.show_frame("MoneyData"))
        button_school.place(x=400, y=0, width=400, height=600)
    
    def alert(self, text):
        messagebox.showinfo("Teavitus", message=text)

class Stocks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        button_back = tk.Button(self, text="Avalehele", command=lambda: controller.show_frame("MainPage"))
        button_back.place(x=0, y=0)
        
        stock_lable = tk.Label(self, text="Aktsia sümbol")
        stock_lable.place(x=100, y=60)
        self.stock = tk.Entry(self)
        self.stock.place(x=100, y=80)
        
        button_stock = tk.Button(self, text="Graafik", command=lambda: self.show_stock())
        button_stock.place(x=100, y=110)
        
    def show_stock(self):
    
        try:
            data = stock_info.DataReader(self.stock.get(), "yahoo")
            data["Adj Close"].plot()
            plt.title(self.stock.get())
            plt.show()
        except:
            messagebox.showinfo("Teavitus", "Sellist sümbolit ei leitud!")

class MoneyData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button_back = tk.Button(self, text="Avalehele", command=lambda: controller.show_frame("MainPage"))
        button_back.grid(row=0, column=0)
        
        tk.Label(self, text="Rahavoog:").grid(row=1, column=0)
        tk.Label(self, text="Kirjeldus:").grid(row=1, column=2)
        
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=1, column=3)


        tk.Button(self, text='Lisa', command=self.add).grid(row=1, column=4, sticky=tk.W)
        tk.Button(self, text='Salvesta andmed', command=self.save).grid(row=1, column=5)
        
        self.data = {}
        
        try: self.read_data()
        except FileNotFoundError: self.save()
        
    
    def add(self):
        try: int(self.e1.get());is_dig=True
        except ValueError: is_dig=False
        if (self.e1.get() != '' and self.e2.get() != ''):
            if (is_dig == True):
                self.data[len(self.data)+1]=list((self.e1.get(), self.e2.get()))
                self.e1.delete(0, 'end')
                self.e2.delete(0, 'end')
                self.tabel(self.data)
            else:
                self.e1.delete(0, 'end')
                return messagebox.showinfo("Teavitus", "Palun sisestage rahavoo lahtrisse aind numbreid")
        else:
            return messagebox.showinfo("Teavitus", "Palun täitke mõlemad lahtrid :)")

    def save(self):
        w = csv.DictWriter(open("raha_data.csv","w"), ['nr','summa','kirjeldus'])
        w.writeheader()
        for nr, sisu in self.data.items():
            rida = {}
            rida['nr']=nr
            rida['summa']=sisu[0]
            rida['kirjeldus']=sisu[1]
            w.writerow(rida)
        
    def read_data(self):
        w = csv.DictReader(open("raha_data.csv","r"))
        for row in w:
            d_row = []
            d_row.append(row['summa'])
            d_row.append(row['kirjeldus'])
            self.data[row['nr']]=d_row
        self.tabel(self.data)
            
    def tabel(self, data):
        total = 0
        tk.Label(self, text="Sissekande number").grid(row=2, column=1)
        tk.Label(self, text="Summa").grid(row=2, column=2, columnspan=2)
        tk.Label(self, text="Kirjeldus").grid(row=2, column=4, columnspan=2)
        for key in data.keys():
            nr = int(key)+1
            sisu = data[key]
            tk.Label(self, text=nr-1).grid(row=nr+1, column=1)
            t1 = tk.Entry(self)
            t2 = tk.Entry(self)
            t1.grid(row=nr+1, column=2, columnspan=2)
            t1.insert(nr+1,sisu[0])
            t2.grid(row=nr+1, column=4, columnspan=2)
            t2.insert(nr+1,sisu[1])
            total = total + int(sisu[0])
            text_total = 'Summa: '+str(total)
            sum = tk.Label(self, text=text_total).grid(row=1, column = 6)
    
        

if __name__ == "__main__":
    prog = Program()
    prog.mainloop()
