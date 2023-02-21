from common import *
import guiBaseForm
import dbWorkers

table = {'name':'workerList','header':'Сотрудники'}
fldList = []
fldList.append({'fld_name':'Id',          'header':'Id',            'visible':False, 'width':10})
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

    def editItem(self, sender, e):
        id, name, secondName, lastName, level, departmentId, positionId = \
            self.getSelectedRowValues(['id', 'Name', 'SecondName', 'LastName', 'Level', 'DepartmentId', 'PositionId'])
        frm = frmWorker(id, name, secondName, lastName, level, departmentId, positionId, self)
        frm.ShowDialog()
    
    def createItem(self, sender, e):
        id = guiBaseForm.newId
        name = ''
        frm = frmWorkers(id, name, self)
        frm.ShowDialog()

    def deleteItem(self, sender, e):
        pass
        

class frmWorker(WinForms.Form):
    def __init__(self, id, name, secondName, lastName, level, departmentId, positionId, parent):
        super().__init__()
        self.parent = parent
        self.Size = Size(500,600)
        x = 20  # координата X для выстраивания контролов
        # создаем контейнер с Label и TextBox для Id
        self.cntLblTxt_Id = cntLblText(name='lbl', header='Id', readonly=True)
        y = vertInterval                                        # координата Y для первого контейнера
        self.cntLblTxt_Id.Location = Point(x, y)                 # положения контейнера
        self.cntLblTxt_Id.txt_value.Text = str(id)
        self.Controls.Add(self.cntLblTxt_Id)                     # вставляем на форму

        self.cntLblTxt_Name = cntLblText(name='name', header='Имя')
        y = self.cntLblTxt_Id.Bottom + vertInterval
        self.cntLblTxt_Name.Location = Point(x, y)
        self.cntLblTxt_Name.txt_value.Text = name
        self.Controls.Add(self.cntLblTxt_Name)

        self.cntLblTxt_SecondName = cntLblText(name='secondName', header='Отчество')
        y = self.cntLblTxt_Name.Bottom + vertInterval
        self.cntLblTxt_SecondName.Location = Point(x, y)
        self.cntLblTxt_SecondName.txt_value.Text = secondName
        self.Controls.Add(self.cntLblTxt_SecondName)

        self.cntLblTxt_lastName = cntLblText(name='secondName', header='Фамилия')
        y = self.cntLblTxt_SecondName.Bottom + vertInterval
        self.cntLblTxt_lastName.Location = Point(x, y)
        self.cntLblTxt_lastName.txt_value.Text = lastName
        self.Controls.Add(self.cntLblTxt_lastName)

        self.cntLblTxt_level = cntLblText(name='level', header='Разряд')
        y = self.cntLblTxt_lastName.Bottom + vertInterval
        self.cntLblTxt_level.Location = Point(x, y)
        self.cntLblTxt_level.txt_value.Text = str(level)
        self.Controls.Add(self.cntLblTxt_level)

        # создаем кнопку Save
        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = vertInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.doSave                  # цепляем на нее обработчик клика
        self.Controls.Add(self.btnSave)                         # вставляем на форму


    def doSave(self, sender, e):
        pass