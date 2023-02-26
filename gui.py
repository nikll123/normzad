from tkinter import *
from tkinter import ttk
import guiCommon, guiDepartments, guiPositions

root = guiCommon.formTk(title="Нормированные задания", frmName='root')

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
frameDepartments = guiDepartments.createFrame(root)
notebook.add(frameDepartments, text="Подразделения")

framePositions = guiPositions.createFrame(root)
notebook.add(framePositions, text="Должности")


root.mainloop()

