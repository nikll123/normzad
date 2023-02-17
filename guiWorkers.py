import common
import guiBaseForm
import dbWorkers

tableArg = {'name':'workerList','header':'Сотрудники'}

class frmWorkers(guiBaseForm.frmBaseTable):
    def __init__(self):
        fldsArg = []
        fldsArg.append({'fld_name':'Id',         'header':'Id',            'visible':False, 'width':10})
        fldsArg.append({'fld_name':'LastName',   'header':'Фамилия',       'visible':True,  'width':200})
        fldsArg.append({'fld_name':'Name',       'header':'Имя',           'visible':True,  'width':200})
        fldsArg.append({'fld_name':'SecondName', 'header':'Отчество',      'visible':True,  'width':200})
        fldsArg.append({'fld_name':'Level',      'header':'Разряд',        'visible':True,  'width':100})
        fldsArg.append({'fld_name':'Department', 'header':'Подразделение', 'visible':True,  'width':100})
        fldsArg.append({'fld_name':'Position',   'header':'Должность',     'visible':True,  'width':100})
        super().__init__(tableArg, fldsArg, readonly=True)
    #     self.btnNew.MouseClick += self.createItem
    #     self.btnEdit.MouseClick += self.editItem
        self.btnDelete.MouseClick += self.deleteItem

    # def editItem(self, sender, e):
    #     id = self.getSelectedRowFldValue('id')
    #     name = self.getSelectedRowFldValue('Name')
    #     frm = frmPosition(id, name, self)
    #     frm.ShowDialog()
    
    # def createItem(self, sender, e):
    #     id = guiBaseForm.dummyId
    #     name = ''
    #     frm = frmPosition(id, name, self)
    #     frm.ShowDialog()

    def deleteItem(self, sender, e):
        pass
        
# class frmPosition(guiBaseForm.frmSimpleEditData):
#     def __init__(self, positionId, positionName, parent):
#         super().__init__(tableArg, positionId, positionName)
#         self.parent = parent
#         self.btnSave.MouseClick += self.doSave

#     def doSave(self, sender, e):
#         id = int(self.cntLblTxtId.txt_value.Text)
#         name = self.cntLblTxtName.txt_value.Text
#         if id == guiBaseForm.dummyId:
#             err, newId = dbPositions.new(name)
#         else:
#             err = dbPositions.update(id, name)
#         if err:
#             common.SowErrorMessage(err)
#         else:
#             self.parent.getDataFromDb()
#             self.Close()

