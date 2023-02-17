import clr

# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point
import System.Windows

def ShowErrorIfNotEmpty(err):
    isError = err != ''
    if isError:
        WinForms.MessageBox.Show(err, "Ошибка")
    return isError

def ShowQuestionMessage(msg):
    answer = WinForms.MessageBox.Show(msg, "Вопрос", WinForms.MessageBoxButtons.YesNo)
    return answer == WinForms.DialogResult.Yes
    