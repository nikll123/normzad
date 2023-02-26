from tkinter.messagebox import showerror, askyesno

def notError(err):
    """проверка наличия ошибки 

    если err не пустая строка - значит есть ошибка, 
    выдатеся сообщение об ошибке и возвращается True, иначе False."""
    isError = err != ''
    if isError:
        showerror(title="Ошибка", message=err)
    return not isError

