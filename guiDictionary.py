from win import WinForms, Size, Point
import db

yInterval = 30
dummyId = 0

# DataGridViewComboBoxColumn 
# https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/how-to-host-controls-in-windows-forms-datagridview-cells?view=netframeworkdesktop-4.8
# col.CellTemplate.ValueType = int

class frmTable(WinForms.Form):
    def __init__(self, tableArg, fldsArg, readonly=False) -> None:
        super().__init__()
        self.Text = tableArg['title']
        self.grd = WinForms.DataGridView()
        self.table = tableArg
        self.flds = fldsArg
        self.Controls.Add(self.grd)
        for f in self.flds:
            col = WinForms.DataGridViewColumn()
            col.CellTemplate = WinForms.DataGridViewTextBoxCell()
            if 'title' in f.keys():
                col.Name = f['title']
            if 'visible' in f.keys():
                col.Visible = f['visible']
            if 'width' in f.keys():
                col.Width = f['width']
            if 'readonly' in f.keys():
                col.ReadOnly = f['readonly']
            
            self.grd.Columns.Add(col)
        self.getData()
        self.grd.ReadOnly = readonly
        self.grd.BackgroundColor = self.BackColor
        self.grd.SelectionMode = WinForms.DataGridViewSelectionMode.FullRowSelect
        # self.grd.MultiSelect = False

        self.btnNew = WinForms.Button()
        self.btnNew.Text = 'Добавить'

        self.btnSave = WinForms.Button()
        self.btnSave.MouseClick
        self.btnSave.Text = 'Изменить'

        self.btnDelete = WinForms.Button()
        self.btnDelete.MouseClick += self.doDelete
        self.btnDelete.Text = 'Удалить' 

        self.Controls.Add(self.btnNew)
        self.Controls.Add(self.btnSave)
        self.Controls.Add(self.btnDelete)
        
        self.Resize += self.myResized
        self.Size = Size(500,300)

    def doDelete(self, sender, e):
        tableName = self.table['name']
        id = self.getSelectedId()
        if id is not None:
            if WinForms.DialogResult.Yes == WinForms.MessageBox.Show(f"Удалить", "Вопрос", WinForms.MessageBoxButtons.YesNo):
                err = db.delete(tableName,'id', id)
                if err:
                    WinForms.MessageBox.Show(err)
                else:
                    self.getData()
        pass

    def myResized(self, sender, e):
        w, h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)
        y = self.grd.Size.Height + self.grd.Location.Y + yInterval
        self.btnNew.Location = Point(50, y)
        self.btnSave.Location = Point(150, y)
        self.btnDelete.Location = Point(250, y)
    
    def getSelectedId(self):
        selectedId = self.grd.SelectedRows[0].Cells['Id'].Value
        return selectedId

    def getData(self):
        self.grd.Rows.Clear()
        tableName = self.table['name']
        flds = [f['fld_name'] for f in self.flds]
        err, data = db.select(tableName, flds)
        if err:
            WinForms.MessageBox.Show(err)
        else:
            for row in data:
                self.grd.Rows.Add(row)

    def Execute(self):
        WinForms.Application.Run(self)

# --------------------------------------------------
class cntLblText(WinForms.ContainerControl):
    def __init__(self, name, header, value='', readonly=False) -> None:
        super().__init__()
        self.Name=name
        self.Size = Size(300, 24)

        self.lbl_header = WinForms.Label()
        self.lbl_header.Text = header
        self.lbl_header.Size = Size(150, 24)
        self.lbl_header.Location = Point(0,0)
        self.Controls.Add(self.lbl_header)

        self.txt_value = WinForms.TextBox()
        self.txt_value.Size = Size(150, 24)
        self.txt_value.Location = Point(150,0)
        self.txt_value.ReadOnly = readonly
        self.txt_value.Text = value
        self.Controls.Add(self.txt_value)

# --------------------------------------------------
class frmSimpleObject(WinForms.Form):
    def __init__(self, tableArg, argId, argName, size=Size(500,300)) -> None:
        super().__init__()
        self.Size = size
        self.MinimumSize = size
        self.MaximumSize = size
        self.TableName = tableArg
        x = 20
        y = 10

        y = y + yInterval
        self.cntLblTxtId = cntLblText(name='lbl', header='Id', readonly = True)
        self.cntLblTxtId.Location = Point(x, y)
        self.cntLblTxtId.txt_value.Text = str(argId)
        self.Controls.Add(self.cntLblTxtId)

        y = y + yInterval
        self.cntLblTxtName = cntLblText(name='txt', header='Название')
        self.cntLblTxtName.Name='qq'
        self.cntLblTxtName.Location = Point(x, y)
        self.cntLblTxtName.txt_value.Text = argName
        self.Controls.Add(self.cntLblTxtName)

        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = y + yInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.saveData
        self.Controls.Add(self.btnSave)
        pass
    
    def saveData(self, sender, e):
        if __name__ == '__main__':
            if int(self.cntLblTxtId.txt_value.Text) == dummyId:
                WinForms.MessageBox.Show('New')
            else: 
                WinForms.MessageBox.Show(f'save {self.cntLblTxtId.txt_value.Text}')


    def Execute(self):
        WinForms.Application.Run(self)


if __name__ == '__main__':
    table = {'name':'Departments','title':'Справочник', 'readonly':True}
    cols = []
    cols.append({'fld_name':'Id',   'title':'Id',       'visible':True, 'readonly':True,   'width':50})
    cols.append({'fld_name':'Name', 'title':'Название', 'visible':True, 'readonly':False,  'width':300})

    frm = frmTable(table, cols, readonly=True)
    frm.Execute()

    # frm = frmSimpleObject(tableArg='Справочник', argId=dummyId, argName='testData')
    # frm.ShowDialog()
