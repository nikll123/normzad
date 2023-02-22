from common import WinForms, Size, Point
import guiBaseForm

table = {'name':'JobList','header':'Табель'}
fldList = []
fldList.append({'fld_name':'Id',        'header':'Id',          'visible':False, 'width':10,  'readonly':True})
fldList.append({'fld_name':'Date',      'header':'Дата',        'visible':True,  'width':100, 'readonly':False})
fldList.append({'fld_name':'TabNum',    'header':'Табельный №', 'visible':True,  'width':100, 'readonly':False})
fldList.append({'fld_name':'ShortName', 'header':'Ф.И.О.',      'visible':True,  'width':300, 'readonly':False})
fldList.append({'fld_name':'Level',     'header':'Разряд',      'visible':True,  'width':100, 'readonly':False})
fldList.append({'fld_name':'Position',  'header':'Должность',   'visible':True,  'width':150, 'readonly':False})
fldList.append({'fld_name':'Task',      'header':'Задание',     'visible':True,  'width':200, 'readonly':False})
fldList.append({'fld_name':'TimeJob',   'header':'Время',       'visible':True,  'width':100, 'readonly':False})

class frmJobList(guiBaseForm.frmDictionary):
    def __init__(self):
        super().__init__(table, fldList, readonly=True)
        self.Size = Size(1000, 500)

    def createItem(self, sender, e):
        pass
    def editItem(self, sender, e):
        pass
    def deleteItem(self, sender, e):
        pass
