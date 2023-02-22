import clr
import db

# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point
import System.Windows

vertInterval = 10   # вертикальный (по оси Y) интервал между объектами на форме
dummyId = -1        # фиктивный ID, используется во время создания нового объекта


def checkIfError(err):
    isError = err != ''
    if isError:
        WinForms.MessageBox.Show(err, "Ошибка")
    return isError

def showQuestionMessage(msg):
    answer = WinForms.MessageBox.Show(msg, "Вопрос", WinForms.MessageBoxButtons.YesNo)
    return answer == WinForms.DialogResult.Yes
    
def isArray(var):
    return hasattr(var,'__iter__')

# класс - Контейнер содержащий Label 
# родительский класс WinForms.ContainerControl
class _baseControl(WinForms.ContainerControl):
    def __init__(self, name, header, readonly=False):
        super().__init__()
        self.Name=name
        self.Size = Size(300, 24)

        self.lbl_header = WinForms.Label()
        self.lbl_header.Text = header
        self.lbl_header.Size = Size(150, 24)
        self.lbl_header.Location = Point(0,0)
        self.Controls.Add(self.lbl_header)

# класс - Контейнер содержащий Label и TextBox
# родительский класс _baseControl
class cntText(_baseControl):
    def __init__(self, name, header, value='', readonly=False):
        super().__init__(name, header)

        self.txt = WinForms.TextBox()
        self.txt.Size = Size(150, 24)
        self.txt.Location = Point(150,0)
        self.txt.ReadOnly = readonly
        self.txt.Text = value
        self.Controls.Add(self.txt)

# класс - Контейнер содержащий Label и комбобокс
# родительский класс _baseControl
class cntCombox(_baseControl):
    def __init__(self, name, header, dataSource, idItem, readonly=False):
        super().__init__(name, header)
        self.idItem = idItem
        self.cmbBox = WinForms.ComboBox()
        err, data = db.select(dataSource, ['id', 'name'])
        if not checkIfError(err):
            self.rows = data
            for id, name in data:
                self.cmbBox.Items.Add(name)
                if self.idItem == id:
                    self.cmbBox.Text = name

            self.cmbBox.Size = Size(150, 24)
            self.cmbBox.Location = Point(150,0)
            self.cmbBox.ReadOnly = readonly
            self.Controls.Add(self.cmbBox)
    
    def getId(self):
        for id, name in self.rows:
            if self.cmbBox.Text == name:
                self.idItem = id
