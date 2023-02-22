from common import *
import guiBaseForm
import dbWorkers

table = {'name':'workerList','header':'Сотрудники'}
fldList = []
fldList.append({'fld_name':'Id',          'header':'Таб. №',        'visible':True,  'width':50})
fldList.append({'fld_name':'LastName',    'header':'Фамилия',       'visible':True,  'width':200})
fldList.append({'fld_name':'Name',        'header':'Имя',           'visible':True,  'width':200})
fldList.append({'fld_name':'SecondName',  'header':'Отчество',      'visible':True,  'width':200})
fldList.append({'fld_name':'Level',       'header':'Разряд',        'visible':True,  'width':100})
fldList.append({'fld_name':'Department',  'header':'Подразделение', 'visible':True,  'width':100})
fldList.append({'fld_name':'Position',    'header':'Должность',     'visible':True,  'width':100})
fldList.append({'fld_name':'DepartmentId','header':'DepartmentId',  'visible':False, 'width':100})
fldList.append({'fld_name':'PositionId',  'header':'PositionId',    'visible':False, 'width':100})

class frmWorkers(guiBaseForm.frmDictionary):
    def __init__(self):
        super().__init__(table, fldList, readonly=True)
        self.Size = Size(1000,600)

    def editItem(self, sender, e):
        id, name, secondName, lastName, level, departmentId, positionId = \
            self.getSelectedRowValues(['id', 'Name', 'SecondName', 'LastName', 'Level', 'DepartmentId', 'PositionId'])
        frm = frmWorker(id, name, secondName, lastName, level, departmentId, positionId, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        id = guiBaseForm.dummyId
        name = ''
        frm = frmWorkers(id, name, self)
        frm.ShowDialog()

    def deleteItem(self, sender, e):
        if not self.grd.SelectedRows[0].IsNewRow:
            id, name, lastname, secondname = self.getSelectedRowValues(['id','Name', 'LastName', 'SecondName'])
            if showQuestionMessage(f"Удалить сотрудника: {lastname} {name} {secondname}?"):
                err = dbWorkers.delete(id)
                isError = checkIfError(err)
                if not isError:
                    self.getDataFromDb()

class frmWorker(WinForms.Form):
    def __init__(self, id, name, secondName, lastName, level, departmentId, positionId, parent):
        super().__init__()
        self.parent = parent
        self.Size = Size(500,600)
        x = 20  # координата X для выстраивания контролов
        # создаем контейнер с Label и TextBox для Id
        self.txtId = cntText(name='txtId', header='Табельный №')
        y = vertInterval                                  # координата Y для первого контейнера
        self.txtId.Location = Point(x, y)                 # положения контейнера
        self.txtId.txt.Text = str(id)
        self.Controls.Add(self.txtId)                     # вставляем на форму

        self.txtName = cntText(name='txtName', header='Имя')
        y = self.txtId.Bottom + vertInterval
        self.txtName.Location = Point(x, y)
        self.txtName.txt.Text = name
        self.Controls.Add(self.txtName)

        self.txtSecondName = cntText(name='txtSecondName', header='Отчество')
        y = self.txtName.Bottom + vertInterval
        self.txtSecondName.Location = Point(x, y)
        self.txtSecondName.txt.Text = secondName
        self.Controls.Add(self.txtSecondName)

        self.txtLastName = cntText(name='txtLastName', header='Фамилия')
        y = self.txtSecondName.Bottom + vertInterval
        self.txtLastName.Location = Point(x, y)
        self.txtLastName.txt.Text = lastName
        self.Controls.Add(self.txtLastName)

        self.txtLevel = cntText(name='txtLevel', header='Разряд')
        y = self.txtLastName.Bottom + vertInterval
        self.txtLevel.Location = Point(x, y)
        self.txtLevel.txt.Text = str(level)
        self.Controls.Add(self.txtLevel)

        self.cmbDepartment = cntCombox(name='cmbDepartment', header='Подразделение', dataSource='vDepartments', idItem=departmentId)
        y = self.txtLevel.Bottom + vertInterval
        self.cmbDepartment.Location = Point(x, y)
        self.cmbDepartment.cmbBox.Text = str(level)
        self.cmbDepartment.DropDownStyle = WinForms.ComboBoxStyle.DropDownList
        self.Controls.Add(self.cmbDepartment)

        self.cmbPosition = cntCombox(name='cmbPosition', header='Должность', dataSource='vPositions', idItem=positionId)
        y = self.cmbDepartment.Bottom + vertInterval
        self.cmbPosition.Location = Point(x, y)
        self.cmbPosition.cmbBox.Text = str(level)
        self.cmbPosition.DropDownStyle = WinForms.ComboBoxStyle.DropDownList
        self.Controls.Add(self.cmbPosition)

        # создаем кнопку Save
        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = vertInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.doSave                  # цепляем на нее обработчик клика
        self.Controls.Add(self.btnSave)                         # вставляем на форму

    def doSave(self, sender, e):
        id = int(self.txtId.txt.Text)
        LastName = self.txtLastName.txt.Text
        Name = self.txtName.txt.Text
        SecondName = self.txtSecondName.txt.Text
        Level = int(self.txtLevel.txt.Text)
        PositionId = self.cmbPosition.getId()
        DepartmentId = self.cmbDepartment.getId()
        dbWorkers.new(id,LastName,Name,SecondName,Level,PositionId,DepartmentId)
        