Tkinter
=============

* <http://tkinter.programujte.com/>
* <http://tkinter.py.cz/>
* <http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html>
* <https://docs.python.org/3/library/tkinter.html>
* <https://docs.python.org/3/library/tkinter.ttk.html>


Helo World
---------------

```python
from os.path import basename, splitext
import tkinter as tk
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = 'Foo'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text='Quit', command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()

```
