from win import WinForms, Size, Point
import guiDictionary

tableArg = {'name':'JobList','title':'Задания'}

class frmJobList(guiDictionary.frmTable):
    def __init__(self) -> None:
        fldsArg = []
        fldsArg.append({'fld_name':'Id',        'title':'Id',          'visible':False, 'width':10,  'readonly':True})
        fldsArg.append({'fld_name':'Date',      'title':'Дата',        'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'WorkerId',  'title':'Табельный №', 'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'ShortName', 'title':'Ф.И.О.',      'visible':True,  'width':300, 'readonly':False})
        fldsArg.append({'fld_name':'Level',     'title':'Разряд',      'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'Position',  'title':'Должность',   'visible':True,  'width':150, 'readonly':False})
        fldsArg.append({'fld_name':'Task',      'title':'Задание',     'visible':True,  'width':200, 'readonly':False})
        fldsArg.append({'fld_name':'TimeJob',   'title':'Время',       'visible':True,  'width':100, 'readonly':False})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.Size = Size(1000, 500)

