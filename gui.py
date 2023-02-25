from tkinter import *
from tkinter import ttk
import guiDepartments, guiPositions

root = Tk()
root.title("Нормированные задания")
root.Name = 'root'
root.geometry("300x600")
root.iconbitmap("nz.ico")


# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
guiDepartments.mainFrame(notebook)
guiPositions.createFramePositions(notebook)

root.mainloop()
