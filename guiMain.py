from tkinter import *
from tkinter import ttk
import guiCommon, guiDepartments, guiPositions, guiTasks, guiJobList

root = guiCommon.form(title="Нормированные задания")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
frameDepartments = guiJobList.createFrame(root)
notebook.add(frameDepartments, text="Табель")

frameDepartments = guiDepartments.createFrame(root)
notebook.add(frameDepartments, text="Подразделения")

framePositions = guiPositions.createFrame(root)
notebook.add(framePositions, text="Должности")

frameTasks = guiTasks.createFrame(root)
notebook.add(frameTasks, text="Задания")

root.mainloop()

