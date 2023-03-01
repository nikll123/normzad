import string
from tkinter import *
from tkinter import font


class AutoComplete:
    def __init__(self):
        self.ent_index = 0

        self.root = Tk()
        self.root.title('AutoComplete')

        self.ent_var = StringVar()
        self.entry = Entry(self.root, textvariable=self.ent_var, width=50)
        self.entry.pack()

        self.list_var = Variable(self.entry)
        self.listbox = Listbox(self.root, listvariable=self.list_var, exportselection=False, activestyle='none', selectmode=SINGLE, width=50)
        self.listbox.pack()

        self.all_fonts = list(font.families())
        self.all_fonts.sort()
        self.all_fonts = self.all_fonts[26:]
        self.non_duplicates_fonts()
        self.lower_case = [f.lower() for f in self.all_fonts]

        self.list_var.set(self.all_fonts)
        self.entry.focus()

        self.entry.bind('<Up>', self.up_direction)
        self.entry.bind('<Tab>', self.tab_completion)
        self.entry.bind('<BackSpace>', self.backspace)
        self.entry.bind('<Down>', self.down_direction)
        self.entry.bind('<KeyPress>', self.key_pressed)
        self.listbox.bind('<<ListboxSelect>>', self.button_click)

        self.default()

        self.root.resizable(0, 0)
        self.root.mainloop()

    def non_duplicates_fonts(self):
        '''Filter fonts starting with same name'''

        prev_family = ' '
        font_families = []

        for family in self.all_fonts:
            if not family.startswith(prev_family):
                font_families.append(family)
                prev_family = family

        self.all_fonts = font_families

    def default(self):
        '''Set default values in entry widget and listbox'''

        self.listbox.selection_set(3)
        self.ent_var.set('Arial')

        self.entry.config(insertofftime=1000000, insertontime=0)
        self.set_selection()

    def key_pressed(self, event=None):
        key = event.keysym

        if key == 'space':
            key = ' '

        if key in string.printable:
            if self.entry.selection_present():
                self.sel = self.entry.index('sel.first') + 1
                self.entry.delete('sel.first', 'sel.last')

            else:
                self.sel = self.entry.index('insert') + 1

            value = self.ent_var.get() + key
            self.ent_var.set(value)
            self.ent_index += 1

            self.entry.icursor(self.ent_index)
            self.auto_complete()

        return 'break'

    def backspace(self, event=None):
        value = self.entry.get()[:-1]
        self.ent_var.set(value)

        if self.ent_index != 0:
            if self.entry.selection_present():
                self.entry.delete('sel.first', 'sel.last')
                self.ent_index = len(self.ent_var.get())

                if self.entry['insertofftime'] == 1000000:  # Restore time of blinking to default
                    self.entry.config(insertofftime=300, insertontime=600)

            else:
                self.ent_index -= 1

        return 'break'

    def tab_completion(self, event=None):
        '''Select all text in entry widget of matched one.
           Also select the same value in listbox'''

        value = self.ent_var.get()

        self.entry.selection_range(0, 'end')
        self.entry.icursor('end')

        index = self.all_fonts.index(value)
        self.listbox.selection_clear(0, 'end')
        self.listbox.selection_set(index)

        self.entry.config(insertofftime=1000000, insertontime=0)
        return 'break'

    def auto_complete(self):
        value = self.ent_var.get().strip().lower()
        matched = [f for f in self.lower_case if f.startswith(value)]

        if matched:
            matched = matched[0]
            index = self.lower_case.index(matched)

            self.ent_var.set(self.all_fonts[index])

            if self.entry.index('insert') == len(matched):
                self.entry.selection_range(0, 'end')
                self.listbox.selection_clear(0, 'end')
                self.listbox.selection_set(index)

            else:
                self.entry.selection_range(self.sel, 'end')

            self.listbox.see(index)

    def down_direction(self, event=None):
        '''Move selection in downwards direction in listbox'''

        index = self.listbox.curselection()[0]

        if index < len(self.all_fonts) - 1:
            index += 1

            self.listbox.selection_clear(0, 'end')
            self.listbox.selection_set(index)
            self.listbox.see(index)

            self.ent_var.set(self.all_fonts[index])
            self.entry.selection_range(0, 'end')

        return 'break'

    def up_direction(self, event=None):
        '''Move selection in upwards direction in listbox'''

        index = self.listbox.curselection()[0]

        if index > 0:
            index -= 1

            self.listbox.selection_clear(0, 'end')
            self.listbox.selection_set(index)
            self.listbox.see(index)

            self.ent_var.set(self.all_fonts[index])
            self.entry.selection_range(0, 'end')

        return 'break'

    def button_click(self, event=None):
        '''When selection is made by clicking'''

        index = self.listbox.curselection()[0]

        self.ent_var.set(self.all_fonts[index])
        self.root.after(10, self.set_selection)

    def set_selection(self):
        '''Select all text in entry widget'''

        self.entry.select_range(0, 'end')
        self.entry.focus()


if __name__ == '__main__':
    AutoComplete()