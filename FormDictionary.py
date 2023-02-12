import clr
import db
# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")

import System.Windows.Forms as WinForms
# import System.Windows
from System.Drawing import Size, Point, Color

class frmDictionary(WinForms.Form):
    def __init__(self, tableArg, fldsArg) -> None:
        super().__init__()
        self.Text = tableArg['title']
        self.grd = WinForms.DataGridView()
        self.table = tableArg
        self.flds = fldsArg
        self.Controls.Add(self.grd)
        for f in self.flds:
            col = WinForms.DataGridViewColumn()
            col.CellTemplate = WinForms.DataGridViewTextBoxCell()
            col.Name = f['title']
            col.Visible = f['visible']
            if col.Visible:
                col.Width = f['width']
                col.ReadOnly = f['readonly']
            
            self.grd.Columns.Add(col)
        self.getData()
        self.Resize += self.myResized
        self.Size = Size(500,300)
        
    def myResized(self, parent, e):
        w,h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)

    
    
    # def getData():

    def getData(self):
        tableName = self.table['name']
        flds = [f['name'] for f in self.flds]
        err, data = db.select(tableName, flds)
        if err:
            WinForms.MessageBox.Show(err)
        else:
            for row in data:
                self.grd.Rows.Add(row)

    def Execute(self):
        WinForms.Application.Run(self)


def frmPositions():
    table = {'name':'Positions','title':'Должнсти'}
    cols = []
    cols.append({'name':'Id',   'title':'Id',        'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Name', 'title':'Название', 'visible':True,  'width':300, 'readonly':True})

    frm = frmDictionary(table, cols) 
    return frm

def frmTasks():
    table = {'name':'Tasks','title':'Задания'}
    cols = []
    cols.append({'name':'Id',   'title':'Id',        'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Name', 'title':'Название', 'visible':True,  'width':300, 'readonly':True})

    frm = frmDictionary(table, cols) 
    return frm

def frmJobList():
    table = {'name':'JobList','title':'Табель'}
    cols = []
    cols.append({'name':'Id',   'title':'Id',               'visible':False, 'width':10,  'readonly':True})
    cols.append({'name':'Date', 'title':'Дата',             'visible':True,  'width':100, 'readonly':True})
    cols.append({'name':'TabelNom', 'title':'Табельный №',  'visible':True,  'width':100, 'readonly':True})
    cols.append({'name':'ShortName', 'title':'Ф.И.О.',      'visible':True,  'width':300, 'readonly':True})
    cols.append({'name':'Level', 'title':'Разряд',          'visible':True,  'width':100, 'readonly':True})
    cols.append({'name':'Position', 'title':'Должность',   'visible':True,  'width':150, 'readonly':True})
    cols.append({'name':'Task', 'title':'Задание',          'visible':True,  'width':200, 'readonly':True})
    cols.append({'name':'TimeJob', 'title':'Время',         'visible':True,  'width':100, 'readonly':True})

    frm = frmDictionary(table, cols) 
    return frm



# if __name__ == '__main__':
    # frmDepartments()
