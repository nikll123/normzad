import clr
import FormDictionary
import frmDepartments
# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")

# import FusionMacro as fm
import System.Windows.Forms as WinForms
import System.Windows
from System.Drawing import Size, Point

f = WinForms.Form()
f.Text = "Нормированные задания"
f.Size = Size(800,500)
f.Visible = True
f.IsMdiContainer = True


# tspTop = WinForms.ToolStripPanel()
# tspTop.Dock = WinForms.DockStyle.Top
# tsTop = WinForms.ToolStrip()
# tsTop.Items.Add("Top")
# tspTop.Join(tsTop)

# f.Controls.Add(tspTop);

def frmDepartments_open(sender, e):
    f1 = frmDepartments.frmDepartments()
    f1.MdiParent = f
    f1.Show()

def frmPositions_open(sender, e):
    f1 = FormDictionary.frmPositions()
    f1.MdiParent = f
    f1.Show()

def frmTasks_open(sender, e):
    f1 = FormDictionary.frmTasks()
    f1.MdiParent = f
    f1.Show()


def frmJobList_open(sender, e):
    f1 = FormDictionary.frmJobList()

    f1.MdiParent = f
    f1.Show()

ms = WinForms.MenuStrip()
menuFile = WinForms.ToolStripMenuItem("Справочники")
menuItemDepartments = WinForms.ToolStripMenuItem("Подразделения", None, System.EventHandler(frmDepartments_open))
menuItemPositions = WinForms.ToolStripMenuItem("Должности", None, System.EventHandler(frmPositions_open))
menuItemTasks = WinForms.ToolStripMenuItem("Задания", None, System.EventHandler(frmTasks_open))
menuItemTabel = WinForms.ToolStripMenuItem("Табель", None, System.EventHandler(frmJobList_open))

menuFile.DropDownItems.Add(menuItemDepartments)
menuFile.DropDownItems.Add(menuItemPositions)
menuFile.DropDownItems.Add(menuItemTasks)
menuFile.DropDownItems.Add(menuItemTabel)

ms.MdiWindowListItem = menuFile
ms.Items.Add(menuFile);
ms.Dock = WinForms.DockStyle.Top
f.MainStrip = ms
f.Controls.Add(ms)

# # Create a GroupBox and add a TextBox to it.
# groupBox1 = WinForms.GroupBox()
# textBox1 = WinForms.TextBox()
# textBox1.Location = Point(100, 30)
# groupBox1.Controls.Add(textBox1)

# groupBox1.Text = " MyGroupBox ";
# groupBox1.Dock = WinForms.DockStyle.Top;

# # groupBox1.Enabled = False

# tlp = WinForms.TableLayoutPanel()
# tlp.Text = "tlp"
# tlp.RowCount = 5
# tlp.BackColor = tlp.BackColor.FromArgb(255,255,122)
# tlp.Dock = tlp.Dock.Bottom
# # tlp.Dock = tlp.Dock.Fill

# # tlp.Rows.Add()

# b = WinForms.Button()
# b.Text = "bbb"
# tlp.Controls.Add(b)
# tlp.Controls.Add(groupBox1)
# f.Controls.Add(tlp)

# def button_Click(self, sender): # , args
#     """Button click event handler"""
#     WinForms.MessageBox.Show("Please do not press this button again.")

# b.Click += button_Click

WinForms.Application.Run(f)

