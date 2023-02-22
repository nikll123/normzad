from common import *
import db

# DataGridViewComboBoxColumn 
# https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/how-to-host-controls-in-windows-forms-datagridview-cells?view=netframeworkdesktop-4.8
# col.CellTemplate.ValueType = int

class frmDictionary(WinForms.Form):
    """Базовый класс формы справочника

    это шаблон для создания конкретных справочников,
    родительский класс WinForms.Form
    аргументы:

    argTable - это словарь вида: {'name':'ИмяТаблицыБазыДанных','header':'Заголовок Для Формы'}

    argFlds  - это список словарей вида: 
    [{'fld_name':'ИмяПолявТаблице', 'header':'Заголовок поля', 'visible':True,  'width':300}, ...]

    readonly - если readonly=True - то грид только для чтения (в гриде ячейки нередактируемые)
    """
    def __init__(self, argTable, argFlds, readonly=False):
        super().__init__()
        self.Text = argTable['header']     # Заголовок формы 
        self.tableName = argTable['name']  # сохраняем имя таблицы как свойство формы для последующего использования
        self.flds = argFlds                # сохраняем список полей как свойство формы для последующего использования

        self.btnNew = WinForms.Button()                       # создали кнопку
        self.btnNew.Text = 'Добавить'
        self.btnNew.Location = Point(50, vertInterval)        # ставим кнопку
        self.btnNew.MouseClick += self.createItem             # добавляем обработчик клика по кнопке
        self.Controls.Add(self.btnNew)                        # встраиваем кнопку на форму

        self.btnEdit = WinForms.Button()
        self.btnEdit.Text = 'Изменить'
        self.btnEdit.Location = Point(150, vertInterval)
        self.btnEdit.MouseClick += self.editItem
        self.Controls.Add(self.btnEdit)

        self.btnDelete = WinForms.Button()
        self.btnDelete.Text = 'Удалить' 
        self.btnDelete.Location = Point(250, vertInterval)
        self.btnDelete.MouseClick += self.deleteItem
        self.Controls.Add(self.btnDelete)
        
        self.btnrefresh = WinForms.Button()
        self.btnrefresh.Text = 'Обновить' 
        self.btnrefresh.Location = Point(350, vertInterval)
        self.btnrefresh.MouseClick += self.refreshData
        self.Controls.Add(self.btnrefresh)

        self.grd = WinForms.DataGridView()                                    # создаем объект датагридвью - таблица на форме
        self.grd.Location = Point(0, self.btnrefresh.Bottom + vertInterval)   # ставим грид под кнопки
        self.Controls.Add(self.grd)                                           # встроили грид в форму

        # Создание колонок (филдов) в таблице (гриде)
        for fld in self.flds:
            col = WinForms.DataGridViewColumn()                   # создаем объект новой колонки
            col.CellTemplate = WinForms.DataGridViewTextBoxCell() # устанавливаем шаблон ячейки
            col.Name = fld['fld_name']                            # имя колонки
            col.HeaderText = fld['header']                        # заголовок
            col.Visible = fld['visible']                          # видимая или невидимая
            col.Width = fld['width']                              # ширина
            self.grd.Columns.Add(col)                             # вставляем колонку в грид

        self.getDataFromDb()                                      # выбираем данные из БД и заполняем грид данными
        self.grd.ReadOnly = readonly                              # свойство "только для чтения"
        self.grd.BackgroundColor = self.BackColor                 # цвет заднего фона грида такой же как и цвет фона формы
        self.grd.SelectionMode = WinForms.DataGridViewSelectionMode.FullRowSelect # режим выделения - вся строка
        self.grd.CellDoubleClick += self.dblClick                 # добавляем обработчик двойного клика на ячейке грида

        self.Resize += self.frmIsResized                          # добавляем обработчик события изменения размера формы
        self.Size = Size(500,300)                                 # изменяем размер формы

    def dblClick(self, sender, e):                                # обработчик двойного клика на ячейке грида
        id = self.getSelectedRowValue('id')
        if id == None:
            self.createItem(sender, e)
        else:
            self.editItem(sender, e)

    def frmIsResized(self, sender, e):
        w, h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)
    
    # получить значениЯ полЕЙ в выделеной строке
    def getSelectedRowValues(self, flds):
        values = []
        for f in flds:
            v = self.getSelectedRowValue(f)
            values.append(v)
        return values

    # получить значениЕ поля в выделеной строке
    def getSelectedRowValue(self, fld):
        value = self.grd.SelectedRows[0].Cells[fld].Value
        return value

    def refreshData(self, sender, e):
        self.getDataFromDb()

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

class frmDictionaryItem(WinForms.Form):
    """Бзовый класс формы для редактирования элемента справочника 

    Шаблон для создания конкретных форм, 
    родительский класс WinForms.Form
    
    аргументы:
    argTable, argId, argValue, size=Size(500,300)

    """
    def __init__(self, argTable, argId, argValue, size=Size(500,300)):
        super().__init__()
        self.Size = size                    # установка размера
        self.MinimumSize = size             # фиксация минимального размера
        self.MaximumSize = size             # фиксация максимального размера
        # self.TableName = tableArg['name']   
        self.text = argTable['header']      # заголовок формы

        x = 20  # координата X для выстраивания контролов
        # создаем контейнер с Label и TextBox для Id
        self.cntLblTxtId = cntText(name='lbl', header='Id', readonly = True)
        y = vertInterval                                           # координата Y для первого контейнера
        self.cntLblTxtId.Location = Point(x, y)                 # положения контейнера
        self.cntLblTxtId.txt.Text = str(argId)
        self.Controls.Add(self.cntLblTxtId)                     # вставляем на форму

        # создаем контейнер с Label и TextBox для названия
        self.cntLblTxtName = cntText(name='txt', header='Название')
        y = self.cntLblTxtId.Bottom + vertInterval                 # координата Y для следующего контейнера
        self.cntLblTxtName.Location = Point(x, y)
        self.cntLblTxtName.txt.Text = argValue
        self.Controls.Add(self.cntLblTxtName)                   # вставляем на форму

        # создаем кнопку Save
        self.btnSave = WinForms.Button()
        self.btnSave.Text = 'Сохранить'
        x = int((self.ClientSize.Width - self.btnSave.Size.Width)/ 2) 
        y = self.cntLblTxtName.Bottom + vertInterval
        self.btnSave.Location = Point(x, y)
        self.btnSave.MouseClick += self.doSave                  # цепляем на нее обработчик клика
        self.Controls.Add(self.btnSave)                         # вставляем на форму

    def Execute(self):
        WinForms.Application.Run(self)


# if __name__ == '__main__':
    # table = {'name':'Departments','header':'Справочник', 'readonly':True}
    # cols = []
    # cols.append({'fld_name':'Id',   'header':'Id',       'visible':True, 'readonly':True,   'width':50})
    # cols.append({'fld_name':'Name', 'header':'Название', 'visible':True, 'readonly':False,  'width':300})

    # frm = frmDictionary(table, cols, readonly=True)
    # frm.Execute()

    # frm = frmSimpleObject(tableArg='Справочник', argId=dummyId, argName='testData')
    # frm.ShowDialog()
