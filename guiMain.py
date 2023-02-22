from common import WinForms, Size, Point, System
import guiDepartments
import guiPositions
import guiTasks
import guiTabel
import guiWorkers

mainForm = WinForms.Form()
mainForm.Text = "Нормированные задания"
mainForm.Size = Size(1500,800)
# mainForm.Visible = True
mainForm.IsMdiContainer = True  # Mdi - multi document interface, форма контейнер для других форм "детей"

def activateIfOpened(name):   # активировать форму если она уже открыта
    res = False
    for frm in mainForm.MdiChildren:   # цикл по "детям" главной формы
        if frm.Name == name: # already opened (уже открыта)
            frm.Activate()   # активировать форму (вывести на первый план)
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

# пункты вертикального меню спавоников 
menuItemDepartments = WinForms.ToolStripMenuItem("Подразделения", None, System.EventHandler(openFormDepartments))
menuItemPositions = WinForms.ToolStripMenuItem("Должности", None, System.EventHandler(openFormPositions))
menuItemTasks = WinForms.ToolStripMenuItem("Задания", None, System.EventHandler(openFormTasks))
menuItemWorkers = WinForms.ToolStripMenuItem("Сотрудники", None, System.EventHandler(openFormWorkerList))

# виртикальное меню справочников
menuDicts = WinForms.ToolStripMenuItem("Справочники")
menuDicts.DropDownItems.Add(menuItemDepartments)
menuDicts.DropDownItems.Add(menuItemPositions)
menuDicts.DropDownItems.Add(menuItemTasks)
menuDicts.DropDownItems.Add(menuItemWorkers)

# пункт меню "Табель"
menuTabel = WinForms.ToolStripMenuItem("Табель", None, System.EventHandler(openFormJobList))

# горизонтальное меню (strip)
menuStrip = WinForms.MenuStrip()  # меню главной формы
menuStrip.Dock = WinForms.DockStyle.Top
menuStrip.Items.Add(menuDicts);
menuStrip.Items.Add(menuTabel);


mainForm.Controls.Add(menuStrip)

WinForms.Application.Run(mainForm)

