from tkinter import ttk
import tkinter
import reports

# import sqlite3

# def connect():

#     con1 = sqlite3.connect("tmp.db")

#     cur1 = con1.cursor()

#     cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

#     con1.commit()

#     con1.close()


# def View():

#     con1 = sqlite3.connect("tmp.db")

#     cur1 = con1.cursor()

#     cur1.execute("SELECT * FROM table1")

#     rows = cur1.fetchall()    
#     rows = reports.JobList()

#     for row in rows:
#         tree.insert("", tkinter.END, values=row)        

#     con1.close()


# connect to the database

# connect() 

def treeAddColumn(tree, title, width):
    tree.colCount = tree.colCount + 1
    cc = tree.colCount
    tree.column(f"#{cc}", anchor=tkinter.W, width=width)
    tree.heading(f"#{cc}", text=title)
    return tree

def jobList():
    root = tkinter.Tk()
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
    tree.colCount = 0
    tree = treeAddColumn(tree, "id", 40)
    tree = treeAddColumn(tree, "Дата", 100)
    tree = treeAddColumn(tree, "Таб. номер", 80)
    tree = treeAddColumn(tree, "ФИО", 200)
    tree = treeAddColumn(tree, "Разряд", 40)
    tree = treeAddColumn(tree, "Специальность", 200)
    tree = treeAddColumn(tree, "Задание", 200)
    tree = treeAddColumn(tree, "Время", 80)
    
    tree.pack()

    rows = reports.JobList()
    for row in rows:
        tree.insert("", tkinter.END, values=row)        

    # button1 = tkinter.Button(text="Display data", command=View)
    # button1.pack(pady=10)
    root.mainloop()

jobList()
