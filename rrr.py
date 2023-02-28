import tkinter
from tkinter import *

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
    def ppp(self):
      print(self)


john = Employee('john', 'computer lab', 1000)
john1 = Employee('22', 'computer12', 2000)


ws = Tk(  )
ws.geometry("200x200")
display='Press Any Button, or Press  Key'
Lab= Label(ws, text=display, width=len(display))
Lab.pack(pady=40)

def key(eve):
    if eve.char==eve.keysym:
        message =f'Normal Key {eve.char}'
    elif len(eve.char)==1:
        message =f'Punctuation Key {eve.keysym} ({eve.char})'
    else:
        message =f'Special Key {eve.keysym}'
    Lab.config(text=message)
Lab.bind_all('<Key>', key)

def do_mouse(eventname):
    def mouse_binding(event):
        message = f'Mouse event {eventname}'
        Lab.config(text=message)
    Lab.bind_all(f'<{eventname}>', mouse_binding)

for i in range(1,4):
    do_mouse(f'Button-{i}')
    do_mouse(f'ButtonRelease-{i}')
    do_mouse(f'Double-Button-{i}')


ws.mainloop(  )