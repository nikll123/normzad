import clr

# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point
import System.Windows

def SowErrorMessage(err):
    WinForms.MessageBox.Show(err)

