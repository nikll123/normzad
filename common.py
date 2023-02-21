import clr

# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point
import System.Windows

vertInterval = 10   # вертикальный (по оси Y) интервал между объектами на форме
newId = 0           # фиктивный ID, используется во время создания нового объекта

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

# класс - Контейнер содержащий Label и TextBox
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

# класс - Контейнер содержащий Label и комбобокс
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

        self.txt_value = WinForms.ComboBox()
        self.txt_value.Size = Size(150, 24)
        self.txt_value.Location = Point(150,0)
        self.txt_value.ReadOnly = readonly
        self.txt_value.Text = value
        self.Controls.Add(self.txt_value)

