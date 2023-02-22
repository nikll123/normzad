from common import WinForms, Size, Point, System
import guiDepartments
import guiPositions
import guiTasks
import guiTabel
import guiWorkers

mainForm = WinForms.Form()
mainForm.Text = "Нормированные задания"
mainForm.Size = Size(1500,800)
mainForm.Visible = True
mainForm.IsMdiContainer = True

def activateIfOpened(name):
    res = False
    for frm in mainForm.MdiChildren:
        if frm.Name == name: # already opened (уже открыта)
            frm.Activate()
            res = True
            break
    return res

def openFormDepartments(sender, e):
    frmName = 'frmDeps'
    if activateIfOpened(frmName) == False:
        frm = guiDepartments.frmDepartmentTable()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFormPositions(sender, e):
    frmName = 'frmPositions'
    if activateIfOpened(frmName) == False:
        frm = guiPositions.frmPositions()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFormTasks(sender, e):
    frmName = 'frmTasks'
    if activateIfOpened(frmName) == False:
        frm = guiTasks.frmTasks()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFormJobList(sender, e):
    frmName = 'frmJobList'
    if activateIfOpened(frmName) == False:
        frm = guiTabel.frmJobList()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

def openFormWorkerList(sender, e):
    frmName = 'frmWorkerList'
    if activateIfOpened(frmName) == False:
        frm = guiWorkers.frmWorkers()
        frm.Name = frmName
        frm.MdiParent = mainForm
        frm.Show()

ms = WinForms.MenuStrip()
menuDicts = WinForms.ToolStripMenuItem("Справочники")

menuItemDepartments = WinForms.ToolStripMenuItem("Подразделения", None, System.EventHandler(openFormDepartments))
menuItemPositions = WinForms.ToolStripMenuItem("Должности", None, System.EventHandler(openFormPositions))
menuItemTasks = WinForms.ToolStripMenuItem("Задания", None, System.EventHandler(openFormTasks))
menuItemWorkers = WinForms.ToolStripMenuItem("Сотрудники", None, System.EventHandler(openFormWorkerList))

menuDicts.DropDownItems.Add(menuItemDepartments)
menuDicts.DropDownItems.Add(menuItemPositions)
menuDicts.DropDownItems.Add(menuItemTasks)
menuDicts.DropDownItems.Add(menuItemWorkers)

menuTabel = WinForms.ToolStripMenuItem("Табель", None, System.EventHandler(openFormJobList))

ms.MdiWindowListItem = menuDicts

ms.Items.Add(menuDicts);
ms.Items.Add(menuTabel);
ms.Dock = WinForms.DockStyle.Top
mainForm.MainStrip = ms
mainForm.Controls.Add(ms)

WinForms.Application.Run(mainForm)

