from common import *
import guiBaseForm
import dbWorkers

table = {'name':'workerList','header':'Сотрудники'}
fldList = []
fldList.append({'fld_name':'Id',          'header':'Id',            'visible':False, 'width':50})
fldList.append({'fld_name':'TabNum',      'header':'Таб. №',        'visible':True,  'width':50})
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
        id, tabnum, name, secondName, lastName, level, departmentId, positionId = \
            self.getSelectedRowValues(['id', 'TabNum', 'Name', 'SecondName', 'LastName', 'Level', 'DepartmentId', 'PositionId'])
        frm = frmWorker(id, tabnum, name, secondName, lastName, level, departmentId, positionId, self)
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
    def __init__(self, id, tabnum, name, secondName, lastName, level, departmentId, positionId, parent):
        super().__init__()
        self.parent = parent
        self.Size = Size(500,400)
        self.id = id     # сохраняем id как свойство формы
        x = 20           # координата X для выстраивания виджетов (контролов)
        
        # создаем контейнер с Label и TextBox для Id
        self.cntTxtTn = cntText(name='txtTn', header='Табельный №')
        y = vertInterval                                     # координата Y для первого контейнера
        self.cntTxtTn.Location = Point(x, y)                 # положения контейнера
        self.cntTxtTn.txt.Text = str(tabnum)
        self.Controls.Add(self.cntTxtTn)                     # вставляем на форму

        self.cntTxtName = cntText(name='txtName', header='Имя')
        y = self.cntTxtTn.Bottom + vertInterval
        self.cntTxtName.Location = Point(x, y)
        self.cntTxtName.txt.Text = name
        self.Controls.Add(self.cntTxtName)

        self.cntTxtSecondName = cntText(name='txtSecondName', header='Отчество')
        y = self.cntTxtName.Bottom + vertInterval
        self.cntTxtSecondName.Location = Point(x, y)
        self.cntTxtSecondName.txt.Text = secondName
        self.Controls.Add(self.cntTxtSecondName)

        self.cntTxtLastName = cntText(name='txtLastName', header='Фамилия')
        y = self.cntTxtSecondName.Bottom + vertInterval
        self.cntTxtLastName.Location = Point(x, y)
        self.cntTxtLastName.txt.Text = lastName
        self.Controls.Add(self.cntTxtLastName)

        self.cntTxtLevel = cntText(name='txtLevel', header='Разряд')
        y = self.cntTxtLastName.Bottom + vertInterval
        self.cntTxtLevel.Location = Point(x, y)
        self.cntTxtLevel.txt.Text = str(level)
        self.Controls.Add(self.cntTxtLevel)

        self.cntCmbDepartment = cntCombox(name='cmbDepartment', header='Подразделение', dataSource='vDepartments', id=departmentId)
        y = self.cntTxtLevel.Bottom + vertInterval
        self.cntCmbDepartment.Location = Point(x, y)
        self.cntCmbDepartment.cmbBox.Text = str(level)
        self.cntCmbDepartment.DropDownStyle = WinForms.ComboBoxStyle.DropDownList
        self.Controls.Add(self.cntCmbDepartment)

        self.cntCmbPosition = cntCombox(name='cmbPosition', header='Должность', dataSource='vPositions', id=positionId)
        y = self.cntCmbDepartment.Bottom + vertInterval
        self.cntCmbPosition.Location = Point(x, y)
        self.cntCmbPosition.cmbBox.Text = str(level)
        self.cntCmbPosition.DropDownStyle = WinForms.ComboBoxStyle.DropDownList
        self.Controls.Add(self.cntCmbPosition)

        # создаем кнопку Save
        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = self.cntCmbPosition.Bottom + vertInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.doSave                  # цепляем на нее обработчик клика
        self.Controls.Add(self.btnSave)                         # вставляем на форму

    def doSave(self, sender, e):
        tn = int(self.cntTxtTn.txt.Text)
        LastName = self.cntTxtLastName.txt.Text
        Name = self.cntTxtName.txt.Text
        SecondName = self.cntTxtSecondName.txt.Text
        Level = int(self.cntTxtLevel.txt.Text)
        PositionId = self.cntCmbPosition.getId()
        DepartmentId = self.cntCmbDepartment.getId()
        if self.id == dummyId:
            err = dbWorkers.new(tn,LastName,Name,SecondName,Level,PositionId,DepartmentId)
        else:
            err = dbWorkers.update(self.id ,tn,LastName,Name,SecondName,Level,PositionId,DepartmentId)
        if not checkIfError(err):
            self.parent.getDataFromDb()
            self.Close()

