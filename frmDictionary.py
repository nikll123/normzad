import clr
import db
# from pythonnet import load
# load()
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Windows")

import System.Windows.Forms as WinForms
# import System.Windows
from System.Drawing import Size, Point, Color

class frmDictionary(WinForms.Form):
    def __init__(self, tableArg, fldsArg, size=Size(500,300), readonly=False) -> None:
        super().__init__()
        self.Text = tableArg['title']
        self.grd = WinForms.DataGridView()
        self.table = tableArg
        self.flds = fldsArg
        self.Controls.Add(self.grd)
        for f in self.flds:
            col = WinForms.DataGridViewColumn()
            col.CellTemplate = WinForms.DataGridViewTextBoxCell()
            col.Name = f['title']
            col.Visible = f['visible']
            if col.Visible:
                col.Width = f['width']
                col.ReadOnly = f['readonly']
            
            self.grd.Columns.Add(col)
        self.getData()
        self.Resize += self.myResized
        self.Size = size
        self.grd.ReadOnly = readonly
        self.grd.BackgroundColor = self.BackColor
        # self.grd.ForeColor = Color.Red
        
    def myResized(self, parent, e):
        w,h = self.ClientSize.Width, self.ClientSize.Height
        h = max(0, h - 50)
        self.grd.Size = Size(w, h)

    
    
    # def getData():

    def getData(self):
        tableName = self.table['name']
        flds = [f['name'] for f in self.flds]
        err, data = db.select(tableName, flds)
        if err:
            WinForms.MessageBox.Show(err)
        else:
            for row in data:
                self.grd.Rows.Add(row)

    def Execute(self):
        WinForms.Application.Run(self)


