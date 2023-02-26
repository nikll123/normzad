from tkinter import *
from tkinter import ttk
import guiDepartments, guiPositions

root = Tk()
root.title("Нормированные задания")
root.Name = 'root'
root.geometry("400x600")
root.iconbitmap("nz.ico")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
guiDepartments.mainFrame(notebook)

framePositions = guiPositions.createMainFrame()
notebook.add(framePositions, text="Должности")


root.mainloop()

