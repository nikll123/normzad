from tkinter import *
from tkinter import ttk
import guiCommon, guiDepartments, guiPositions, guiTasks

root = guiCommon.formTk(title="Нормированные задания")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
frameDepartments = guiDepartments.createFrame(root)
notebook.add(frameDepartments, text="Подразделения")

framePositions = guiPositions.createFrame(root)
notebook.add(framePositions, text="Должности")

frameTasks = guiTasks.createFrame(root)
notebook.add(frameTasks, text="Задания")

root.mainloop()

