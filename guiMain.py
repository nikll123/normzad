from tkinter import *
from tkinter import ttk
import guiCommon, guiDepartments, guiPositions, guiTasks, guiJobs, guiWorkers

root = guiCommon.form(title="Нормированные задания")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
frameTabel = guiJobs.createFrame(root)
notebook.add(frameTabel, text="Табель")

frameWorkers = guiWorkers.createFrame(root)
notebook.add(frameWorkers, text="Сотрудники")

frameDepartments = guiDepartments.createFrame(root)
notebook.add(frameDepartments, text="Подразделения")

framePositions = guiPositions.createFrame(root)
notebook.add(framePositions, text="Должности")

frameTasks = guiTasks.createFrame(root)
notebook.add(frameTasks, text="Задания")

root.mainloop()

