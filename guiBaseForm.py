from common import WinForms, Size, Point
import db

yInterval = 10
dummyId = 0

# DataGridViewComboBoxColumn 
# https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/how-to-host-controls-in-windows-forms-datagridview-cells?view=netframeworkdesktop-4.8
# col.CellTemplate.ValueType = int

# Форма для работы с табличными данными
class frmBaseTable(WinForms.Form):
    def __init__(self, tableArg, fldsArg, readonly=False):
        super().__init__()
        self.Text = tableArg['header']
        self.tableName = tableArg['name']
        self.grd = WinForms.DataGridView()
        self.table = tableArg
        self.flds = fldsArg
        self.Controls.Add(self.grd)
        # Создание колонок (филдов) в таблице (гриде)
        for fld in self.flds:
            col = WinForms.DataGridViewColumn()
            col.CellTemplate = WinForms.DataGridViewTextBoxCell()
            col.Name = fld['fld_name']
            col.HeaderText = fld['header']
            col.Visible = fld['visible']
            col.Width = fld['width']
             
            self.grd.Columns.Add(col)
        self.getDataFromDb()
        self.grd.ReadOnly = readonly
        self.grd.BackgroundColor = self.BackColor
        self.grd.SelectionMode = WinForms.DataGridViewSelectionMode.FullRowSelect

        self.btnNew = WinForms.Button()
        self.btnNew.Text = 'Добавить'

        self.btnEdit = WinForms.Button()
        self.btnEdit.Text = 'Изменить'

        self.btnDelete = WinForms.Button()
        # self.btnDelete.MouseClick += self.doDelete
        self.btnDelete.Text = 'Удалить' 

        self.Controls.Add(self.btnNew)
        self.Controls.Add(self.btnEdit)
        self.Controls.Add(self.btnDelete)
        
        self.Resize += self.myResized
        self.Size = Size(500,300)

    # def doDelete(self, sender, e):
    #     id = self.getSelectedRowFldValue('id')
    #     if id is not None:
    #         if WinForms.DialogResult.Yes == WinForms.MessageBox.Show(f"Удалить", "Вопрос", WinForms.MessageBoxButtons.YesNo):
    #             err = db.delete(self.tableName,'id', id)
    #             if err:
    #                 WinForms.MessageBox.Show(err)
    #             else:
    #                 self.getDataFromDb()
    #     pass

    def myResized(self, sender, e):
        w, h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)
        y = self.grd.Location.Y + self.grd.Size.Height + yInterval
        self.btnNew.Location = Point(50, y)
        self.btnEdit.Location = Point(150, y)
        self.btnDelete.Location = Point(250, y)
    
    def getSelectedRowFldValue(self, fldName):
        value = self.grd.SelectedRows[0].Cells[fldName].Value
        return value

    def getDataFromDb(self):
        self.grd.Rows.Clear()
        flds = [f['fld_name'] for f in self.flds]
        err, data = db.select(self.tableName, flds)
        if err:
            WinForms.MessageBox.Show(err)
        else:
            for row in data:
                self.grd.Rows.Add(row)

    def Execute(self):
        WinForms.Application.Run(self)

# Контейнер содержащий Label и TextBox
class cntLblText(WinForms.ContainerControl):
    def __init__(self, name, header, value='', readonly=False):
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

# Базовая (шаблон) форма для редактирования элемента справочника
class frmSimpleEditData(WinForms.Form):
    def __init__(self, tableArg, argId, argValue, size=Size(500,300)):
        super().__init__()
        self.Size = size
        self.MinimumSize = size
        self.MaximumSize = size
        self.TableName = tableArg['name']
        self.text = tableArg['header']
        x = 20

        y = yInterval
        self.cntLblTxtId = cntLblText(name='lbl', header='Id', readonly = True)
        self.cntLblTxtId.Location = Point(x, y)
        self.cntLblTxtId.txt_value.Text = str(argId)
        self.Controls.Add(self.cntLblTxtId)

        y = self.cntLblTxtId.Bottom + yInterval
        self.cntLblTxtName = cntLblText(name='txt', header='Название')
        self.cntLblTxtName.Location = Point(x, y)
        self.cntLblTxtName.txt_value.Text = argValue
        self.Controls.Add(self.cntLblTxtName)

        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = self.cntLblTxtName.Bottom + yInterval
        self.btnSave.Location = Point(x, y)
        self.Controls.Add(self.btnSave)


    def Execute(self):
        WinForms.Application.Run(self)


if __name__ == '__main__':
    table = {'name':'Departments','header':'Справочник', 'readonly':True}
    cols = []
    cols.append({'fld_name':'Id',   'header':'Id',       'visible':True, 'readonly':True,   'width':50})
    cols.append({'fld_name':'Name', 'header':'Название', 'visible':True, 'readonly':False,  'width':300})

    frm = frmBaseTable(table, cols, readonly=True)
    frm.Execute()

    # frm = frmSimpleObject(tableArg='Справочник', argId=dummyId, argName='testData')
    # frm.ShowDialog()
