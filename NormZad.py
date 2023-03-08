from tkinter import *
from tkinter import ttk
import guiCommon, guiDepartments, guiPositions, guiTasks, \
        guiJobs, guiWorkers, guiConfiguration, blConfiguration

blConfiguration.checkConfig()

_err, showId = blConfiguration.getShowId()
root = guiCommon.form(title="Нормированные задания")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
frameTabel = guiJobs.createFrame(root, showId)
notebook.add(frameTabel, text="Табель")

frameWorkers = guiWorkers.createFrame(root, showId)
notebook.add(frameWorkers, text="Сотрудники")

frameDepartments = guiDepartments.createFrame(root, showId)
notebook.add(frameDepartments, text="Подразделения")

framePositions = guiPositions.createFrame(root, showId)
notebook.add(framePositions, text="Должности")

frameTasks = guiTasks.createFrame(root, showId)
notebook.add(frameTasks, text="Задания")

frameTasks = guiConfiguration.createFrame(root)
notebook.add(frameTasks, text="Конфигурация")

root.mainloop()

