from tkinter import *
from tkinter import ttk
# import tkinter
# from tkinter.messagebox import showerror, showwarning, showinfo, askyesno, askyesnocancel
import  guiDepartments

# def saveDepartment(e):
#     pass
    # btn = e.widget
    # print(btn['name'])

    # result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")
    # if result: showinfo("Результат", "Операция подтверждена")
    # else: showinfo("Результат", "Операция отменена")


# def treeAddColumn(tree, title, width):
#     tree.colCount = tree.colCount + 1
#     cc = tree.colCount
#     tree.column(f"#{cc}", anchor=tkinter.W, width=width)
#     tree.heading(f"#{cc}", text=title)
#     return tree

# def jobList():
#     root = tkinter.Tk()
#     tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
#     tree.colCount = 0
#     tree = treeAddColumn(tree, "id", 40)
#     tree = treeAddColumn(tree, "Дата", 100)
#     tree = treeAddColumn(tree, "Таб. номер", 80)
#     tree = treeAddColumn(tree, "ФИО", 200)
#     tree = treeAddColumn(tree, "Разряд", 40)
#     tree = treeAddColumn(tree, "Специальность", 200)
#     tree = treeAddColumn(tree, "Задание", 200)
#     tree = treeAddColumn(tree, "Время", 80)
    
#     tree.pack()

#     rows = reports.JobList()
#     for row in rows:
#         tree.insert("", tkinter.END, values=row)        

    # button1 = tkinter.Button(text="Display data", command=View)
    # button1.pack(pady=10)


root = Tk()
root.title("Нормированные задания")
root.geometry("300x600")
root.iconbitmap("nz.ico")
root.btnDepartments = ttk.Button(root, text="Подразделения")
root.btnDepartments.bind('<ButtonRelease-1>', guiDepartments.openFormDepartments)
root.btnDepartments.grid(row=0,column=0,padx=10,pady=10)
root.mainloop()
