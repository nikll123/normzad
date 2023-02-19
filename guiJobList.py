from common import WinForms, Size, Point
import guiBaseForm

tableArg = {'name':'JobList','header':'Табель'}

class frmJobList(guiBaseForm.frmDictionary):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',        'header':'Id',          'visible':False, 'width':10,  'readonly':True})
        fldsArg.append({'fld_name':'Date',      'header':'Дата',        'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'WorkerId',  'header':'Табельный №', 'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'ShortName', 'header':'Ф.И.О.',      'visible':True,  'width':300, 'readonly':False})
        fldsArg.append({'fld_name':'Level',     'header':'Разряд',      'visible':True,  'width':100, 'readonly':False})
        fldsArg.append({'fld_name':'Position',  'header':'Должность',   'visible':True,  'width':150, 'readonly':False})
        fldsArg.append({'fld_name':'Task',      'header':'Задание',     'visible':True,  'width':200, 'readonly':False})
        fldsArg.append({'fld_name':'TimeJob',   'header':'Время',       'visible':True,  'width':100, 'readonly':False})
        super().__init__(tableArg, fldsArg, readonly=True)
        self.Size = Size(1000, 500)

