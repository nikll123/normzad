from tkinter import *
from tkinter import ttk
# import tkinter
# from tkinter.messagebox import showerror, showwarning, showinfo, askyesno, askyesnocancel
import  guiDepartments

root = Tk()
root.title("Нормированные задания")
root.Name = 'root'
root.geometry("300x600")
root.iconbitmap("nz.ico")


# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов
guiDepartments.frameDepartments(notebook)


framePos = ttk.Frame(master=notebook)
framePos.pack(fill=BOTH, expand=True)
notebook.add(framePos, text="Должности")

root.mainloop()
