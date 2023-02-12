import clr
import frmDictionary
import frmDepartments
import frmPositions
import frmTasks
import frmJobList

# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")
import System.Windows.Forms as WinForms
import System.Windows
from System.Drawing import Size, Point

mainForm = WinForms.Form()
mainForm.Text = "Нормированные задания"
mainForm.Size = Size(1500,800)
mainForm.Visible = True
mainForm.IsMdiContainer = True

def activateIfOpened(name):
    res = False
    for frm in mainForm.MdiChildren:
        if frm.Name == name: # already opened
            frm.Activate()
            res = True
            break
    return res

def openFrmDepartments(sender, e):
    frmName = 'frmDeps'
    if activateIfOpened(frmName) == False:
        frm = frmDepartments.frmDepartments()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFrmPositions(sender, e):
    frmName = 'frmPoss'
    if activateIfOpened(frmName) == False:
        frm = frmPositions.frmPositions()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFrmTasks(sender, e):
    frmName = 'frmTasks'
    if activateIfOpened(frmName) == False:
        frm = frmTasks.frmTasks()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFrmJobList(sender, e):
    frmName = 'frmJobList'
    if activateIfOpened(frmName) == False:
        frm = frmJobList.frmJobList()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

ms = WinForms.MenuStrip()
menuDicts = WinForms.ToolStripMenuItem("Справочники")

menuItemDepartments = WinForms.ToolStripMenuItem("Подразделения", None, System.EventHandler(openFrmDepartments))
menuItemPositions = WinForms.ToolStripMenuItem("Должности", None, System.EventHandler(openFrmPositions))
menuItemTasks = WinForms.ToolStripMenuItem("Задания", None, System.EventHandler(openFrmTasks))

menuDicts.DropDownItems.Add(menuItemDepartments)
menuDicts.DropDownItems.Add(menuItemPositions)
menuDicts.DropDownItems.Add(menuItemTasks)

menuTabel = WinForms.ToolStripMenuItem("Табель", None, System.EventHandler(openFrmJobList))

ms.MdiWindowListItem = menuDicts

ms.Items.Add(menuDicts);
ms.Items.Add(menuTabel);
ms.Dock = WinForms.DockStyle.Top
mainForm.MainStrip = ms
mainForm.Controls.Add(ms)

WinForms.Application.Run(mainForm)

