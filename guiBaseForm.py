from common import WinForms, Size, Point, checkIfError
import db

yInterval = 10  # вертикальный (по оси Y) интервал между объектами на форме
newId = 0       # фиктивный ID, используется во время создания нового объекта

# DataGridViewComboBoxColumn 
# https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/how-to-host-controls-in-windows-forms-datagridview-cells?view=netframeworkdesktop-4.8
# col.CellTemplate.ValueType = int

# базовый класс формы справочника 
# это шаблон для создания конкретных справочников
# родительский класс WinForms.Form
class frmDictionary(WinForms.Form):
    def __init__(self, tableArg, fldsArg, readonly=False):
        super().__init__()
        self.Text = tableArg['header']     # Заголовок формы 
        self.tableName = tableArg['name']  # сохраняем имя таблицы как свойство формы для последующего использования
        self.flds = fldsArg                # сохраняем список полей как свойство формы для последующего использования
        self.grd = WinForms.DataGridView() # создаем объект датагридвью - таблица на форме
        self.Controls.Add(self.grd)        # встроили грид в форму

        # Создание колонок (филдов) в таблице (гриде)
        for fld in self.flds:
            col = WinForms.DataGridViewColumn()                   # создаем объект новой колонки
            col.CellTemplate = WinForms.DataGridViewTextBoxCell() # устанавливаем шаблон ячейки
            col.Name = fld['fld_name']                            # имя колонки
            col.HeaderText = fld['header']                        # заголовок
            col.Visible = fld['visible']                          # видимая или невидимая
            col.Width = fld['width']                              # ширина
            self.grd.Columns.Add(col)                             # вставляем колонку в грид

        self.getDataFromDb()                                      # заполняем грид данными из БД
        self.grd.ReadOnly = readonly                              # свойство "только для чтения"
        self.grd.BackgroundColor = self.BackColor                 # цвет заднего фона грида такой же как и цвет фона формы
        self.grd.SelectionMode = WinForms.DataGridViewSelectionMode.FullRowSelect # режим выделения - вся строка
        self.grd.CellDoubleClick += self.dblClick                 # добавляем обработчик двойного клика на ячейке грида

        self.btnNew = WinForms.Button()                           # создали кнопку
        self.btnNew.Text = 'Добавить'
        self.btnNew.MouseClick += self.createItem                 # добавляем обработчик клика по кнопке
        self.Controls.Add(self.btnNew)                            # встраиваем кнопку на форму

        self.btnEdit = WinForms.Button()
        self.btnEdit.Text = 'Изменить'
        self.btnEdit.MouseClick += self.editItem
        self.Controls.Add(self.btnEdit)

        self.btnDelete = WinForms.Button()
        self.btnDelete.Text = 'Удалить' 
        self.btnDelete.MouseClick += self.deleteItem
        self.Controls.Add(self.btnDelete)
        
        self.Resize += self.frmIsResized                          # добавляем обработчик события изменения размера формы
        self.Size = Size(500,300)                                 # изменяем размер формы

    def dblClick(self, sender, e):                                # обработчик двойного клика на ячейке грида
        id = self.getSelectedFldValue('id')
        if id == None:
            self.createItem(sender, e)
        else:
            self.editItem(sender, e)

    def frmIsResized(self, sender, e):
        w, h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)
        y = self.grd.Location.Y + self.grd.Size.Height + yInterval
        self.btnNew.Location = Point(50, y)
        self.btnEdit.Location = Point(150, y)
        self.btnDelete.Location = Point(250, y)
    
    # получить значение поля в выделеной строке
    def getSelectedFldValue(self, fldName):
        value = self.grd.SelectedRows[0].Cells[fldName].Value
        return value

    # получить данные из БД и поместить их в грид
    def getDataFromDb(self):
        self.grd.Rows.Clear()                          # очистить (удалить) все сторки
        flds = [f['fld_name'] for f in self.flds]      # получить список полей
        err, data = db.select(self.tableName, flds)    # выбрать данные из БД
        isError = checkIfError(err)                    # проверка появления ошибки
        if not isError:                                # если нет ошибки - 
            for row in data:                           # - то данные вставляем в грид
                self.grd.Rows.Add(row)

    def Execute(self):                                 # метод для запуска формы
        WinForms.Application.Run(self)

# класс Контейнера содержащего Label и TextBox
# родительский класс WinForms.ContainerControl
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

# базовый класс формы для редактирования элемента справочника 
# шаблон для создания конкретных форм
# родительский класс WinForms.Form
class frmDictionaryItem(WinForms.Form):
    def __init__(self, tableArg, argId, argValue, size=Size(500,300)):
        super().__init__()
        self.Size = size                    # установка размера
        self.MinimumSize = size             # фиксация минимального размера
        self.MaximumSize = size             # фиксация максимального размера
        # self.TableName = tableArg['name']   
        self.text = tableArg['header']      # заголовок формы

        x = 20  # координата X для выстраивания контролов
        # создаем контейнер с Label и TextBox для Id
        self.cntLblTxtId = cntLblText(name='lbl', header='Id', readonly = True)
        y = yInterval                                           # координата Y для первого контейнера
        self.cntLblTxtId.Location = Point(x, y)                 # положения контейнера
        self.cntLblTxtId.txt_value.Text = str(argId)
        self.Controls.Add(self.cntLblTxtId)                     # вставляем на форму

        # создаем контейнер с Label и TextBox для названия
        self.cntLblTxtName = cntLblText(name='txt', header='Название')
        y = self.cntLblTxtId.Bottom + yInterval                 # координата Y для следующего контейнера
        self.cntLblTxtName.Location = Point(x, y)
        self.cntLblTxtName.txt_value.Text = argValue
        self.Controls.Add(self.cntLblTxtName)                   # вставляем на форму

        # создаем кнопку Save
        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Save'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = self.cntLblTxtName.Bottom + yInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.doSave                  # цепляем на нее обработчик клика
        self.Controls.Add(self.btnSave)                         # вставляем на форму

    def Execute(self):
        WinForms.Application.Run(self)


if __name__ == '__main__':
    table = {'name':'Departments','header':'Справочник', 'readonly':True}
    cols = []
    cols.append({'fld_name':'Id',   'header':'Id',       'visible':True, 'readonly':True,   'width':50})
    cols.append({'fld_name':'Name', 'header':'Название', 'visible':True, 'readonly':False,  'width':300})

    frm = frmDictionary(table, cols, readonly=True)
    frm.Execute()

    # frm = frmSimpleObject(tableArg='Справочник', argId=dummyId, argName='testData')
    # frm.ShowDialog()
